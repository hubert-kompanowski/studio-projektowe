from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/api/login', methods=['GET', 'POST'])
def login():
    req = request.json

    if 'login' in req and 'password' in req:
        return 'Login successful'
    else:
        return 'Login not successful'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
