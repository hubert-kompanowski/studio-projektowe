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
                final       bool,
                CONSTRAINT student_events_pkey PRIMARY KEY (student_id, event_id)
                );"""
    cursor.execute(query)
    cnx.commit()
    cnx.close()


def user_exists(id):
    cnx = create_database_connection()
    resp = execute_query(
        "SELECT * FROM users  WHERE id = {};".format(id), cnx)
    cnx.close()
    if resp:
        return True
    else:
        return False


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


def get_student_events(id, final):
    cnx = create_database_connection()
    if final == False:
        resp = execute_query(
        "SELECT * FROM events LEFT JOIN student_events se on events.id = se.event_id WHERE (student_id = {} and se.final = False) or study_group = '0';".format(id), cnx)
    else:
        resp = execute_query(
        "SELECT * FROM events LEFT JOIN student_events se on events.id = se.event_id WHERE (student_id= {} and se.final = True) or study_group = '0';".format(id), cnx)
    cnx.close()
    return resp




def set_student_events(student_id, events_list, final):
    cnx = create_database_connection()
    cursor = cnx.cursor()
    cursor.execute("""DELETE FROM student_events where student_id = {} and final = {};""".format(student_id, final), cnx)
    for event in events_list:
        cursor.execute(
            """INSERT INTO student_events (student_id, event_id, final) VALUES ({}, {}, {});""".format(student_id, event.idx, final), cnx)
    cnx.commit()
    cnx.close()