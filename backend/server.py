from flask import Flask, request, json
from flask_cors import CORS
from dbconnection import *
app = Flask(__name__)

CORS(app)
#app.config['SERVER_NAME'] = '172.16.27.180:5000'


@app.route('/auth', methods=['POST'])
def auth():
    if request.method == 'POST':
        userDetails = request.json
        username = userDetails['username']
        password = userDetails['password']
        return check_user(username,password)


@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        userDetails = request.json

        username = userDetails['username']
        password = userDetails['password']
        email = userDetails['email']
        phone_number = userDetails['phone_number']
        return register_user(username,password,email,phone_number)


@app.route('/userdetails', methods=['POST'])
def get_info():
    if request.method == 'POST':
        userDetails = request.json
        id = userDetails['id']
        return get_all_info(id)

@app.route('/')
def main():
    return 'hi'


if __name__ == '__main__':
    app.run()