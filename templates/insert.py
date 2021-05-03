import pyrebase
import os
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

        else:
            data={'ip':'Down'}
            db.child("status").child("chabua").child("machine1").child("id1").set(data)
            db.child("status").child("chabua").child("machine1").child("id1").update({'ip': data})


chabua_machine1_check()
#check2

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

        else:
            data={'ip':'Down'}
            db.child("status").child("chabua").child("machine2").child("id2").set(data)
            db.child("status").child("chabua").child("machine2").child("id2").update({'ip': data})


chabua_machine2_check()
#check3

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

        else:
            data={'ip':'Down'}
            db.child("status").child("chabua").child("machine3").child("id3").set(data)
            db.child("status").child("chabua").child("machine3").child("id3").update({'ip': data})


chabua_machine3_check()

#check4

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

        else:
            data={'ip':'Down'}
            db.child("status").child("chabua").child("machine4").child("id4").set(data)
            db.child("status").child("chabua").child("machine4").child("id4").update({'ip': data})


chabua_machine4_check()

#check5

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

        else:
            data={'ip':'Down'}
            db.child("status").child("chabua").child("machine5").child("id5").set(data)
            db.child("status").child("chabua").child("machine5").child("id5").update({'ip': data})


chabua_machine5_check()



#naharkatia_machines

#ip_checks1

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

        else:
            data={'ip':'Down'}
            db.child("status").child("naharkatia").child("machine1").child("id1").set(data)
            db.child("status").child("naharkatia").child("machine1").child("id1").update({'ip': data})


naharkatia_machine1_check()
#check2

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

        else:
            data={'ip':'Down'}
            db.child("status").child("naharkatia").child("machine1").child("id1").set(data)
            db.child("status").child("naharkatia").child("machine1").child("id1").update({'ip': data})


naharkatia_machine2_check()
#check3

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

        else:
            data={'ip':'Down'}
            db.child("status").child("naharkatia").child("machine3").child("id3").set(data)
            db.child("status").child("naharkatia").child("machine3").child("id3").update({'ip': data})


naharkatia_machine3_check()

#check4

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

        else:
            data={'ip':'Down'}
            db.child("status").child("naharkatia").child("machine4").child("id4").set(data)
            db.child("status").child("naharkatia").child("machine4").child("id4").update({'ip': data})


naharkatia_machine4_check()

#check5

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

        else:
            data={'ip':'Down'}
            db.child("status").child("naharkatia").child("machine5").child("id5").set(data)
            db.child("status").child("naharkatia").child("machine5").child("id5").update({'ip': data})


naharkatia_machine5_check()


#ip_checks1
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

        else:
            data={'ip':'Down'}
            db.child("status").child("dibrugarh_east").child("machine1").child("id1").set(data)
            db.child("status").child("dibrugarh_east").child("machine1").child("id1").update({'ip': data})


dibrugarh_east_machine1_check()
#check2
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

        else:
            data={'ip':'Down'}
            db.child("status").child("dibrugarh_east").child("machine2").child("id2").set(data)
            db.child("status").child("dibrugarh_east").child("machine2").child("id2").update({'ip': data})


dibrugarh_east_machine2_check()
#check3
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

        else:
            data={'ip':'Down'}
            db.child("status").child("dibrugarh_east").child("machine3").child("id3").set(data)
            db.child("status").child("dibrugarh_east").child("machine3").child("id3").update({'ip': data})


dibrugarh_east_machine3_check()

#check4
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

        else:
            data={'ip':'Down'}
            db.child("status").child("dibrugarh_east").child("machine4").child("id4").set(data)
            db.child("status").child("dibrugarh_east").child("machine4").child("id4").update({'ip': data})


dibrugarh_east_machine4_check()

#check5

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

        else:
            data={'ip':'Down'}
            db.child("status").child("dibrugarh_east").child("machine5").child("id5").set(data)
            db.child("status").child("dibrugarh_east").child("machine5").child("id5").update({'ip': data})


dibrugarh_east_machine5_check()
#dibrugarh west

#ip_checks1
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

        else:
            data={'ip':'Down'}
            db.child("status").child("dibrugarh_west").child("machine1").child("id1").set(data)
            db.child("status").child("dibrugarh_west").child("machine1").child("id1").update({'ip': data})


dibrugarh_west_machine1_check()
#check2

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

        else:
            data={'ip':'Down'}
            db.child("status").child("dibrugarh_west").child("machine2").child("id2").set(data)
            db.child("status").child("dibrugarh_west").child("machine2").child("id2").update({'ip': data})


dibrugarh_west_machine2_check()
#check3
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

        else:
            data={'ip':'Down'}
            db.child("status").child("dibrugarh_west").child("machine3").child("id3").set(data)
            db.child("status").child("dibrugarh_west").child("machine3").child("id3").update({'ip': data})


dibrugarh_east_machine3_check()

#check4

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

        else:
            data={'ip':'Down'}
            db.child("status").child("dibrugarh_west").child("machine4").child("id4").set(data)
            db.child("status").child("dibrugarh_west").child("machine4").child("id4").update({'ip': data})


dibrugarh_east_machine4_check()

#check5

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

        else:
            data={'ip':'Down'}
            db.child("status").child("dibrugarh_west").child("machine5").child("id5").set(data)
            db.child("status").child("dibrugarh_west").child("machine5").child("id5").update({'ip': data})


dibrugarh_east_machine5_check()

#tingkhong_rev
#ip_checks1
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

        else:
            data={'ip':'Down'}
            db.child("status").child("tingkhong_rev").child("machine1").child("id1").set(data)
            db.child("status").child("tingkhong_rev").child("machine1").child("id1").update({'ip': data})


tingkhong_rev_machine1_check()
#check2

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

        else:
            data={'ip':'Down'}
            db.child("status").child("tingkhong_rev").child("machine2").child("id2").set(data)
            db.child("status").child("tingkhong_rev").child("machine2").child("id2").update({'ip': data})


tingkhong_rev_machine2_check()
#check3
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

        else:
            data={'ip':'Down'}
            db.child("status").child("tingkhong_rev").child("machine3").child("id3").set(data)
            db.child("status").child("tingkhong_rev").child("machine3").child("id3").update({'ip': data})


tingkhong_rev_machine3_check()

#check4
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

        else:
            data={'ip':'Down'}
            db.child("status").child("tingkhong_rev").child("machine4").child("id4").set(data)
            db.child("status").child("tingkhong_rev").child("machine4").child("id4").update({'ip': data})


tingkhong_rev_machine4_check()

#check5

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

        else:
            data={'ip':'Down'}
            db.child("status").child("tingkhong_rev").child("machine5").child("id5").set(data)
            db.child("status").child("tingkhong_rev").child("machine5").child("id5").update({'ip': data})


tingkhong_rev_machine5_check()
#moran

#ip_checks1
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

        else:
            data={'ip':'Down'}
            db.child("status").child("moran").child("machine1").child("id1").set(data)
            db.child("status").child("moran").child("machine1").child("id1").update({'ip': data})


moran_machine1_check()
#check2
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

        else:
            data={'ip':'Down'}
            db.child("status").child("moran").child("machine2").child("id2").set(data)
            db.child("status").child("moran").child("machine2").child("id2").update({'ip': data})


moran_machine2_check()
#check3
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

        else:
            data={'ip':'Down'}
            db.child("status").child("moran").child("machine3").child("id3").set(data)
            db.child("status").child("moran").child("machine3").child("id3").update({'ip': data})


moran_machine3_check()

#check4
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

        else:
            data={'ip':'Down'}
            db.child("status").child("moran").child("machine4").child("id4").set(data)
            db.child("status").child("moran").child("machine4").child("id4").update({'ip': data})


moran_machine4_check()

#check5

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

        else:
            data={'ip':'Down'}
            db.child("status").child("moran").child("machine5").child("id5").set(data)
            db.child("status").child("moran").child("machine5").child("id5").update({'ip': data})


moran_machine5_check()
#tengakhat

#ip_checks1

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

        else:
            data={'ip':'Down'}
            db.child("status").child("tengakhat").child("machine1").child("id1").set(data)
            db.child("status").child("tengakhat").child("machine1").child("id1").update({'ip': data})


tengakhat_machine1_check()
#check2
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

        else:
            data={'ip':'Down'}
            db.child("status").child("tengakhat").child("machine2").child("id2").set(data)
            db.child("status").child("tengakhat").child("machine2").child("id2").update({'ip': data})


tengakhat_machine2_check()

#check3

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

        else:
            data={'ip':'Down'}
            db.child("status").child("tengakhat").child("machine3").child("id3").set(data)
            db.child("status").child("tengakhat").child("machine3").child("id3").update({'ip': data})


tengakhat_machine3_check()

#check4

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

        else:
            data={'ip':'Down'}
            db.child("status").child("tengakhat").child("machine4").child("id4").set(data)
            db.child("status").child("tengakhat").child("machine4").child("id4").update({'ip': data})


tengakhat_machine4_check()

#check5

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

        else:
            data={'ip':'Down'}
            db.child("status").child("tengakhat").child("machine5").child("id5").set(data)
            db.child("status").child("tengakhat").child("machine5").child("id5").update({'ip': data})


tengakhat_machine5_check()


#dibrugarh_west_rev_circleA

#ip_checks1
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

        else:
            data={'ip':'Down'}
            db.child("status").child("dibrugarh_west_rev_circle").child("machine1").child("id1").set(data)
            db.child("status").child("dibrugarh_west_rev_circle").child("machine1").child("id1").update({'ip': data})


dibrugarh_west_rev_circleA_machine1_check()
#check2
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

        else:
            data={'ip':'Down'}
            db.child("status").child("dibrugarh_west_rev_circle").child("machine2").child("id2").set(data)
            db.child("status").child("dibrugarh_west_rev_circle").child("machine2").child("id2").update({'ip': data})


dibrugarh_west_rev_circleA_machine2_check()
#check3
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

        else:
            data={'ip':'Down'}
            db.child("status").child("dibrugarh_west_rev_circle").child("machine3").child("id3").set(data)
            db.child("status").child("dibrugarh_west_rev_circle").child("machine3").child("id3").update({'ip': data})


dibrugarh_west_rev_circleA_machine3_check()

#check4
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

        else:
            data={'ip':'Down'}
            db.child("status").child("dibrugarh_west_rev_circle").child("machine4").child("id4").set(data)
            db.child("status").child("dibrugarh_west_rev_circle").child("machine4").child("id4").update({'ip': data})


dibrugarh_west_rev_circleA_machine4_check()

#check5

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

        else:
            data={'ip':'Down'}
            db.child("status").child("dibrugarh_west_rev_circle").child("machine5").child("id5").set(data)
            db.child("status").child("dibrugarh_west_rev_circle").child("machine5").child("id5").update({'ip': data})


dibrugarh_west_rev_circleA_machine5_check()
#tengakhat_co
#ip_checks1
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
        else:
            data={'ip':'Down'}
            db.child("status").child("tengakhat_co").child("machine1").child("id1").set(data)
            db.child("status").child("tengakhat_co").child("machine1").child("id1").update({'ip': data})


tengakhat_co_machine1_check()
#check2

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

        else:
            data={'ip':'Down'}
            db.child("status").child("tengakhat_co").child("machine2").child("id2").set(data)
            db.child("status").child("tengakhat_co").child("machine2").child("id2").update({'ip': data})


tengakhat_co_machine2_check()
#check3

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

        else:
            data={'ip':'Down'}
            db.child("status").child("tengakhat_co").child("machine3").child("id3").set(data)
            db.child("status").child("tengakhat_co").child("machine3").child("id3").update({'ip': data})


tengakhat_co_machine3_check()

#check4
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

        else:
            data={'ip':'Down'}
            db.child("status").child("tengakhat_co").child("machine4").child("id4").set(data)
            db.child("status").child("tengakhat_co").child("machine4").child("id4").update({'ip': data})


tengakhat_co_machine4_check()

#check5

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

        else:
            data={'ip':'Down'}
            db.child("status").child("tengakhat_co").child("machine5").child("id5").set(data)
            db.child("status").child("tengakhat_co").child("machine5").child("id5").update({'ip': data})


tengakhat_co_machine5_check()

#naharkatia_rev

#ip_checks1
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

        else:
            data={'ip':'Down'}
            db.child("status").child("naharkatia_rev").child("machine1").child("id1").set(data)
            db.child("status").child("naharkatia_rev").child("machine1").child("id1").update({'ip': data})


naharkatia_rev_machine1_check()
#check2

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

        else:
            data={'ip':'Down'}
            db.child("status").child("naharkatia_rev").child("machine2").child("id2").set(data)
            db.child("status").child("naharkatia_rev").child("machine2").child("id2").update({'ip': data})


naharkatia_rev_machine2_check()
#check3
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

        else:
            data={'ip':'Down'}
            db.child("status").child("naharkatia_rev").child("machine3").child("id3").set(data)
            db.child("status").child("naharkatia_rev").child("machine3").child("id3").update({'ip': data})


naharkatia_rev_machine3_check()

#check4
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

        else:
            data={'ip':'Down'}
            db.child("status").child("naharkatia_rev").child("machine4").child("id4").set(data)
            db.child("status").child("naharkatia_rev").child("machine4").child("id4").update({'ip': data})


naharkatia_rev_machine4_check()

#check5

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

        else:
            data={'ip':'Down'}
            db.child("status").child("naharkatia_rev").child("machine5").child("id5").set(data)
            db.child("status").child("naharkatia_rev").child("machine5").child("id5").update({'ip': data})


naharkatia_rev_machine5_check()