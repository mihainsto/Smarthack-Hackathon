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


@app.route('/adregister', methods=['POST'])
def adregister():
    if request.method == 'POST':
        userDetails = request.json
        title = userDetails['title']
        userid = userDetails['userid']
        description = userDetails['description']
        category = userDetails['category']
        location = userDetails['location']
        return register_ad(title,userid,description,category,location)

@app.route('/addetails', methods=['POST'])
def get_adinfo():
    if request.method == 'POST':
        userDetails = request.json
        id = userDetails['id']
        return get_ad_info(id)

@app.route('/addfiltercategorylocation', methods=['POST'])
def get_adinfocategorylocation():
    if request.method == 'POST':
        userDetails = request.json
        location = userDetails['location']
        category = userDetails['category']
        return get_ad_by_location_category(location, category)

@app.route('/changeadstatus', methods=['POST'])
def change_ad_status():
    if request.method == 'POST':
        userDetails = request.json
        ad_id = userDetails['id']
        ad_status = userDetails['status']
        return trigger_ad_activation(ad_id, ad_status)

@app.route('/')
def main():
    return 'hi'


if __name__ == '__main__':
    app.run()