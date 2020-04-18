#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from serial import Serial
from time import gmtime, strftime
from datetime import datetime, date, time


class SerialMonitor(object):

    port = "/dev/ttyACM0"

    def __init__(self):
        pass

    def clear_data(self, data):
        return data.replace("b'", "").replace("\\r\\n'", "")

    def read(self):
        try:
            arduino = Serial(self.port, timeout=1)
            raw_data = str(arduino.readline())
            
            raw_json = self.clear_data(raw_data)
            data_json = json.loads(raw_json)

            data_json = {
                "date": str(date.today()),
                "time": str(strftime("%H:%M:%S", gmtime())),
                "s1": data_json['s1'],
                "s2": data_json['s2'],
                "s3": data_json['s3'],
                "s4": data_json['s4']
            }

            return data_json
        except Exception as err:
            print(err)

if __name__ == "__main__":
    while(True):
        data = SerialMonitor().read()
        print(">> data arduino: ", data)
