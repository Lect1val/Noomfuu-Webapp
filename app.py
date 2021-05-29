from flask import Flask, request, jsonify
from flask import render_template

import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("noomfuuproject-f3b69-firebase-adminsdk-mpbf0-0db0cba4ee.json")
firebase_admin.initialize_app(cred)
db = firestore.client()  


app = Flask(__name__)




@app.route('/')
def index():
    
    user_ref = db.collection(u'User')  
    users = user_ref.stream()
    nick_name_list = []
    for user in users:
        nick_name_list.append(u'{}'.format(user.to_dict()['nickName']))
    return render_template('index.html', my_user_lists = nick_name_list)
    

@app.route('/profile')
def profile():
    user_ref = db.collection(u'User')  
    users = user_ref.stream()
    nick_name_list = []
    for user in users:
        nick_name_list.append(u'{}'.format(user.to_dict()['nickName']))
    return render_template('user_profile.html',my_user_lists = nick_name_list)


@app.route('/analytic')
def analytic():
    user_ref = db.collection(u'User')  
    users = user_ref.stream()
    nick_name_list = []
    for user in users:
        nick_name_list.append(u'{}'.format(user.to_dict()['nickName']))
    return render_template('feeling_analytic.html',my_user_lists = nick_name_list)


if __name__ == "__main__":
    app.debug = True    
    app.run()
