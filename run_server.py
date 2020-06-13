from flask import Flask
from flask import request

from server.database_operations import check_login, add_user
from timetable_api.EventJsonMapper import databaseArrayToJson
from timetable_api.eventsDAO import get_all_events
from timetable_api.CoursesPicker import getCoursesList

app = Flask(__name__)


@app.route('/api/login', methods=['GET', 'POST'])
def login():
    req = request.json

    if 'login' in req and 'password' in req:
        i, name, lastname = check_login(req['login'], req['password'])
        return {'id': i, 'name': name, 'lastname':lastname}
    else:
        return {'id': -1, 'name': "", 'lastname':""}


@app.route('/api/register', methods=['GET', 'POST'])
def register():
    req = request.json

    if 'login' in req and 'password' in req:
        i = add_user(req['last_name'], req['login'], req['name'],
                     req['password'])
        return {'id': i}
    else:
        return {'id': -1}


@app.route('/api/get_plan', methods=['GET', 'POST'])
def getting_schedule():
    # req = request.json

    return databaseArrayToJson(get_all_events())

    # if 'group' in req and 'start_date' in req and 'end_date' in req:
    #     return "Not implemented jet"
    #     # return schedule.get_schedule(group, start_date, end_date)
    # else:
    #     return "Not implemented jet"


@app.route('/api/courses', methods=['GET', 'POST'])
def course_picker():
    return getCoursesList()


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
