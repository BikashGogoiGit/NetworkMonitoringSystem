from __future__ import print_function
import pyrebase
from cgitb import text
from tkinter import font
from turtle import color
from Tools.scripts.dutree import display
from flask import Flask, render_template, request, redirect,jsonify,session,url_for
from flask_restful import Api, Resource
from datetime import datetime
import subprocess
import os
import sys
import platform
#import pyrebase

class User:
    def __init__(self,id,username,password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

users = []
users.append(User(id=1, username='CHABUA',password='chabua'))
users.append(User(id=1, username='NAHARKATIA',password='naharkatia'))
users.append(User(id=1, username='DIBRUGARH_EAST',password='dibrugarh_east'))
users.append(User(id=1, username='DIBRUGARH_WEST',password='dibrugarh_west'))
users.append(User(id=1, username='TINGKHONG_REV',password='tingkhong_rev'))
users.append(User(id=1, username='MORAN',password='moran'))
users.append(User(id=1, username='TENGAKHAT',password='tengakhat'))
users.append(User(id=1, username='DIBRUGARH_WEST_REV_CIRCLE(A)',password='dibrugarh_west_rev_circleA'))
users.append(User(id=1, username='TENGAKHAT_CO(A)',password='tengakhat_coA'))
users.append(User(id=1, username='NAHARKATIA_REV',password='naharkatia'))

app = Flask(__name__)
app.secret_key = 'secret_key'
api = Api(app)

#ips = ["192.168.2.0", "192.32.4.5"]
ip1 = "8.8.8.8"
ip2 = "192.87.67.32"
ip3 = "192.168.3.4"


@app.route('/', methods=['GET'])
def front():
    return render_template('front.html')


@app.route('/chabua', methods=['GET', 'POST'])
def ping():
    ip_list = ["192.168.137.213"]
    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 1").read()
        return render_template('chabua_machine.html', ip1=ip_list) 

@app.route('/naharkatia_circle', methods=['GET', 'POST'])
def naharkatia():
    ip_list = ["8.8.8.8"]
    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 1").read()
        return render_template('naharkatia_machine.html', ip1=ip_list)

@app.route('/dibrugarh_east_circle', methods=['GET', 'POST'])
def dibrugarh_east():
    ip_list = ["8.8.8.8"]
    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 1").read()
        return render_template('dibrugarh_east_machine.html',ip1=ip_list)

@app.route('/dibrugarh_west', methods=['GET', 'POST'])
def dibrugarh_west():
    ip_list = ["8.8.8.8"]
    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 1").read()
        return render_template('dibrugarh_west_machine.html',ip1=ip_list)

@app.route('/tingkhong_rev', methods=['GET', 'POST'])
def tingkhong_rev():
    ip_list = ["8.8.8.8"]
    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 1").read()
        return render_template('tingkhong_rev_machine.html',ip1=ip_list) 

@app.route('/moran', methods=['GET', 'POST'])
def moran():
    ip_list = ["8.8.8.8"]
    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 1").read()
        return render_template('moran_machine.html',ip1=ip_list) 

@app.route('/tengakhat', methods=['GET', 'POST'])
def tengakhat():
    ip_list = ["8.8.8.8"]
    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 1").read()
        return render_template('tengakhat_machine.html',ip1=ip_list)

@app.route('/dibrugarh_west_rev_circleA', methods=['GET', 'POST'])
def dibrugarh_west_rev_circleA():
    ip_list = ["8.8.8.8"]
    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 1").read()
        return render_template('dibrugarh_west_rev_machine.html',ip1=ip_list)

@app.route('/tengakhat_coA', methods=['GET', 'POST'])
def tengakhat_coA():
    ip_list = ["8.8.8.8"]
    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 1").read()
        return render_template('tengakhat_co_machine.html',ip1=ip_list)


@app.route('/naharkatia_rev', methods=['GET', 'POST'])
def naharkatia_rev():
    ip_list = ["8.8.8.8"]
    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 1").read()
        return render_template('naharkatia_rev_machine.html',ip1=ip_list)

#login session

@app.route('/login1', methods=['GET', 'POST'])
def login1():
    if request.method == 'POST':
        session.pop('user_id', None)
        username = request.form['username']
        password = request.form['password']

        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('chabua1'))
        return redirect(url_for('chabua1'))
        
    return render_template('login.html')


@app.route('/chabua1', methods=['GET', 'POST'])
def chabua1():

    return render_template('chabua_machine.html')

#second login session
@app.route('/login2', methods=['GET', 'POST'])
def login2():
    if request.method == 'POST':
        session.pop('user_id', None)
        username = request.form['username']
        password = request.form['password']

        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('naharkatia1'))
        return redirect(url_for('naharkatia1'))
        
    return render_template('login.html')


@app.route('/naharkatia1', methods=['GET', 'POST'])
def naharkatia1():

    return render_template('naharkatia_machine.html')

#third login session
@app.route('/login3', methods=['GET', 'POST'])
def login3():
    if request.method == 'POST':
        session.pop('user_id', None)
        username = request.form['username']
        password = request.form['password']

        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('dibrugarh_east1'))
        return redirect(url_for('dibrugarh_east1'))
        
    return render_template('login.html')


@app.route('/dibrugarh_east1', methods=['GET', 'POST'])
def dibrugarh_east1():

    return render_template('dibrugarh_east_machine.html')

#fourth login session

@app.route('/login4', methods=['GET', 'POST'])
def login4():
    if request.method == 'POST':
        session.pop('user_id', None)
        username = request.form['username']
        password = request.form['password']

        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('dibrugarh_west1'))
        return redirect(url_for('dibrugarh_west1'))
        
    return render_template('login.html')


@app.route('/dibrugarh_west1', methods=['GET', 'POST'])
def dibrugarh_west1():

    return render_template('dibrugarh_west_machine.html')

#fifth login session

@app.route('/login5', methods=['GET', 'POST'])
def login5():
    if request.method == 'POST':
        session.pop('user_id', None)
        username = request.form['username']
        password = request.form['password']

        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('tingkhong_rev1'))
        return redirect(url_for('tingkhong_rev1'))
        
    return render_template('login.html')


@app.route('/tingkhong_rev1', methods=['GET', 'POST'])
def tingkhong_rev1():

    return render_template('tingkhong_rev_machine.html')

#sith login session

@app.route('/login6', methods=['GET', 'POST'])
def login6():
    if request.method == 'POST':
        session.pop('user_id', None)
        username = request.form['username']
        password = request.form['password']

        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('moran1'))
        return redirect(url_for('moran1'))
        
    return render_template('login.html')


@app.route('/moran1', methods=['GET', 'POST'])
def moran1():

    return render_template('moran_machine.html')

#seventh login session

@app.route('/login7', methods=['GET', 'POST'])
def login7():
    if request.method == 'POST':
        session.pop('user_id', None)
        username = request.form['username']
        password = request.form['password']

        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('tengakhat1'))
        return redirect(url_for('tengakhat1'))
        
    return render_template('login.html')


@app.route('/tengakhat1', methods=['GET', 'POST'])
def tengakhat1():

    return render_template('tengakhat_machine.html')


#eight login session
@app.route('/login8', methods=['GET', 'POST'])
def login8():
    if request.method == 'POST':
        session.pop('user_id', None)
        username = request.form['username']
        password = request.form['password']

        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('dibrugarh_west_rev1'))
        return redirect(url_for('dibugarh_west_rev1'))
        
    return render_template('login.html')


@app.route('/dibrugarh_west_rev1', methods=['GET', 'POST'])
def dibrugarh_west_rev1():

    return render_template('dibrugarh_west_rev_machine.html')

#ninth login session
@app.route('/login9', methods=['GET', 'POST'])
def login9():
    if request.method == 'POST':
        session.pop('user_id', None)
        username = request.form['username']
        password = request.form['password']

        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('tengakhat_co1'))
        return redirect(url_for('tengakhat_co1'))
        
    return render_template('login.html')


@app.route('/tengakhat_co1', methods=['GET', 'POST'])
def tengakhat_co1():

    return render_template('tengakhat_co_machine.html')

#tenth login session

@app.route('/login10', methods=['GET', 'POST'])
def login10():
    if request.method == 'POST':
        session.pop('user_id', None)
        username = request.form['username']
        password = request.form['password']

        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('naharkatia_rev1'))
        return redirect(url_for('naharkatia_rev1'))
        
    return render_template('login.html')
#check all ip
@app.route('/allip', methods=['GET', 'POST'])
def allip():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}

    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()


    #chabua circle
    chabua_ip1=db.child("circle").child("chabua").child("machine1").child("id1").get()
    chabua_circle_ip1=(chabua_ip1.val())
    chabua_ip2=db.child("circle").child("chabua").child("machine2").child("id2").get()
    chabua_circle_ip2=(chabua_ip1.val())
    chabua_ip3=db.child("circle").child("chabua").child("machine3").child("id3").get()
    chabua_circle_ip3=(chabua_ip1.val())
    chabua_ip4=db.child("circle").child("chabua").child("machine4").child("id4").get()
    chabua_circle_ip4=(chabua_ip1.val())
    chabua_ip5=db.child("circle").child("chabua").child("machine5").child("id5").get()
    chabua_circle_ip5=(chabua_ip1.val())
    #status
    chabua_status_ip1=db.child("status").child("chabua").child("machine1").child("id1").child("ip").child("ip").get()
    chabua_circle_status_ip1=(chabua_status_ip1.val())
    chabua_status_ip2=db.child("status").child("chabua").child("machine2").child("id2").child("ip").child("ip").get()
    chabua_circle_status_ip2=(chabua_status_ip2.val())
    chabua_status_ip3=db.child("status").child("chabua").child("machine3").child("id3").child("ip").child("ip").get()
    chabua_circle_status_ip3=(chabua_status_ip3.val())
    chabua_status_ip4=db.child("status").child("chabua").child("machine4").child("id4").child("ip").child("ip").get()
    chabua_circle_status_ip4=(chabua_status_ip4.val())
    chabua_status_ip5=db.child("status").child("chabua").child("machine5").child("id5").child("ip").child("ip").get()
    chabua_circle_status_ip5=(chabua_status_ip5.val())

    #dibrugarh_east circle
    dibrugarh_east_ip1=db.child("circle").child("dibrugarh_east").child("machine1").child("id1").get()
    dibrugarh_east_circle_ip1=(dibrugarh_east_ip1.val())
    dibrugarh_east_ip2=db.child("circle").child("dibrugarh_east").child("machine2").child("id2").get()
    dibrugarh_east_circle_ip2=(dibrugarh_east_ip2.val())
    dibrugarh_east_ip3=db.child("circle").child("dibrugarh_east").child("machine3").child("id3").get()
    dibrugarh_east_circle_ip3=(dibrugarh_east_ip3.val())
    dibrugarh_east_ip4=db.child("circle").child("dibrugarh_east").child("machine4").child("id4").get()
    dibrugarh_east_circle_ip4=(dibrugarh_east_ip4.val())
    dibrugarh_east_ip5=db.child("circle").child("dibrugarh_east").child("machine5").child("id5").get()
    dibrugarh_east_circle_ip5=(dibrugarh_east_ip5.val())
    #status
    dibrugarh_east_status_ip1=db.child("status").child("dibrugarh_east").child("machine1").child("id1").child("ip").child("ip").get()
    dibrugarh_east_circle_status_ip1=(dibrugarh_east_status_ip1.val())
    dibrugarh_east_status_ip2=db.child("status").child("dibrugarh_east").child("machine2").child("id2").child("ip").child("ip").get()
    dibrugarh_east_circle_status_ip2=(dibrugarh_east_status_ip2.val())
    dibrugarh_east_status_ip3=db.child("status").child("dibrugarh_east").child("machine3").child("id3").child("ip").child("ip").get()
    dibrugarh_east_circle_status_ip3=(dibrugarh_east_status_ip3.val())
    dibrugarh_east_status_ip4=db.child("status").child("dibrugarh_east").child("machine4").child("id4").child("ip").child("ip").get()
    dibrugarh_east_circle_status_ip4=(dibrugarh_east_status_ip4.val())
    dibrugarh_east_status_ip5=db.child("status").child("dibrugarh_east").child("machine5").child("id5").child("ip").child("ip").get()
    dibrugarh_east_circle_status_ip5=(dibrugarh_east_status_ip5.val())


    #dibrugarh_west circle
    dibrugarh_west_ip1=db.child("circle").child("dibrugarh_west").child("machine1").child("id1").get()
    dibrugarh_west_circle_ip1=(dibrugarh_west_ip1.val())
    dibrugarh_west_ip2=db.child("circle").child("dibrugarh_west").child("machine2").child("id2").get()
    dibrugarh_west_circle_ip2=(dibrugarh_west_ip2.val())
    dibrugarh_west_ip3=db.child("circle").child("dibrugarh_west").child("machine3").child("id3").get()
    dibrugarh_west_circle_ip3=(dibrugarh_west_ip3.val())
    dibrugarh_west_ip4=db.child("circle").child("dibrugarh_west").child("machine4").child("id4").get()
    dibrugarh_west_circle_ip4=(dibrugarh_west_ip4.val())
    dibrugarh_west_ip5=db.child("circle").child("dibrugarh_west").child("machine5").child("id5").get()
    dibrugarh_west_circle_ip5=(dibrugarh_west_ip5.val())
    #status
    dibrugarh_west_status_ip1=db.child("status").child("dibrugarh_west").child("machine1").child("id1").child("ip").child("ip").get()
    dibrugarh_west_circle_status_ip1=(dibrugarh_west_status_ip1.val())
    dibrugarh_west_status_ip2=db.child("status").child("dibrugarh_west").child("machine2").child("id2").child("ip").child("ip").get()
    dibrugarh_west_circle_status_ip2=(dibrugarh_west_status_ip2.val())
    dibrugarh_west_status_ip3=db.child("status").child("dibrugarh_west").child("machine3").child("id3").child("ip").child("ip").get()
    dibrugarh_west_circle_status_ip3=(dibrugarh_west_status_ip3.val())
    dibrugarh_west_status_ip4=db.child("status").child("dibrugarh_west").child("machine4").child("id4").child("ip").child("ip").get()
    dibrugarh_west_circle_status_ip4=(dibrugarh_west_status_ip4.val())
    dibrugarh_west_status_ip5=db.child("status").child("dibrugarh_west").child("machine5").child("id5").child("ip").child("ip").get()
    dibrugarh_west_circle_status_ip5=(dibrugarh_west_status_ip5.val())


    #dibrugarh_west_rev circle
    dibrugarh_west_rev_circle_ip1=db.child("circle").child("dibrugarh_west_rev_circle").child("machine1").child("id1").get()
    dibrugarh_west_rev_circle_circle_ip1=(dibrugarh_west_rev_circle_ip1.val())
    dibrugarh_west_rev_circle_ip2=db.child("circle").child("dibrugarh_west_rev_circle").child("machine2").child("id2").get()
    dibrugarh_west_rev_circle_circle_ip2=(dibrugarh_west_rev_circle_ip2.val())
    dibrugarh_west_rev_circle_ip3=db.child("circle").child("dibrugarh_west_rev_circle").child("machine3").child("id3").get()
    dibrugarh_west_rev_circle_circle_ip3=(dibrugarh_west_rev_circle_ip3.val())
    dibrugarh_west_rev_circle_ip4=db.child("circle").child("dibrugarh_west_rev_circle").child("machine4").child("id4").get()
    dibrugarh_west_rev_circle_circle_ip4=(dibrugarh_west_rev_circle_ip1.val())
    dibrugarh_west_rev_circle_ip5=db.child("circle").child("dibrugarh_west_rev_circle").child("machine5").child("id5").get()
    dibrugarh_west_rev_circle_circle_ip5=(dibrugarh_west_rev_circle_ip5.val())
    #status
    dibrugarh_west_rev_circle_status_ip1=db.child("status").child("dibrugarh_west_rev_circle").child("machine1").child("id1").child("ip").child("ip").get()
    dibrugarh_west_rev_circle_circle_status_ip1=(dibrugarh_west_rev_circle_status_ip1.val())
    dibrugarh_west_rev_circle_status_ip2=db.child("status").child("dibrugarh_west_rev_circle").child("machine2").child("id2").child("ip").child("ip").get()
    dibrugarh_west_rev_circle_circle_status_ip2=(dibrugarh_west_rev_circle_status_ip2.val())
    dibrugarh_west_rev_circle_status_ip3=db.child("status").child("dibrugarh_west_rev_circle").child("machine3").child("id3").child("ip").child("ip").get()
    dibrugarh_west_rev_circle_circle_status_ip3=(dibrugarh_west_rev_circle_status_ip3.val())
    dibrugarh_west_rev_circle_status_ip4=db.child("status").child("dibrugarh_west_rev_circle").child("machine4").child("id4").child("ip").child("ip").get()
    dibrugarh_west_rev_circle_circle_status_ip4=(dibrugarh_west_rev_circle_status_ip4.val())
    dibrugarh_west_rev_circle_status_ip5=db.child("status").child("dibrugarh_west_rev_circle").child("machine5").child("id5").child("ip").child("ip").get()
    dibrugarh_west_rev_circle_circle_status_ip5=(dibrugarh_west_rev_circle_status_ip5.val())

    #moran circle
    moran_ip1=db.child("circle").child("moran").child("machine1").child("id1").get()
    moran_circle_ip1=(moran_ip1.val())
    moran_ip2=db.child("circle").child("moran").child("machine2").child("id2").get()
    moran_circle_ip2=(moran_ip2.val())
    moran_ip3=db.child("circle").child("moran").child("machine3").child("id3").get()
    moran_circle_ip3=(moran_ip3.val())
    moran_ip4=db.child("circle").child("moran").child("machine4").child("id4").get()
    moran_circle_ip4=(moran_ip4.val())
    moran_ip5=db.child("circle").child("moran").child("machine5").child("id5").get()
    moran_circle_ip5=(moran_ip4.val())
    #status
    moran_status_ip1=db.child("status").child("moran").child("machine1").child("id1").child("ip").child("ip").get()
    moran_circle_status_ip1=(moran_status_ip1.val())
    moran_status_ip2=db.child("status").child("moran").child("machine2").child("id2").child("ip").child("ip").get()
    moran_circle_status_ip2=(moran_status_ip2.val())
    moran_status_ip3=db.child("status").child("moran").child("machine3").child("id3").child("ip").child("ip").get()
    moran_circle_status_ip3=(moran_status_ip3.val())
    moran_status_ip4=db.child("status").child("moran").child("machine4").child("id4").child("ip").child("ip").get()
    moran_circle_status_ip4=(moran_status_ip4.val())
    moran_status_ip5=db.child("status").child("moran").child("machine5").child("id5").child("ip").child("ip").get()
    moran_circle_status_ip5=(moran_status_ip5.val())

    #naharkatia circle
    naharkatia_ip1=db.child("circle").child("naharkatia").child("machine1").child("id1").get()
    naharkatia_circle_ip1=(naharkatia_ip1.val())
    naharkatia_ip2=db.child("circle").child("naharkatia").child("machine2").child("id2").get()
    naharkatia_circle_ip2=(naharkatia_ip2.val())
    naharkatia_ip3=db.child("circle").child("naharkatia").child("machine3").child("id3").get()
    naharkatia_circle_ip3=(naharkatia_ip3.val())
    naharkatia_ip4=db.child("circle").child("naharkatia").child("machine4").child("id4").get()
    naharkatia_circle_ip4=(naharkatia_ip4.val())
    naharkatia_ip5=db.child("circle").child("naharkatia").child("machine5").child("id5").get()
    naharkatia_circle_ip5=(naharkatia_ip5.val())
    #status
    naharkatia_status_ip1=db.child("status").child("naharkatia").child("machine1").child("id1").child("ip").child("ip").get()
    naharkatia_circle_status_ip1=(naharkatia_status_ip1.val())
    naharkatia_status_ip2=db.child("status").child("naharkatia").child("machine2").child("id2").child("ip").child("ip").get()
    naharkatia_circle_status_ip2=(naharkatia_status_ip2.val())
    naharkatia_status_ip3=db.child("status").child("naharkatia").child("machine3").child("id3").child("ip").child("ip").get()
    naharkatia_circle_status_ip3=(naharkatia_status_ip3.val())
    naharkatia_status_ip4=db.child("status").child("naharkatia").child("machine4").child("id4").child("ip").child("ip").get()
    naharkatia_circle_status_ip4=(naharkatia_status_ip4.val())
    naharkatia_status_ip5=db.child("status").child("naharkatia").child("machine5").child("id5").child("ip").child("ip").get()
    naharkatia_circle_status_ip5=(naharkatia_status_ip5.val())

    #naharkatia_rev circle
    naharkatia_rev_ip1=db.child("circle").child("naharkatia_rev").child("machine1").child("id1").get()
    naharkatia_rev_circle_ip1=(naharkatia_rev_ip1.val())
    naharkatia_rev_ip2=db.child("circle").child("naharkatia_rev").child("machine2").child("id2").get()
    naharkatia_rev_circle_ip2=(naharkatia_rev_ip2.val())
    naharkatia_rev_ip3=db.child("circle").child("naharkatia_rev").child("machine3").child("id3").get()
    naharkatia_rev_circle_ip3=(naharkatia_rev_ip3.val())
    naharkatia_rev_ip4=db.child("circle").child("naharkatia_rev").child("machine4").child("id4").get()
    naharkatia_rev_circle_ip4=(naharkatia_rev_ip4.val())
    naharkatia_rev_ip5=db.child("circle").child("naharkatia_rev").child("machine5").child("id5").get()
    naharkatia_rev_circle_ip5=(naharkatia_rev_ip5.val())
    #status
    naharkatia_rev_status_ip1=db.child("status").child("naharkatia_rev").child("machine1").child("id1").child("ip").child("ip").get()
    naharkatia_rev_circle_status_ip1=(naharkatia_rev_status_ip1.val())
    naharkatia_rev_status_ip2=db.child("status").child("naharkatia_rev").child("machine2").child("id2").child("ip").child("ip").get()
    naharkatia_rev_circle_status_ip2=(naharkatia_rev_status_ip2.val())
    naharkatia_rev_status_ip3=db.child("status").child("naharkatia_rev").child("machine3").child("id3").child("ip").child("ip").get()
    naharkatia_rev_circle_status_ip3=(naharkatia_rev_status_ip3.val())
    naharkatia_rev_status_ip4=db.child("status").child("naharkatia_rev").child("machine4").child("id4").child("ip").child("ip").get()
    naharkatia_rev_circle_status_ip4=(naharkatia_rev_status_ip4.val())
    naharkatia_rev_status_ip5=db.child("status").child("naharkatia_rev").child("machine5").child("id5").child("ip").child("ip").get()
    naharkatia_rev_circle_status_ip5=(naharkatia_rev_status_ip5.val())

    #tengakhat circle
    tengakhat_ip1=db.child("circle").child("tengakhat").child("machine1").child("id1").get()
    tengakhat_circle_ip1=(tengakhat_ip1.val())
    tengakhat_ip2=db.child("circle").child("tengakhat").child("machine2").child("id2").get()
    tengakhat_circle_ip2=(tengakhat_ip2.val())
    tengakhat_ip3=db.child("circle").child("tengakhat").child("machine3").child("id3").get()
    tengakhat_circle_ip3=(tengakhat_ip3.val())
    tengakhat_ip4=db.child("circle").child("tengakhat").child("machine4").child("id4").get()
    tengakhat_circle_ip4=(tengakhat_ip4.val())
    tengakhat_ip5=db.child("circle").child("tengakhat").child("machine5").child("id5").get()
    tengakhat_circle_ip5=(tengakhat_ip5.val())
    #status
    tengakhat_status_ip1=db.child("status").child("tengakhat").child("machine1").child("id1").child("ip").child("ip").get()
    tengakhat_circle_status_ip1=(tengakhat_status_ip1.val())
    tengakhat_status_ip2=db.child("status").child("tengakhat").child("machine2").child("id2").child("ip").child("ip").get()
    tengakhat_circle_status_ip2=(tengakhat_status_ip2.val())
    tengakhat_status_ip3=db.child("status").child("tengakhat").child("machine3").child("id3").child("ip").child("ip").get()
    tengakhat_circle_status_ip3=(tengakhat_status_ip3.val())
    tengakhat_status_ip4=db.child("status").child("tengakhat").child("machine4").child("id4").child("ip").child("ip").get()
    tengakhat_circle_status_ip4=(tengakhat_status_ip4.val())
    tengakhat_status_ip5=db.child("status").child("tengakhat").child("machine5").child("id5").child("ip").child("ip").get()
    tengakhat_circle_status_ip5=(tengakhat_status_ip5.val())

    #tengakhat_co circle
    tengakhat_co_ip1=db.child("circle").child("tengakhat_co").child("machine1").child("id1").get()
    tengakhat_co_circle_ip1=(tengakhat_co_ip1.val())
    tengakhat_co_ip2=db.child("circle").child("tengakhat_co").child("machine2").child("id2").get()
    tengakhat_co_circle_ip2=(tengakhat_co_ip2.val())
    tengakhat_co_ip3=db.child("circle").child("tengakhat_co").child("machine3").child("id3").get()
    tengakhat_co_circle_ip3=(tengakhat_co_ip3.val())
    tengakhat_co_ip4=db.child("circle").child("tengakhat_co").child("machine4").child("id4").get()
    tengakhat_co_circle_ip4=(tengakhat_co_ip4.val())
    tengakhat_co_ip5=db.child("circle").child("tengakhat_co").child("machine5").child("id5").get()
    tengakhat_co_circle_ip5=(tengakhat_co_ip5.val())
    #status
    tengakhat_co_status_ip1=db.child("status").child("tengakhat_co").child("machine1").child("id1").child("ip").child("ip").get()
    tengakhat_co_circle_status_ip1=(tengakhat_co_status_ip1.val())
    tengakhat_co_status_ip2=db.child("status").child("tengakhat_co").child("machine2").child("id2").child("ip").child("ip").get()
    tengakhat_co_circle_status_ip2=(tengakhat_co_status_ip2.val())
    tengakhat_co_status_ip3=db.child("status").child("tengakhat_co").child("machine3").child("id3").child("ip").child("ip").get()
    tengakhat_co_circle_status_ip3=(tengakhat_co_status_ip3.val())
    tengakhat_co_status_ip4=db.child("status").child("tengakhat_co").child("machine4").child("id4").child("ip").child("ip").get()
    tengakhat_co_circle_status_ip4=(tengakhat_co_status_ip4.val())
    tengakhat_co_status_ip5=db.child("status").child("tengakhat_co").child("machine5").child("id5").child("ip").child("ip").get()
    tengakhat_co_circle_status_ip5=(tengakhat_co_status_ip5.val())

    #tingkhong_rev circle
    tingkhong_rev_ip1=db.child("circle").child("tingkhong_rev").child("machine1").child("id1").get()
    tingkhong_rev_circle_ip1=(tingkhong_rev_ip1.val())
    tingkhong_rev_ip2=db.child("circle").child("tingkhong_rev").child("machine2").child("id2").get()
    tingkhong_rev_circle_ip2=(tingkhong_rev_ip2.val())
    tingkhong_rev_ip3=db.child("circle").child("tingkhong_rev").child("machine3").child("id3").get()
    tingkhong_rev_circle_ip3=(tingkhong_rev_ip3.val())
    tingkhong_rev_ip4=db.child("circle").child("tingkhong_rev").child("machine4").child("id4").get()
    tingkhong_rev_circle_ip4=(tingkhong_rev_ip4.val())
    tingkhong_rev_ip5=db.child("circle").child("tingkhong_rev").child("machine5").child("id5").get()
    tingkhong_rev_circle_ip5=(tingkhong_rev_ip5.val())
    #status
    tingkhong_rev_status_ip1=db.child("status").child("tingkhong_rev").child("machine1").child("id1").child("ip").child("ip").get()
    tingkhong_rev_circle_status_ip1=(tingkhong_rev_status_ip1.val())
    tingkhong_rev_status_ip2=db.child("status").child("tingkhong_rev").child("machine2").child("id2").child("ip").child("ip").get()
    tingkhong_rev_circle_status_ip2=(tingkhong_rev_status_ip2.val())
    tingkhong_rev_status_ip3=db.child("status").child("tingkhong_rev").child("machine3").child("id3").child("ip").child("ip").get()
    tingkhong_rev_circle_status_ip3=(tingkhong_rev_status_ip3.val())
    tingkhong_rev_status_ip4=db.child("status").child("tingkhong_rev").child("machine4").child("id4").child("ip").child("ip").get()
    tingkhong_rev_circle_status_ip4=(tingkhong_rev_status_ip4.val())
    tingkhong_rev_status_ip5=db.child("status").child("tingkhong_rev").child("machine5").child("id5").child("ip").child("ip").get()
    tingkhong_rev_circle_status_ip5=(tingkhong_rev_status_ip5.val())

    return f'''
          <html>
<head></head>
<body style="background-color: #F89471 ">
<div style="border:2px,solid"><section>
    <aside style="width: 100%; background-color: #DAF7A6 ;height: 50px;font-size: 30px;text-align: center;border:2px,solid;font-weight:bold">DIBRUGARH_DISTRICT</aside>
</section>
</div>
<div>

    <table align="left" style="width: 100%;height: 80px;">
        <tr style="background-color: #B0F871  ">
            <th>CIRCLE</th>
            <th>MACHINE</th>
            <th>IP_ADDRESS</th>
            <th>STATUS</th>
        </tr>
        <!-- chabua circle -->
        <tr style="background-color: #F8F071 ">
            <th>CHABUA</th>
            <th>DESKTOP-A
            </th>
            <th>{chabua_circle_ip1}
            </th>
            <th style="background-color:#27AE60;">{chabua_circle_status_ip1}
            </th>
        </tr>
        <tr style="background-color: #F8F071 ">
            <th>CHABUA</th>
            <th>DESKTOP-B
            </th>
            <th>{chabua_circle_ip2}
            </th>
            <th style="background-color:#27AE60;">{chabua_circle_status_ip2}
            </th>
        </tr>
        <tr style="background-color: #F8F071 ">
            <th>CHABUA</th>
            <th>DESKTOP-C
            </th>
            <th>{chabua_circle_ip3}
            </th>
            <th style="background-color:#27AE60;">{chabua_circle_status_ip3}
            </th>
        </tr>
        <tr style="background-color: #F8F071 ">
            <th>CHABUA</th>
            <th>DESKTOP-D
            </th>
            <th>{chabua_circle_ip4}
            </th>
            <th style="background-color:#27AE60;">{chabua_circle_status_ip4}
            </th>
        </tr>
        <tr style="background-color: #F8F071 ">
            <th>CHABUA</th>
            <th>DESKTOP-E
            </th>
            <th>{chabua_circle_ip5}
            </th>
            <th style="background-color:#27AE60;">{chabua_circle_status_ip5}
            </th>
        </tr>
        <!--dibrugarh east-->
        <tr style="background-color: #F8F071 ">
            <th>DIBRUGARH_EAST</th>
            <th>DESKTOP-A
            </th>
            <th>{dibrugarh_east_circle_ip1}
            </th>
            <th style="background-color:#27AE60;">{dibrugarh_east_circle_status_ip1}
            </th>
        </tr>
        <tr style="background-color: #F8F071 ">
            <th>DIBRUGARH_EAST</th>
            <th>DESKTOP-B
            </th>
            <th>{dibrugarh_east_circle_ip2}
            </th>
            <th style="background-color:#27AE60;">{dibrugarh_east_circle_status_ip2}
            </th>
        </tr>
        <tr style="background-color: #F8F071 ">
            <th>DIBRUGARH_EAST</th>
            <th>DESKTOP-C
            </th>
            <th>{dibrugarh_east_circle_ip3}
            </th>
            <th style="background-color:#27AE60;">{dibrugarh_east_circle_status_ip3}
            </th>
        </tr>
        <tr style="background-color: #F8F071 ">
            <th>DIBRUGARH_EAST</th>
            <th>DESKTOP-D
            </th>
            <th>{dibrugarh_east_circle_ip4}
            </th>
            <th style="background-color:#27AE60;">{dibrugarh_east_circle_status_ip4}
            </th>
        </tr>
        <tr style="background-color: #F8F071 ">
            <th>DIBRUGARH_EAST</th>
            <th>DESKTOP-E
            </th>
            <th>{dibrugarh_east_circle_ip5}
            </th>
            <th style="background-color:#27AE60;">{dibrugarh_east_circle_status_ip5}
            </th>
        </tr>
        
        <!--dibrugarh west-->
        <tr style="background-color: #F8F071 ">
            <th>DIBRUGARH_WEST</th>
            <th>DESKTOP-A
            </th>
            <th>{dibrugarh_west_circle_ip1}
            </th>
            <th style="background-color:#27AE60;">{dibrugarh_west_circle_status_ip1}
            </th>
        </tr>
        <tr style="background-color: #F8F071 ">
            <th>DIBRUGARH_WEST</th>
            <th>DESKTOP-B
            </th>
            <th>{dibrugarh_west_circle_ip2}
            </th>
            <th style="background-color:#27AE60;">{dibrugarh_west_circle_status_ip2}
            </th>
        </tr>
        <tr style="background-color: #F8F071 ">
            <th>DIBRUGARH_WEST</th>
            <th>DESKTOP-C
            </th>
            <th>{dibrugarh_west_circle_ip3}
            </th>
            <th style="background-color:#27AE60;">{dibrugarh_west_circle_status_ip3}
            </th>
        </tr>
        <tr style="background-color: #F8F071 ">
            <th>DIBRUGARH_WEST</th>
            <th>DESKTOP-D
            </th>
            <th>{dibrugarh_west_circle_ip4}
            </th>
            <th style="background-color:#27AE60;">{dibrugarh_west_circle_status_ip4}
            </th>
        </tr>
        <tr style="background-color: #F8F071 ">
            <th>DIBRUGARH_WEST</th>
            <th>DESKTOP-E
            </th>
            <th>{dibrugarh_west_circle_ip5}
            </th>
            <th style="background-color:#27AE60;">{dibrugarh_west_circle_status_ip5}
            </th>
        </tr>
        
        <!--dibrugarh west rev circle-->
        <tr style="background-color: #F8F071 ">
            <th>DIBRUGARH_WEST_REV</th>
            <th>DESKTOP-A
            </th>
            <th>{dibrugarh_west_rev_circle_circle_ip1}
            </th>
            <th style="background-color:#27AE60;">{dibrugarh_west_rev_circle_circle_status_ip1}
            </th>
        </tr>
        <tr style="background-color: #F8F071 ">
            <th>DIBRUGARH_WEST_REV</th>
            <th>DESKTOP-B
            </th>
            <th>{dibrugarh_west_rev_circle_circle_ip2}
            </th>
            <th style="background-color:#27AE60;">{dibrugarh_west_rev_circle_circle_status_ip2}
            </th>
        </tr>
        <tr style="background-color: #F8F071 ">
            <th>DIBRUGARH_WEST_REV</th>
            <th>DESKTOP-C
            </th>
            <th>{dibrugarh_west_rev_circle_circle_ip3}
            </th>
            <th style="background-color:#27AE60;">{dibrugarh_west_rev_circle_circle_status_ip3}
            </th>
        </tr>
        <tr style="background-color: #F8F071 ">
            <th>DIBRUGARH_WEST_REV</th>
            <th>DESKTOP-D
            </th>
            <th>{dibrugarh_west_rev_circle_circle_ip4}
            </th>
            <th style="background-color:#27AE60;">{dibrugarh_west_rev_circle_circle_status_ip4}
            </th>
        </tr>
        <tr style="background-color: #F8F071 ">
            <th>DIBRUGARH_WEST_REV</th>
            <th>DESKTOP-E
            </th>
            <th>{dibrugarh_west_rev_circle_circle_ip5}
            </th>
            <th style="background-color:#27AE60;">{dibrugarh_west_rev_circle_circle_status_ip5}
            </th>
        </tr>
        
        <!--MORAN-->
        <tr style="background-color: #F8F071 ">
            <th>MORAN</th>
            <th>DESKTOP-A
            </th>
            <th>{moran_circle_ip1}
            </th>
            <th style="background-color:#27AE60;">{moran_circle_status_ip1}
            </th>
        </tr>
        <tr style="background-color: #F8F071 ">
            <th>MORAN</th>
            <th>DESKTOP-B
            </th>
            <th>{moran_circle_ip2}
            </th>
            <th style="background-color:#27AE60;">{moran_circle_status_ip2}
            </th>
        </tr>
        <tr style="background-color: #F8F071 ">
            <th>MORAN</th>
            <th>DESKTOP-C
            </th>
            <th>{moran_circle_ip3}
            </th>
            <th style="background-color:#27AE60;">{moran_circle_status_ip3}
            </th>
        </tr>
        <tr style="background-color: #F8F071 ">
            <th>MORAN</th>
            <th>DESKTOP-D
            </th>
            <th>{moran_circle_ip4}
            </th>
            <th style="background-color:#27AE60;">{moran_circle_status_ip4}
            </th>
        </tr>
        <tr style="background-color: #F8F071 ">
            <th>MORAN</th>
            <th>DESKTOP-E
            </th>
            <th>{moran_circle_ip5}
            </th>
            <th style="background-color:#27AE60;">{moran_circle_status_ip5}
            </th>
        </tr>
        
        <!--NAHARKATIA-->
        <tr style="background-color: #F8F071 ">
            <th>NAHARKATIA</th>
            <th>DESKTOP-A
            </th>
            <th>{naharkatia_circle_ip1}
            </th>
            <th style="background-color:#27AE60;">{naharkatia_circle_status_ip1}
            </th>
        </tr>
        <tr style="background-color: #F8F071 ">
            <th>NAHARKATIA</th>
            <th>DESKTOP-B
            </th>
            <th>{naharkatia_circle_ip2}
            </th>
            <th style="background-color:#27AE60;">{naharkatia_circle_status_ip2}
            </th>
        </tr>
        <tr style="background-color: #F8F071 ">
            <th>NAHARKATIA</th>
            <th>DESKTOP-C
            </th>
            <th>{naharkatia_circle_ip3}
            </th>
            <th style="background-color:#27AE60;">{naharkatia_circle_status_ip3}
            </th>
        </tr>
        <tr style="background-color: #F8F071 ">
            <th>NAHARKATIA</th>
            <th>DESKTOP-D
            </th>
            <th>{naharkatia_circle_ip4}
            </th>
            <th style="background-color:#27AE60;">{naharkatia_circle_status_ip4}
            </th>
        </tr>
        <tr style="background-color: #F8F071 ">
            <th>NAHARKATIA</th>
            <th>DESKTOP-E
            </th>
            <th>{naharkatia_circle_ip5}
            </th>
            <th style="background-color:#27AE60;">{naharkatia_circle_status_ip5}
            </th>
        </tr>
        
        <!--NAHARKATIA_REV-->
        <tr style="background-color: #F8F071 ">
            <th>NAHARKATIA_REV</th>
            <th>DESKTOP-A
            </th>
            <th>{naharkatia_rev_circle_ip1}
            </th>
            <th style="background-color:#27AE60;">{naharkatia_rev_circle_status_ip1}
            </th>
        </tr>
        <tr style="background-color: #F8F071 ">
            <th>NAHARKATIA_REV</th>
            <th>DESKTOP-B
            </th>
            <th>{naharkatia_rev_circle_ip2}
            </th>
            <th style="background-color:#27AE60;">{naharkatia_rev_circle_status_ip2}
            </th>
        </tr>
        <tr style="background-color: #F8F071 ">
            <th>NAHARKATIA_REV</th>
            <th>DESKTOP-C
            </th>
            <th>{naharkatia_rev_circle_ip3}
            </th>
            <th style="background-color:#27AE60;">{naharkatia_rev_circle_status_ip3}
            </th>
        </tr>
        <tr style="background-color: #F8F071 ">
            <th>NAHARKATIA_REV</th>
            <th>DESKTOP-D
            </th>
            <th>{naharkatia_rev_circle_ip4}
            </th>
            <th style="background-color:#27AE60;">{naharkatia_rev_circle_status_ip4}
            </th>
        </tr>
        <tr style="background-color: #F8F071 ">
            <th>NAHARKATIA_REV</th>
            <th>DESKTOP-E
            </th>
            <th>{naharkatia_rev_circle_ip5}
            </th>
            <th style="background-color:#27AE60;">{naharkatia_rev_circle_status_ip5}
            </th>
        </tr>
        
        <!--TENGAKHAT-->
        <tr style="background-color: #F8F071 ">
            <th>TENGAKHAT</th>
            <th>DESKTOP-A
            </th>
            <th>{tengakhat_circle_ip1}
            </th>
            <th style="background-color:#27AE60;">{tengakhat_circle_status_ip1}
            </th>
        </tr>
        <tr style="background-color: #F8F071 ">
            <th>TENGAKHAT</th>
            <th>DESKTOP-B
            </th>
            <th>{tengakhat_circle_ip2}
            </th>
            <th style="background-color:#27AE60;">{tengakhat_circle_status_ip2}
            </th>
        </tr>
        <tr style="background-color: #F8F071 ">
            <th>TENGAKHAT</th>
            <th>DESKTOP-C
            </th>
            <th>{tengakhat_circle_ip3}
            </th>
            <th style="background-color:#27AE60;">{tengakhat_circle_status_ip3}
            </th>
        </tr>
        <tr style="background-color: #F8F071 ">
            <th>TENGAKHAT</th>
            <th>DESKTOP-D
            </th>
            <th>{tengakhat_circle_ip4}
            </th>
            <th style="background-color:#27AE60;">{tengakhat_circle_status_ip4}
            </th>
        </tr>
        <tr style="background-color: #F8F071 ">
            <th>TENGAKHAT</th>
            <th>DESKTOP-E
            </th>
            <th>{tengakhat_circle_ip5}
            </th>
            <th style="background-color:#27AE60;">{tengakhat_circle_status_ip5}
            </th>
        </tr>
        
        <!--TENGAKHAT_CO-->
        <tr style="background-color: #F8F071 ">
            <th>TENGAKHAT_CO</th>
            <th>DESKTOP-A
            </th>
            <th>{tengakhat_co_circle_ip1}
            </th>
            <th style="background-color:#27AE60;">{tengakhat_co_circle_status_ip1}
            </th>
        </tr>
        <tr style="background-color: #F8F071 ">
            <th>TENGAKHAT_CO</th>
            <th>DESKTOP-B
            </th>
            <th>{tengakhat_co_circle_ip2}
            </th>
            <th style="background-color:#27AE60;">{tengakhat_co_circle_status_ip2}
            </th>
        </tr>
        <tr style="background-color: #F8F071 ">
            <th>TENGAKHAT_CO</th>
            <th>DESKTOP-C
            </th>
            <th>{tengakhat_co_circle_ip3}
            </th>
            <th style="background-color:#27AE60;">{tengakhat_co_circle_status_ip3}
            </th>
        </tr>
        <tr style="background-color: #F8F071 ">
            <th>TENGAKHAT_CO</th>
            <th>DESKTOP-D
            </th>
            <th>{tengakhat_co_circle_ip4}
            </th>
            <th style="background-color:#27AE60;">{tengakhat_co_circle_status_ip4}
            </th>
        </tr>
        <tr style="background-color: #F8F071 ">
            <th>TENGAKHAT_CO</th>
            <th>DESKTOP-E
            </th>
            <th>{tengakhat_co_circle_ip5}
            </th>
            <th style="background-color:#27AE60;">{tengakhat_co_circle_status_ip5}
            </th>
        </tr>
        
        <!--TINGKHONG_REV-->
        <tr style="background-color: #F8F071 ">
            <th>TINGKHONG_REV</th>
            <th>DESKTOP-A
            </th>
            <th>{tingkhong_rev_circle_ip1}
            </th>
            <th style="background-color:#27AE60;">{tingkhong_rev_circle_status_ip1}
            </th>
        </tr>
        <tr style="background-color: #F8F071 ">
            <th>TINGKHONG_REV</th>
            <th>DESKTOP-B
            </th>
            <th>{tingkhong_rev_circle_ip2}
            </th>
            <th style="background-color:#27AE60;">{tingkhong_rev_circle_status_ip2}
            </th>
        </tr>
        <tr style="background-color: #F8F071 ">
            <th>TINGKHONG_REV</th>
            <th>DESKTOP-C
            </th>
            <th>{tingkhong_rev_circle_ip3}
            </th>
            <th style="background-color:#27AE60;">{tingkhong_rev_circle_status_ip3}
            </th>
        </tr>
        <tr style="background-color: #F8F071 ">
            <th>TINGKHONG_REV</th>
            <th>DESKTOP-D
            </th>
            <th>{tingkhong_rev_circle_ip4}
            </th>
            <th style="background-color:#27AE60;">{tingkhong_rev_circle_status_ip4}
            </th>
        </tr>
        <tr style="background-color: #F8F071 ">
            <th>TINGKHONG_REV</th>
            <th>DESKTOP-E
            </th>
            <th>{tingkhong_rev_circle_ip5}
            </th>
            <th style="background-color:#27AE60;">{tingkhong_rev_circle_status_ip5}
            </th>
        </tr>
        
    </table>
</div>
</body>
</html>
    '''


        


@app.route('/naharkatia_rev1', methods=['GET', 'POST'])
def naharkatia_rev1():

    return render_template('naharkatia_rev_machine.html')

#database

    #ip_checks1____importent
@app.route('/chabua_machine_check', methods=['GET', 'POST'])
def chabua_machine1_check():
   firebaseConfig = {
     'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
    'authDomain': "experiment-663c2.firebaseapp.com",
    'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
    'projectId': "experiment-663c2",
    'storageBucket': "experiment-663c2.appspot.com",
    'messagingSenderId': "378598338807",
    'appId': "1:378598338807:web:114229685379655a45a3f2",
    'measurementId': "G-E8WX073DSD"}


   firebase = pyrebase.initialize_app(firebaseConfig)

   db = firebase.database()
   ip=db.child("circle").child("chabua").child("machine1").child("id1").get()
   new_ip=(ip.val())
   ip_list=new_ip
   
   for ip in ip_list:
       response = os.popen(f"ping {ip} -n 4").read()
       if "Received = 4" in response:
           data={'ip':'up'}
           db.child("status").child("chabua").child("machine1").child("id1").set(data)
           db.child("status").child("chabua").child("machine1").child("id1").update({'ip': data})
           return render_template('chabua_machine1_check.html', ip1=ip)
       else:
            data={'ip':'Down'}
            db.child("status").child("chabua").child("machine1").child("id1").set(data)
            db.child("status").child("chabua").child("machine1").child("id1").update({'ip': data})
            return render_template('chabua_machine1_check1.html', ip1=ip)

#chabua_machine1_check()
#check2
@app.route('/chabua_machine_check', methods=['GET', 'POST'])
def chabua_machine2_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("chabua").child("machine2").child("id2").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
           data={'ip':'up'}
           db.child("status").child("chabua").child("machine2").child("id2").set(data)
           db.child("status").child("chabua").child("machine2").child("id2").update({'ip': data})
           return render_template('chabua_machine2_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("chabua").child("machine2").child("id2").set(data)
            db.child("status").child("chabua").child("machine2").child("id2").update({'ip': data})
            return render_template('chabua_machine2_check1.html', ip1=ip)

#chabua_machine2_check()
#check3
@app.route('/chabua_machine_check', methods=['GET', 'POST'])
def chabua_machine3_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("chabua").child("machine3").child("id3").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("chabua").child("machine3").child("id3").set(data)
            db.child("status").child("chabua").child("machine3").child("id3").update({'ip': data})
            return render_template('chabua_machine3_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("chabua").child("machine3").child("id3").set(data)
            db.child("status").child("chabua").child("machine3").child("id3").update({'ip': data})
            return render_template('chabua_machine3_check1.html', ip1=ip)

#chabua_machine3_check()

#check4
@app.route('/chabua_machine_check', methods=['GET', 'POST'])
def chabua_machine4_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("chabua").child("machine4").child("id4").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("chabua").child("machine4").child("id4").set(data)
            db.child("status").child("chabua").child("machine4").child("id4").update({'ip': data})
            return render_template('chabua_machine4_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("chabua").child("machine4").child("id4").set(data)
            db.child("status").child("chabua").child("machine4").child("id4").update({'ip': data})
            return render_template('chabua_machine4_check1.html',ip1=ip)

#chabua_machine4_check()

#check5

@app.route('/chabua_machine_check', methods=['GET', 'POST'])
def chabua_machine5_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("chabua").child("machine5").child("id5").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("chabua").child("machine5").child("id5").set(data)
            db.child("status").child("chabua").child("machine5").child("id5").update({'ip': data})
            return render_template('chabua_machine5_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("chabua").child("machine5").child("id5").set(data)
            db.child("status").child("chabua").child("machine5").child("id5").update({'ip': data})
            return render_template('chabua_machine5_check1.html', ip1=ip)

#chabua_machine5_check()

#add new machine
@app.route('/add_new_machine', methods=['GET'])
def add_new_machine():
    return '''
      <!DOCTYPE HTML>
      <html>
      <body>
      <label>machine_name</label>
      <input type="text"  name="machine_name">
      <label>ip_address</label>
      <input type="text"  name="machine_name">
      </body>
      </html>
    '''


#naharkatia_machines

#ip_checks1
@app.route('/naharkatia_machine1_check', methods=['GET', 'POST'])
def naharkatia_machine1_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("naharkatia").child("machine1").child("id1").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("naharkatia").child("machine1").child("id1").set(data)
            db.child("status").child("naharkatia").child("machine1").child("id1").update({'ip': data})
            return render_template('naharkatia_machine1_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("naharkatia").child("machine1").child("id1").set(data)
            db.child("status").child("naharkatia").child("machine1").child("id1").update({'ip': data})
            return render_template('naharkatia_machine1_check1.html', ip1=ip)

#naharkatia_machine1_check()
#check2
@app.route('/naharkatia_machine2_check', methods=['GET', 'POST'])
def naharkatia_machine2_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("naharkatia").child("machine1").child("id1").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("naharkatia").child("machine1").child("id1").set(data)
            db.child("status").child("naharkatia").child("machine1").child("id1").update({'ip': data})
            return render_template('naharkatia_machine2_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("naharkatia").child("machine1").child("id1").set(data)
            db.child("status").child("naharkatia").child("machine1").child("id1").update({'ip': data})
            return render_template('naharkatia_machine2_check1.html', ip1=ip)

#naharkatia_machine2_check()
#check3
@app.route('/naharkatia_machine3_check', methods=['GET', 'POST'])
def naharkatia_machine3_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("naharkatia").child("machine3").child("id3").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("naharkatia").child("machine3").child("id3").set(data)
            db.child("status").child("naharkatia").child("machine3").child("id3").update({'ip': data})
            return render_template('naharkatia_machine3_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("naharkatia").child("machine3").child("id3").set(data)
            db.child("status").child("naharkatia").child("machine3").child("id3").update({'ip': data})
            return render_template('naharkatia_machine3_check1.html', ip1=ip)

#naharkatia_machine3_check()

#check4
@app.route('/naharkatia_machine4_check', methods=['GET', 'POST'])
def naharkatia_machine4_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("naharkatia").child("machine4").child("id4").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("naharkatia").child("machine4").child("id4").set(data)
            db.child("status").child("naharkatia").child("machine4").child("id4").update({'ip': data})
            return render_template('naharkatia_machine4_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("naharkatia").child("machine4").child("id4").set(data)
            db.child("status").child("naharkatia").child("machine4").child("id4").update({'ip': data})
            return render_template('naharkatia_machine4_check1.html', ip1=ip)

#naharkatia_machine4_check()

#check5

@app.route('/naharkatia_machine5_check', methods=['GET', 'POST'])
def naharkatia_machine5_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("naharkatia").child("machine5").child("id5").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("naharkatia").child("machine5").child("id5").set(data)
            db.child("status").child("naharkatia").child("machine5").child("id5").update({'ip': data})
            return render_template('naharkatia_machine5_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("naharkatia").child("machine5").child("id5").set(data)
            db.child("status").child("naharkatia").child("machine5").child("id5").update({'ip': data})
            return render_template('naharkatia_machine5_check.html', ip1=ip)

#naharkatia_machine5_check()


#ip_checks1
@app.route('/dibrugarh_east_machine1_check', methods=['GET', 'POST'])
def dibrugarh_east_machine1_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("dibrugarh_east").child("machine1").child("id1").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("dibrugarh_east").child("machine1").child("id1").set(data)
            db.child("status").child("dibrugarh_east").child("machine1").child("id1").update({'ip': data})
            return render_template('dibrugarh_east_machine1_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("dibrugarh_east").child("machine1").child("id1").set(data)
            db.child("status").child("dibrugarh_east").child("machine1").child("id1").update({'ip': data})
            return render_template('dibrugarh_east_machine1_check1.html', ip1=ip)

#dibrugarh_east_machine1_check()
#check2
@app.route('/dibrugarh_east_machine2_check', methods=['GET', 'POST'])
def dibrugarh_east_machine2_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("dibrugarh_east").child("machine2").child("id2").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("dibrugarh_east").child("machine2").child("id2").set(data)
            db.child("status").child("dibrugarh_east").child("machine2").child("id2").update({'ip': data})
            return render_template('dibrugarh_east_machine2_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("dibrugarh_east").child("machine2").child("id2").set(data)
            db.child("status").child("dibrugarh_east").child("machine2").child("id2").update({'ip': data})
            return render_template('dibrugarh_east_machine2_check1.html', ip1=ip)

#dibrugarh_east_machine2_check()
#check3
@app.route('/dibrugarh_east_machine3_check', methods=['GET', 'POST'])
def dibrugarh_east_machine3_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("dibrugarh_east").child("machine3").child("id3").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("dibrugarh_east").child("machine3").child("id3").set(data)
            db.child("status").child("dibrugarh_east").child("machine3").child("id3").update({'ip': data})
            return render_template('dibrugarh_east_machine3_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("dibrugarh_east").child("machine3").child("id3").set(data)
            db.child("status").child("dibrugarh_east").child("machine3").child("id3").update({'ip': data})
            return render_template('dibrugarh_east_machine3_check1.html', ip1=ip)

#dibrugarh_east_machine3_check()

#check4
@app.route('/dibrugarh_east_machine4_check', methods=['GET', 'POST'])
def dibrugarh_east_machine4_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("dibrugarh_east").child("machine4").child("id4").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("dibrugarh_east").child("machine4").child("id4").set(data)
            db.child("status").child("dibrugarh_east").child("machine4").child("id4").update({'ip': data})
            return render_template('dibrugarh_east_machine4_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("dibrugarh_east").child("machine4").child("id4").set(data)
            db.child("status").child("dibrugarh_east").child("machine4").child("id4").update({'ip': data})
            return render_template('dibrugarh_east_machine4_check1.html', ip1=ip)

#dibrugarh_east_machine4_check()

#check5

@app.route('/dibrugarh_east_machine5_check', methods=['GET', 'POST'])
def dibrugarh_east_machine5_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("dibrugarh_east").child("machine5").child("id5").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("dibrugarh_east").child("machine5").child("id5").set(data)
            db.child("status").child("dibrugarh_east").child("machine5").child("id5").update({'ip': data})
            return render_template('dibrugarh_east_machine5_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("dibrugarh_east").child("machine5").child("id5").set(data)
            db.child("status").child("dibrugarh_east").child("machine5").child("id5").update({'ip': data})
            return render_template('dibrugarh_east_machine5_check1.html', ip1=ip)

#dibrugarh_east_machine5_check()
#dibrugarh west

#ip_checks1
@app.route('/dibrugarh_west_machine1_check', methods=['GET', 'POST'])
def dibrugarh_west_machine1_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("dibrugarh_west").child("machine1").child("id1").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("dibrugarh_west").child("machine1").child("id1").set(data)
            db.child("status").child("dibrugarh_west").child("machine1").child("id1").update({'ip': data})
            return render_template('dibrugarh_west_machine1_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("dibrugarh_west").child("machine1").child("id1").set(data)
            db.child("status").child("dibrugarh_west").child("machine1").child("id1").update({'ip': data})
            return render_template('dibrugarh_west_machine1_check1.html', ip1=ip)

#dibrugarh_west_machine1_check()
#check2
@app.route('/dibrugarh_west_machine2_check', methods=['GET', 'POST'])
def dibrugarh_west_machine2_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("dibrugarh_west").child("machine2").child("id2").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("dibrugarh_west").child("machine2").child("id2").set(data)
            db.child("status").child("dibrugarh_west").child("machine2").child("id2").update({'ip': data})
            return render_template('dibrugarh_west_machine2_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("dibrugarh_west").child("machine2").child("id2").set(data)
            db.child("status").child("dibrugarh_west").child("machine2").child("id2").update({'ip': data})
            return render_template('dibrugarh_west_machine2_check1.html', ip1=ip)

#dibrugarh_west_machine2_check()
#check3
@app.route('/dibrugarh_west_machine3_check', methods=['GET', 'POST'])
def dibrugarh_west_machine3_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("dibrugarh_west").child("machine3").child("id3").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("dibrugarh_west").child("machine3").child("id3").set(data)
            db.child("status").child("dibrugarh_west").child("machine3").child("id3").update({'ip': data})
            return render_template('dibrugarh_west_machine3_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("dibrugarh_west").child("machine3").child("id3").set(data)
            db.child("status").child("dibrugarh_west").child("machine3").child("id3").update({'ip': data})
            return render_template('dibrugarh_west_machine3_check1.html', ip1=ip)

#dibrugarh_east_machine3_check()

#check4
@app.route('/dibrugarh_west_machine4_check', methods=['GET', 'POST'])
def dibrugarh_west_machine4_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("dibrugarh_west").child("machine4").child("id4").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("dibrugarh_west").child("machine4").child("id4").set(data)
            db.child("status").child("dibrugarh_west").child("machine4").child("id4").update({'ip': data})
            return render_template('dibrugarh_west_machine4_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("dibrugarh_west").child("machine4").child("id4").set(data)
            db.child("status").child("dibrugarh_west").child("machine4").child("id4").update({'ip': data})
            return render_template('dibrugarh_west_machine4_check1.html', ip1=ip)

#dibrugarh_east_machine4_check()

#check5

@app.route('/dibrugarh_west_machine5_check', methods=['GET', 'POST'])
def dibrugarh_west_machine5_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("dibrugarh_west").child("machine5").child("id5").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("dibrugarh_west").child("machine2").child("id2").set(data)
            db.child("status").child("dibrugarh_west").child("machine2").child("id2").update({'ip': data})
            return render_template('dibrugarh_west_machine5_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("dibrugarh_west").child("machine5").child("id5").set(data)
            db.child("status").child("dibrugarh_west").child("machine5").child("id5").update({'ip': data})
            return render_template('dibrugarh_west_machine5_check1.html', ip1=ip)

#dibrugarh_east_machine5_check()

#tingkhong_rev
#ip_checks1
@app.route('/tingkhong_rev_machine1_check', methods=['GET', 'POST'])
def tingkhong_rev_machine1_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("tingkhong_rev").child("machine1").child("id1").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("tingkhong_rev").child("machine1").child("id1").set(data)
            db.child("status").child("tingkhong_rev").child("machine1").child("id1").update({'ip': data})
            return render_template('tingkhong_rev_machine1_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("tingkhong_rev").child("machine1").child("id1").set(data)
            db.child("status").child("tingkhong_rev").child("machine1").child("id1").update({'ip': data})
            return render_template('tingkhong_rev_machine1_check1.html', ip1=ip)

#tingkhong_rev_machine1_check()
#check2
@app.route('/tingkhong_rev_machine2_check', methods=['GET', 'POST'])
def tingkhong_rev_machine2_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("tingkhong_rev").child("machine2").child("id2").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("tingkhong_rev").child("machine2").child("id2").set(data)
            db.child("status").child("tingkhong_rev").child("machine2").child("id2").update({'ip': data})
            return render_template('tingkhong_rev_machine2_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("tingkhong_rev").child("machine2").child("id2").set(data)
            db.child("status").child("tingkhong_rev").child("machine2").child("id2").update({'ip': data})
            return render_template('tingkhong_rev_machine3_check1.html', ip1=ip)

#tingkhong_rev_machine2_check()
#check3
@app.route('/tingkhong_rev_machine3_check', methods=['GET', 'POST'])
def tingkhong_rev_machine3_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("tingkhong_rev").child("machine3").child("id3").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("tingkhong_rev").child("machine3").child("id3").set(data)
            db.child("status").child("tingkhong_rev").child("machine3").child("id3").update({'ip': data})
            return render_template('tingkhong_rev_machine3_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("tingkhong_rev").child("machine3").child("id3").set(data)
            db.child("status").child("tingkhong_rev").child("machine3").child("id3").update({'ip': data})
            return render_template('tingkhong_rev_machine3_check1.html', ip1=ip)

#tingkhong_rev_machine3_check()

#check4
@app.route('/tingkhong_rev_machine4_check', methods=['GET', 'POST'])
def tingkhong_rev_machine4_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("tingkhong_rev").child("machine4").child("id4").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("tingkhong_rev").child("machine4").child("id4").set(data)
            db.child("status").child("tingkhong_rev").child("machine4").child("id4").update({'ip': data})
            return render_template('tingkhong_rev_machine4_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("tingkhong_rev").child("machine4").child("id4").set(data)
            db.child("status").child("tingkhong_rev").child("machine4").child("id4").update({'ip': data})
            return render_template('tingkhong_rev_machine4_check1.html', ip1=ip)

#tingkhong_rev_machine4_check()

#check5

@app.route('/tingkhong_rev_machine5_check', methods=['GET', 'POST'])
def tingkhong_rev_machine5_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("tingkhong_rev").child("machine5").child("id5").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("tingkhong_rev").child("machine5").child("id5").set(data)
            db.child("status").child("tingkhong_rev").child("machine5").child("id5").update({'ip': data})
            return render_template('tingkhong_rev_machine5_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("tingkhong_rev").child("machine5").child("id5").set(data)
            db.child("status").child("tingkhong_rev").child("machine5").child("id5").update({'ip': data})
            return render_template('tingkhong_rev_machine5_check1.html', ip1=ip)

#tingkhong_rev_machine5_check()
#moran

#ip_checks1
@app.route('/moran_machine1_check', methods=['GET', 'POST'])
def moran_machine1_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("moran").child("machine1").child("id1").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("moran").child("machine1").child("id1").set(data)
            db.child("status").child("moran").child("machine1").child("id1").update({'ip': data})
            return render_template('moran_machine1_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("moran").child("machine1").child("id1").set(data)
            db.child("status").child("moran").child("machine1").child("id1").update({'ip': data})
            return render_template('moran_machine1_check1.html', ip1=ip)

#moran_machine1_check()
#check2
@app.route('/moran_machine2_check', methods=['GET', 'POST'])
def moran_machine2_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("moran").child("machine2").child("id2").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("moran").child("machine2").child("id2").set(data)
            db.child("status").child("moran").child("machine2").child("id2").update({'ip': data})
            return render_template('moran_machine2_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("moran").child("machine2").child("id2").set(data)
            db.child("status").child("moran").child("machine2").child("id2").update({'ip': data})
            return render_template('moran_machine2_check1.html', ip1=ip)

#moran_machine2_check()
#check3
@app.route('/moran_machine3_check', methods=['GET', 'POST'])
def moran_machine3_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("moran").child("machine3").child("id3").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("moran").child("machine3").child("id3").set(data)
            db.child("status").child("moran").child("machine3").child("id3").update({'ip': data})
            return render_template('moran_machine3_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("moran").child("machine3").child("id3").set(data)
            db.child("status").child("moran").child("machine3").child("id3").update({'ip': data})
            return render_template('moran_machine3_check1.html', ip1=ip)

#moran_machine3_check()

#check4
@app.route('/moran_machine4_check', methods=['GET', 'POST'])
def moran_machine4_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("moran").child("machine4").child("id4").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("moran").child("machine4").child("id4").set(data)
            db.child("status").child("moran").child("machine4").child("id4").update({'ip': data})
            return render_template('moran_machine4_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("moran").child("machine4").child("id4").set(data)
            db.child("status").child("moran").child("machine4").child("id4").update({'ip': data})
            return render_template('moran_machine4_check1.html', ip1=ip)

#moran_machine4_check()

#check5

@app.route('/moran_machine5_check', methods=['GET', 'POST'])
def moran_machine5_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("moran").child("machine5").child("id5").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("moran").child("machine5").child("id5").set(data)
            db.child("status").child("moran").child("machine5").child("id5").update({'ip': data})
            return render_template('moran_machine5_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("moran").child("machine5").child("id5").set(data)
            db.child("status").child("moran").child("machine5").child("id5").update({'ip': data})
            return render_template('moran_machine5_check1.html', ip1=ip)

#moran_machine5_check()
#tengakhat

#ip_checks1
@app.route('/tengakhat_machine1_check', methods=['GET', 'POST'])
def tengakhat_machine1_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("tengakhat").child("machine1").child("id1").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("tengakhat").child("machine1").child("id1").set(data)
            db.child("status").child("tengakhat").child("machine1").child("id1").update({'ip': data})
            return render_template('tengakhat_machine1_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("tengakhat").child("machine1").child("id1").set(data)
            db.child("status").child("tengakhat").child("machine1").child("id1").update({'ip': data})
            return render_template('tengakhat_machine1_check1.html', ip1=ip)

#tengakhat_machine1_check()
#check2
@app.route('/tengakhat_machine2_check', methods=['GET', 'POST'])
def tengakhat_machine2_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("tengakhat").child("machine2").child("id2").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("tengakhat").child("machine2").child("id2").set(data)
            db.child("status").child("tengakhat").child("machine2").child("id2").update({'ip': data})
            return render_template('tengakhat_machine2_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("tengakhat").child("machine2").child("id2").set(data)
            db.child("status").child("tengakhat").child("machine2").child("id2").update({'ip': data})
            return render_template('tengakhat_machine2_check1.html', ip1=ip)

#tengakhat_machine2_check()

#check3
@app.route('/tengakhat_machine3_check', methods=['GET', 'POST'])
def tengakhat_machine3_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("tengakhat").child("machine3").child("id3").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("tengakhat").child("machine3").child("id3").set(data)
            db.child("status").child("tengakhat").child("machine3").child("id3").update({'ip': data})
            return render_template('tengakhat_machine3_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("tengakhat").child("machine3").child("id3").set(data)
            db.child("status").child("tengakhat").child("machine3").child("id3").update({'ip': data})
            return render_template('tengakhat_machine3_check1.html', ip1=ip)

#tengakhat_machine3_check()

#check4

@app.route('/tengakhat_machine4_check', methods=['GET', 'POST'])
def tengakhat_machine4_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("tengakhat").child("machine4").child("id4").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("tengakhat").child("machine4").child("id4").set(data)
            db.child("status").child("tengakhat").child("machine4").child("id4").update({'ip': data})
            return render_template('tengakhat_machine4_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("tengakhat").child("machine4").child("id4").set(data)
            db.child("status").child("tengakhat").child("machine4").child("id4").update({'ip': data})
            return render_template('tengakhat_machine4_check1.html', ip1=ip)

#tengakhat_machine4_check()

#check5
@app.route('/tengakhat_machine5_check', methods=['GET', 'POST'])
def tengakhat_machine5_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("tengakhat").child("machine5").child("id5").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("tengakhat").child("machine5").child("id5").set(data)
            db.child("status").child("tengakhat").child("machine5").child("id5").update({'ip': data})
            return render_template('tengakhat_machine5_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("tengakhat").child("machine5").child("id5").set(data)
            db.child("status").child("tengakhat").child("machine5").child("id5").update({'ip': data})
            return render_template('tengakhat_machine5_check1.html', ip1=ip)

#tengakhat_machine5_check()


#dibrugarh_west_rev_circleA

#ip_checks1
@app.route('/dibrugarh_west_rev_circleA_machine1_check', methods=['GET', 'POST'])
def dibrugarh_west_rev_circleA_machine1_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("dibrugarh_west_rev_circle").child("machine1").child("id1").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("dibrugarh_west_rev_circle").child("machine1").child("id1").set(data)
            db.child("status").child("dibrugarh_west_rev_circle").child("machine1").child("id1").update({'ip': data})
            return render_template('dibrugarh_west_rev_circle_machine1_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("dibrugarh_west_rev_circle").child("machine1").child("id1").set(data)
            db.child("status").child("dibrugarh_west_rev_circle").child("machine1").child("id1").update({'ip': data})
            return render_template('dibrugarh_west_rev_circle_machine1_check1.html', ip1=ip)

#dibrugarh_west_rev_circleA_machine1_check()
#check2
@app.route('/dibrugarh_west_rev_circleA_machine2_check', methods=['GET', 'POST'])
def dibrugarh_west_rev_circleA_machine2_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("dibrugarh_west_rev_circle").child("machine2").child("id2").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("dibrugarh_west_rev_circle").child("machine2").child("id2").set(data)
            db.child("status").child("dibrugarh_west_rev_circle").child("machine2").child("id2").update({'ip': data})
            return render_template('dibrugarh_west_rev_circle_machine2_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("dibrugarh_west_rev_circle").child("machine2").child("id2").set(data)
            db.child("status").child("dibrugarh_west_rev_circle").child("machine2").child("id2").update({'ip': data})
            return render_template('dibrugarh_west_rev_circle_machine2_check1.html', ip1=ip)

#dibrugarh_west_rev_circleA_machine2_check()
#check3
@app.route('/dibrugarh_west_rev_circleA_machine3_check', methods=['GET', 'POST'])
def dibrugarh_west_rev_circleA_machine3_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("dibrugarh_west_rev_circle").child("machine3").child("id3").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("dibrugarh_west_rev_circle").child("machine3").child("id3").set(data)
            db.child("status").child("dibrugarh_west_rev_circle").child("machine3").child("id3").update({'ip': data})
            return render_template('dibrugarh_west_rev_circle_machine3_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("dibrugarh_west_rev_circle").child("machine3").child("id3").set(data)
            db.child("status").child("dibrugarh_west_rev_circle").child("machine3").child("id3").update({'ip': data})
            return render_template('dibrugarh_west_rev_circle_machine3_check1.html', ip1=ip)

#dibrugarh_west_rev_circleA_machine3_check()

#check4
@app.route('/dibrugarh_west_rev_circleA_machine4_check', methods=['GET', 'POST'])
def dibrugarh_west_rev_circleA_machine4_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("dibrugarh_west_rev_circle").child("machine4").child("id4").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("dibrugarh_west_rev_circle").child("machine4").child("id4").set(data)
            db.child("status").child("dibrugarh_west_rev_circle").child("machine4").child("id4").update({'ip': data})
            return render_template('dibrugarh_west_rev_circle_machine4_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("dibrugarh_west_rev_circle").child("machine4").child("id4").set(data)
            db.child("status").child("dibrugarh_west_rev_circle").child("machine4").child("id4").update({'ip': data})
            return render_template('dibrugarh_west_rev_circle_machine4_check1.html', ip1=ip)

#dibrugarh_west_rev_circleA_machine4_check()

#check5

@app.route('/dibrugarh_west_rev_circleA_machine5_check', methods=['GET', 'POST'])
def dibrugarh_west_rev_circleA_machine5_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("dibrugarh_west_rev_circle").child("machine5").child("id5").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("dibrugarh_west_rev_circle").child("machine5").child("id5").set(data)
            db.child("status").child("dibrugarh_west_rev_circle").child("machine5").child("id5").update({'ip': data})
            return render_template('dibrugarh_west_rev_circle_machine5_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("dibrugarh_west_rev_circle").child("machine5").child("id5").set(data)
            db.child("status").child("dibrugarh_west_rev_circle").child("machine5").child("id5").update({'ip': data})
            return render_template('dibrugarh_west_rev_circle_machine5_check1.html', ip1=ip)

#dibrugarh_west_rev_circleA_machine5_check()
#tengakhat_co
#ip_checks1
@app.route('/tengakhat_co_machine1_check', methods=['GET', 'POST'])
def tengakhat_co_machine1_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("tengakhat_co").child("machine1").child("id1").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("tengakhat_co").child("machine1").child("id1").set(data)
            db.child("status").child("tengakhat_co").child("machine1").child("id1").update({'ip': data})
            return render_template('tengakhat_co_machine1_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("tengakhat_co").child("machine1").child("id1").set(data)
            db.child("status").child("tengakhat_co").child("machine1").child("id1").update({'ip': data})
            return render_template('tengakhat_co_machine1_check1.html', ip1=ip)

#tengakhat_co_machine1_check()
#check2
@app.route('/tengakhat_co_machine2_check', methods=['GET', 'POST'])
def tengakhat_co_machine2_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("tengakhat_co").child("machine1").child("id1").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("tengakhat_co").child("machine2").child("id2").set(data)
            db.child("status").child("tengakhat_co").child("machine2").child("id2").update({'ip': data})
            return  render_template('tengakhat_co_machine2_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("tengakhat_co").child("machine2").child("id2").set(data)
            db.child("status").child("tengakhat_co").child("machine2").child("id2").update({'ip': data})
            return  render_template('tengakhat_co_machine2_check1.html', ip1=ip)

#tengakhat_co_machine2_check()
#check3
@app.route('/tengakhat_co_machine3_check', methods=['GET', 'POST'])
def tengakhat_co_machine3_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("tengakhat_co").child("machine3").child("id3").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("tengakhat_co").child("machine3").child("id3").set(data)
            db.child("status").child("tengakhat_co").child("machine3").child("id3").update({'ip': data})
            return  render_template('tengakhat_co_machine3_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("tengakhat_co").child("machine3").child("id3").set(data)
            db.child("status").child("tengakhat_co").child("machine3").child("id3").update({'ip': data})
            return render_template('tengakhat_co_machine3_check1.html', ip1=ip)

#tengakhat_co_machine3_check()

#check4
@app.route('/tengakhat_co_machine4_check', methods=['GET', 'POST'])
def tengakhat_co_machine4_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("tengakhat_co").child("machine4").child("id4").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("tengakhat_co").child("machine4").child("id4").set(data)
            db.child("status").child("tengakhat_co").child("machine4").child("id4").update({'ip': data})
            return render_template('tengakhat_co_machine4_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("tengakhat_co").child("machine4").child("id4").set(data)
            db.child("status").child("tengakhat_co").child("machine4").child("id4").update({'ip': data})
            return render_template('tengakhat_co_machine4_check1.html', ip1=ip)

#tengakhat_co_machine4_check()

#check5

@app.route('/tengakhat_co_machine5_check', methods=['GET', 'POST'])
def tengakhat_co_machine5_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("tengakhat_co").child("machine5").child("id5").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("tengakhat_co").child("machine5").child("id5").set(data)
            db.child("status").child("tengakhat_co").child("machine5").child("id5").update({'ip': data})
            return render_template('tengakhat_co_machine5_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("tengakhat_co").child("machine5").child("id5").set(data)
            db.child("status").child("tengakhat_co").child("machine5").child("id5").update({'ip': data})
            return render_template('tengakhat_co_machine5_check1.html', ip1=ip)

#tengakhat_co_machine5_check()

#naharkatia_rev

#ip_checks1
@app.route('/naharkatia_rev_machine1_check', methods=['GET', 'POST'])
def naharkatia_rev_machine1_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("naharkatia_rev").child("machine1").child("id1").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("naharkatia_rev").child("machine1").child("id1").set(data)
            db.child("status").child("naharkatia_rev").child("machine1").child("id1").update({'ip': data})
            return render_template('naharkatia_rev_machine1_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("naharkatia_rev").child("machine1").child("id1").set(data)
            db.child("status").child("naharkatia_rev").child("machine1").child("id1").update({'ip': data})
            return render_template('naharkatia_rev_machine1_check1.html', ip1=ip)

#naharkatia_rev_machine1_check()
#check2
@app.route('/naharkatia_rev_machine2_check', methods=['GET', 'POST'])
def naharkatia_rev_machine2_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("naharkatia_rev").child("machine2").child("id2").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("naharkatia_rev").child("machine2").child("id2").set(data)
            db.child("status").child("naharkatia_rev").child("machine2").child("id2").update({'ip': data})
            return render_template('naharkatia_rev_machine2_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("naharkatia_rev").child("machine2").child("id2").set(data)
            db.child("status").child("naharkatia_rev").child("machine2").child("id2").update({'ip': data})
            return render_template('naharkatia_rev_machine2_check1.html', ip1=ip)

#naharkatia_rev_machine2_check()
#check3
@app.route('/naharkatia_rev_machine3_check', methods=['GET', 'POST'])
def naharkatia_rev_machine3_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("naharkatia_rev").child("machine3").child("id3").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("naharkatia_rev").child("machine3").child("id3").set(data)
            db.child("status").child("naharkatia_rev").child("machine3").child("id3").update({'ip': data})
            return render_template('naharkatia_rev_machine3_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("naharkatia_rev").child("machine3").child("id3").set(data)
            db.child("status").child("naharkatia_rev").child("machine3").child("id3").update({'ip': data})
            return render_template('naharkatia_rev_machine3_check1.html', ip1=ip)

#naharkatia_rev_machine3_check()

#check4
@app.route('/naharkatia_rev_machine4_check', methods=['GET', 'POST'])
def naharkatia_rev_machine4_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("naharkatia_rev").child("machine4").child("id4").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("naharkatia_rev").child("machine4").child("id4").set(data)
            db.child("status").child("naharkatia_rev").child("machine4").child("id4").update({'ip': data})
            return render_template('naharkatia_rev_machine4_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("naharkatia_rev").child("machine4").child("id4").set(data)
            db.child("status").child("naharkatia_rev").child("machine4").child("id4").update({'ip': data})
            return render_template('naharkatia_rev_machine4_check1.html', ip1=ip)

#naharkatia_rev_machine4_check()

#check5

@app.route('/naharkatia_rev_machine5_check', methods=['GET', 'POST'])
def naharkatia_rev_machine5_check():
    firebaseConfig = {
        'apiKey': "AIzaSyBSKAKeAgurdNQsZouQadFsHYBhf4v8lW4",
        'authDomain': "experiment-663c2.firebaseapp.com",
        'databaseURL':"https://experiment-663c2-default-rtdb.firebaseio.com/",
        'projectId': "experiment-663c2",
        'storageBucket': "experiment-663c2.appspot.com",
        'messagingSenderId': "378598338807",
        'appId': "1:378598338807:web:114229685379655a45a3f2",
        'measurementId': "G-E8WX073DSD"}


    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    ip=db.child("circle").child("naharkatia_rev").child("machine5").child("id5").get()
    new_ip=(ip.val())
    ip_list=new_ip

    for ip in ip_list:
        response = os.popen(f"ping {ip} -n 4").read()
        if "Received = 4" in response:
            data={'ip':'up'}
            db.child("status").child("naharkatia_rev").child("machine5").child("id5").set(data)
            db.child("status").child("naharkatia_rev").child("machine5").child("id5").update({'ip': data})
            return render_template('naharkatia_rev_machine5_check.html', ip1=ip)
        else:
            data={'ip':'Down'}
            db.child("status").child("naharkatia_rev").child("machine5").child("id5").set(data)
            db.child("status").child("naharkatia_rev").child("machine5").child("id5").update({'ip': data})
            return render_template('naharkatia_rev_machine5_check1.html', ip1=ip)

#naharkatia_rev_machine5_check()

@app.route('/add_new_machines', methods=['GET', 'POST'])
def add_new_machines():
    return render_template('add_new_machine.html')


@app.route('/login')
def login():
    return render_template('login.html')
    
if __name__ == "__main__":
    app.run(debug=True)





 

