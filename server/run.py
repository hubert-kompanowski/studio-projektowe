# import schedule

from flask import Flask
from flask import request

from database_operations import check_login, add_user

app = Flask(__name__)


@app.route('/api/login', methods=['GET', 'POST'])
def login():
    req = request.json

    if 'login' in req and 'password' in req:
        i = check_login(req['login'], req['password'])
        return {'id': i}
    else:
        return {'id': -1}


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
    req = request.json

    if 'group' in req and 'start_date' in req and 'end_date' in req:
        return "Not implemented jet"
        # return schedule.get_schedule(group, start_date, end_date)
    else:
        return "Not implemented jet"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
