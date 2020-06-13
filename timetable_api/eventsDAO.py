from server.database_operations import execute_query, create_database_connection
from timetable_api.TimetableEvent import TimetableEvent

def drop_and_create_joined_table():
    cnx = create_database_connection()
    cursor = cnx.cursor()
    query = f"DROP TABLE IF EXISTS student_events;"
    cursor.execute(query)
    query = f"""
            CREATE TABLE student_events (
                student_id  int REFERENCES users (id) ON UPDATE CASCADE ON DELETE CASCADE,
                event_id    int REFERENCES events (id) ON UPDATE CASCADE ON DELETE CASCADE,
                CONSTRAINT student_events_pkey PRIMARY KEY (student_id, event_id)
                );"""
    cursor.execute(query)
    cnx.commit()
    cnx.close()


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
    cnx.close()
    return resp

def set_student_events(student_id, events_list):
    cnx = create_database_connection()
    cursor = cnx.cursor()
    cursor.execute("""DELETE FROM student_events where student_id = {};""".format(student_id), cnx)
    for event in events_list:
        cursor.execute("""INSERT INTO student_events (student_id, event_id) VALUES ({}, {});""".format(student_id, event.idx), cnx)
    cnx.commit()
    cnx.close()