import requests
import json
from datetime import datetime
import psycopg2
from server.database_operations import execute_query, create_database_connection


class TimetableEvent:
    def __init__(self, title, room, teacher, group, day, start, end, info):
        self.title = title
        self.room = room
        self.teacher = teacher
        self.group = group
        self.day = day
        self.start = start
        self.end = end
        self.info = info

    def __str__(self) -> str:
        return self.title + " " + self.room + " " + self.teacher + " " + str(self.group) + " " + str(
            self.day) + " " + str(self.start) + " " + str(self.end)


def drop_and_create_table():
    cnx = create_database_connection()
    cursor = cnx.cursor()
    query = f"DROP TABLE IF EXISTS events;"
    cursor.execute(query)
    query = f"""
        CREATE TABLE events (
            id SERIAL PRIMARY KEY,
            title VARCHAR (60) NOT NULL,
            room VARCHAR (40),
            teacher VARCHAR (50),
            study_group VARCHAR(2),
            day integer,
            start_time time,
            end_time time,
            info VARCHAR(500)
            )
            """
    cursor.execute(query)
    cnx.commit()
    cnx.close()


def add_to_database(event: TimetableEvent, cnx):
    cursor = cnx.cursor()
    query = f"""INSERT INTO events (title, room, teacher, study_group, day, start_time, end_time, info)
                VALUES
                ('{event.title}', '{event.room}', '{event.teacher}', '{event.group}', '{event.day}', '{event.start}', '{event.end}', '{event.info}');"""
    cursor.execute(query)




def get_timetable_and_add_to_database():
    cnx = create_database_connection()
    resp = requests.get(
        "https://planzajec.eaiib.agh.edu.pl/view/timetable/645/events?start=2020-03-02&end=2020-03-07&_=1585327741228")
    dataArray = resp.json()

    dateFormat = '%Y-%m-%dT%H:%M:%S%z'

    for i, currentElement in enumerate(dataArray, start=0):
        group = str(currentElement.get('group')).replace(".1", "a").replace(".2", "b")
        if group == '0':
            title = currentElement.get('title').split(',')[0]
            room = currentElement.get('title').split(',')[1].split('<br/>')[1]
            teacher = currentElement.get('title').split(',')[2]
            if len(currentElement.get('title').split(',')) > 3:
                teacher += currentElement.get('title').split(',')[3].split('<br/>')[0]
        else:
            title = currentElement.get('title').split(',')[0]
            room = currentElement.get('title').split(',')[2].split('<br/>')[1]
            teacher = currentElement.get('title').split(',')[3]
            if len(currentElement.get('title').split(',')) > 4:
                teacher += currentElement.get('title').split(',')[4].split('<br/>')[0]
        day = datetime.strptime(currentElement.get('start'), dateFormat).weekday() + 1
        start = datetime.strptime(currentElement.get('start'), dateFormat).time()
        end = datetime.strptime(currentElement.get('end'), dateFormat).time()
        info = ""
        if len(currentElement.get('title').split('<br/>')) == 3:
            info = currentElement.get('title').split('<br/>')[2]
        teacher = teacher.split(':')[1].strip()
        room = room.split(':')[1].strip()
        event = TimetableEvent(title, room, teacher, group, day, start, end, info)

        print(i, ": ", event)
        add_to_database(event, cnx)
    cnx.commit()
    cnx.close()

def print_all_events():
    cnx = create_database_connection()
    resp = execute_query("SELECT * FROM events;", cnx)
    cnx.close
    print(resp)


drop_and_create_table()
get_timetable_and_add_to_database()

