import binascii
import hashlib
import os

import psycopg2


def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                  salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')


def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  provided_password.encode('utf-8'),
                                  salt.encode('ascii'),
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password


def create_database_connection():
    """ Create database connection.
    Returns:
        Database handler
    """
    cnx = psycopg2.connect(
        'postgres://xvpshclnfkhcjq:'
        '091c4fa121d97f8970f1b2c3a0993f9b69b1222a3864e5138a098a5a39502ba5@'
        'ec2-34-195-169-25.compute-1.amazonaws.com:5432/d10mskjniomomv'
    )
    return cnx


def execute_query(query, cnx):
    """ Send query to SQL database server and execute it.
    Args:
        query:  Query to execute
        cnx:    Database handler
    Returns:
        Response from SQL server
    """

    with cnx.cursor() as cursor:
        cursor.execute(query)
        resp = cursor.fetchall()
        return resp


def check_login(login, password):
    cnx = create_database_connection()
    query = f"SELECT id, login, password FROM USERS WHERE login='{login}'"
    resp = execute_query(query, cnx)
    if len(resp) == 0:
        return "0"

    id = resp[0][0]
    stored_login = resp[0][1].strip()
    stored_password = resp[0][2].strip()

    if login == stored_login and verify_password(stored_password, password):
        return id
    else:
        return -1


def add_user(last_name, login, name, password_):
    cnx = create_database_connection()
    password = hash_password(password_)

    query = (f"insert into USERS (lastname, login, name, password) "
             f"values ('{last_name}', '{login}', '{name}', '{password}')")
    with cnx.cursor() as cursor:
        cursor.execute(query)

    cnx.commit()
    cnx.close()

    return check_login(login, password_)


# print(add_user('Kompanowski', 'hkomp', 'Hubert', 'hkomp'))

# print(check_login('jkowalski', 'janek'))


# print(execute_query("SELECT * from USERS", create_database_connection()))