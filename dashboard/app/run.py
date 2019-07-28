import json
import time
import serial
import random

from datetime import datetime, date, time
from time import gmtime, strftime

from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

clients = []


@app.route('/')
def index():
    return render_template("index.html")


@socketio.on('connected')
def connected():
    #print("connected {}".format(request.sid))
    clients.append(request.sid)
    read_data_monitor_serial()
    emit('connect', {'data': 'Connected'})


@socketio.on('disconnect')
def disconnect():
    print("disconnected {} ".format(request.sid))
    clients.remove(request.sid)


def r(data):
    return data.replace("b'", "").replace("\\r\\n'", "")


def read_data_monitor_serial():
    try:
        arduino = serial.Serial("/dev/ttyACM0", timeout=1)

        raw_data = str(arduino.readline())
        raw_json = r(raw_data)
        data_json = json.loads(raw_json)

        # format data json.
        data = {
            "date": str(date.today()),
            "time": str(strftime("%H:%M:%S", gmtime())),
            "s1": data_json['s1'],
            "s2": data_json['s2'],
            "s3": data_json['s3']
        }
        #print(data)

        emit('temp', data)

    except Exception as err:
        print(err)


if __name__ == '__main__':
    socketio.run(app, host="127.0.0.1", port=9000, debug=True)
