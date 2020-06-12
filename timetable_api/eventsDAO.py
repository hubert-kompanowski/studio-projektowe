from server.database_operations import execute_query, create_database_connection
from timetable_api.TimetableEvent import TimetableEvent

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

def get_all_events():
    cnx = create_database_connection()
    resp = execute_query("SELECT * FROM events;", cnx)
    cnx.close
    return resp