import requests
import json
from datetime import datetime
import psycopg2
from server.database_operations import execute_query, create_database_connection
from timetable_api.TimetableEvent import TimetableEvent
from timetable_api.eventsDAO import add_to_database, drop_and_create_table, drop_and_create_joined_table


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


drop_and_create_table()
drop_and_create_joined_table()
get_timetable_and_add_to_database()

