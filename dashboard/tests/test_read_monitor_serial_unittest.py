import unittest

from app.arduino.serial_monitor import SerialMonitor

class TestMonitorSerial(unittest.TestCase):

    def __init__(self):
        pass

    def read(self):
        data = SerialMonitor().read;
        print(data)

if __name__ == "__main__":
    unittest.main()