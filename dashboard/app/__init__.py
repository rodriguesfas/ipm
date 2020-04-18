# -*- coding: utf-8 -*-

import os
import scipy

from time import sleep
from threading import Timer, Thread, Event

from flask import Flask, request, render_template, url_for, request, session, redirect, flash

from flask_socketio import SocketIO, emit
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt

from app.config import database as db
from app.arduino.serial_monitor import SerialMonitor

from bson.objectid import ObjectId


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config.from_object('config')
app.config['SECRET_KEY'] = db.DB['key']

app.config['MONGO_DBNAME'] = db.DB['database']
app.config['MONGO_URI'] = db.DB['uri_mongodb']

mongo = PyMongo(app)
bcrypt = Bcrypt(app)


socketio = SocketIO(app)

clients = []

thread = Thread()
thread_stop_event = Event()




@app.route('/')
def index():
    # check session.
    if 'email' in session:
        email = session['email']
        return redirect(url_for('dashboard'))

    return render_template('index.html')


@app.route('/login')
def login():
    if 'email' in session:
        email = session['email']
        return redirect(url_for('dashboard'))

    return render_template('login.html')


@app.route('/login_validation', methods=['POST'])
def login_validation():
    users = mongo.db.users
    login_user = users.find_one({'email' : request.form['email']})

    print(">>   db: ", login_user['password'])
    print(">>   form: ", bcrypt.generate_password_hash(request.form['password']).decode('utf-8'))

    if login_user:
        if bcrypt.check_password_hash(login_user['password'], request.form['password']):
            session['email'] = request.form['email']
            return redirect(url_for('dashboard'))
        else:
            flash(message='Email e/ou Senha são inválidos!', category='danger')
            return redirect(url_for('login'))
    else:
        flash(message='Email não cadastrado!', category='danger')
        return redirect(url_for('login'))


@app.route('/dashboard')
def dashboard():
    if 'email' in session:
        email = session['email']
        patients = mongo.db.patients
        all_patients = patients.find().count()
        return render_template("dashboard.html", num_patinets=all_patients)

    return redirect(url_for('login'))


@app.route('/login_monitor', methods=['GET'])
def login_monitor():
    if 'email' in session:
        return render_template('login_monitor.html')
    
    return redirect(url_for('login'))


@app.route('/validation_monitor', methods=['POST'])
def validation_monitor():
    patients = mongo.db.patients
    patient = patients.find_one({'cpf': request.form['cpf']})

    print("patient: ", patient['_id'])

    if patient:
        data = {
            "_id_patient": str(patient['_id']),
            "cpf": patient['cpf'],
            "name": patient['name'],
            "description": patient['description'],
            "bed": patient['bed']
        }
        
        session['patient_data'] = data 
        return redirect(url_for('monitor'))

    flash(message='As credenciais do paciente são inválidas!', category='danger')
    return redirect(url_for('login_monitor'))


@app.route('/monitor')
def monitor():
    if 'email' in session:
        return render_template('monitor.html', data=session['patient_data'])

    return redirect(url_for('login'))


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'email' : request.form['email']})

        if existing_user is None:
            hashpass = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
            
            users.insert({
                'name' : request.form['username'], 
                'email' : request.form['email'], 
                'password' : hashpass
                })

            session['email'] = request.form['email']

            return redirect(url_for('dashboard'))
        
        flash(message='Esse email já foi cadastrado!', category='danger')
        return render_template('register.html')

    return render_template('register.html')


@app.route("/logout")
def logout():
    session.pop('email', None)
    return redirect(url_for('login'))


@app.route('/patients')
def patients():
    if 'email' in session:
        patients = mongo.db.patients
        all_patients = patients.find()
        return render_template("patients.html", all_patients=all_patients)


@app.route('/register_patient', methods=['POST'])
def register_patient():
    if 'email' in session:
        if request.method == 'POST':
            patients = mongo.db.patients
            existing_user = patients.find_one({'cpf' : request.form['cpf']})

            if existing_user is None:

                patients.insert({
                    'name' : request.form['name'], 
                    'cpf' : request.form['cpf'], 
                    'description' : request.form['description'],
                    'bed' : request.form['bed'],
                    })

                flash(message='Paciente cadastrado com sucesso!', category='success')
                return redirect(url_for('patients'))
            
            flash(message='Esse paciente já foi cadastrado!', category='danger')
            return redirect(url_for('patients'))

    return redirect(url_for('patients'))


def save_data(data):
    sensors = mongo.db.sensors
    sensors.insert({
        '_id_patient' : session['patient_data']['_id_patient'],
        's1' : data['s1'], 
        's2' : data['s2'], 
        's3' : data['s3'],
        's4' : data['s4'],
        'date' : data['date'],
        'time' : data['time'],
        })


@socketio.on('message')
def print_message(sid, message):
    print("Socket ID: " , sid)
    print(message)


@socketio.on('connected')
def connected():
    global thread
    
    # Start the random number generator thread only if the thread has not been started before.
    if not thread.isAlive():
        print(">> Starting Thread")

        clients.append(request.sid)
        print(">> User connected {} ".format(request.sid))

        thread = Notification()
        thread.start()

    data = SerialMonitor().read()
    thread.push_data(data)
    save_data(data)

    emit('graphic_sensors', data)
    emit('connect', {'data': 'Connected'})


@socketio.on('disconnect')
def disconnect():
    print(">> User disconnected {} ".format(request.sid))
    clients.remove(request.sid)



from app.routes import routes


class Notification(Thread):

    list_cmHg_s1 = []
    list_cmHg_s2 = []
    list_cmHg_s3 = []
    list_cmHg_s4 = []

    CMHG_LIGTH = 12     # leve
    CMHG_AVERAGE = 32   # 28 à 32 cmHG constante já pode ocasionar uma lesão;
                        # 28 Milímetros de mercúrio = 0.038066 kgf/cm² = 
                        # 0.38 kg = 0.03874921609316 kgf/cm² = 28.5024 Milímetros de mercúrio
                        # 0.044 kgf/cm² = 32.3647 Milímetros de mercúrio.

    CMHG_HIGH = 70      # 70 cmHg constante, apalicada por 2h provoca dano irrevrsival.

    TIME = 7200 # tempo de espera para enviar notificações sobre os dados.

    


    def __init__(self):
        self.delay = 10
        super(Notification, self).__init__()

    def clear_lists(self):
        self.list_cmHg_s1.clear()
        self.list_cmHg_s2.clear()
        self.list_cmHg_s3.clear()
        self.list_cmHg_s4.clear()

    def push_data(self, data):
        self.list_cmHg_s1.append(self.kg_to_cmHG(self.kg_to_kgf(int(data['s1']))))
        self.list_cmHg_s2.append(self.kg_to_cmHG(self.kg_to_kgf(int(data['s2']))))
        self.list_cmHg_s3.append(self.kg_to_cmHG(self.kg_to_kgf(int(data['s3']))))
        self.list_cmHg_s4.append(self.kg_to_cmHG(self.kg_to_kgf(int(data['s4']))))

    def kg_to_kgf(self, value):
        """[1 quilograma [kg] = 0,101971621297793 quilograma-força segundo²/metro [kgf•s²/m]]
        
        Arguments:
            value {[type]} -- [description]
        """
        return value * 0.101971621297793

    def kg_to_cmHG(self, value):
        return  value * 735.6 # data kgf convert to cmHg milímetros de mercúrio (mm Hg)

    def averages_pressure(self):
        # print("Value list cmHG: {}".format(self.list_cmHg_s1))
        s1 = scipy.mean(self.list_cmHg_s1)
        s2 = scipy.mean(self.list_cmHg_s2)
        s3 = scipy.mean(self.list_cmHg_s3)
        s4 = scipy.mean(self.list_cmHg_s4)

        self.clear_lists()

        return s1, s2, s3, s4

    def alert(self):
        import json
        data = []
        msg = ''

        for index, sensor in enumerate(self.averages_pressure()):
            if(sensor >= self.CMHG_LIGTH and sensor < self.CMHG_AVERAGE):
                msg = 1
            if(sensor >= self.CMHG_AVERAGE and sensor < self.CMHG_HIGH):
                msg = 2
            if(sensor >= self.CMHG_HIGH):
                msg = 3

            item = {
                "s{}".format(index+1): sensor,
                "msg": msg 
            }

            data.append(item)

        return data


    def send_notification(self):
        while not thread_stop_event.isSet():
            # test send data.
            # from random import random
            # number = round(random()*10, 3)
            socketio.emit('notification', self.alert())
            sleep(self.delay)

    def run(self):
        self.send_notification()