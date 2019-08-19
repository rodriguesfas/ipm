# -*- coding: utf-8 -*-

import os

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
    patients = mongo.db.patients
    all_patients = patients.find()
    return render_template("patients.html", all_patients=all_patients)


@app.route('/register_patient', methods=['POST'])
def register_patient():
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


@socketio.on('connected')
def connected():
    #print("connected {}".format(request.sid))
    clients.append(request.sid)
    print(">> user connected {} ".format(request.sid))

    data = SerialMonitor().read()

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

    emit('temp', data)
    emit('connect', {'data': 'Connected'})


@socketio.on('disconnect')
def disconnect():
    print(">> user disconnected {} ".format(request.sid))
    clients.remove(request.sid)



from app.routes import routes
