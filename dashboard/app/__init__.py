# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit

import os
from app.arduino.serial_monitor import SerialMonitor

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
app.config.from_object('config')

socketio = SocketIO(app)

clients = []

@socketio.on('connected')
def connected():
    #print("connected {}".format(request.sid))
    clients.append(request.sid)
    print(">> user connected {} ".format(request.sid))

    data = SerialMonitor().read()

    emit('temp', data)
    emit('connect', {'data': 'Connected'})

@socketio.on('disconnect')
def disconnect():
    print(">> user disconnected {} ".format(request.sid))
    clients.remove(request.sid)


# Load the views.
from app import views

# Load the config file
