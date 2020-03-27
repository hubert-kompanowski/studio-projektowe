from flask import Flask
from flask import request


app = Flask(__name__)


@app.route('/login',  methods=['GET', 'POST'])
def login():
    req = request.json

    if 'login' in req and 'password' in req:
        return 'Login successful'
    else:
        return 'Login not successful'







