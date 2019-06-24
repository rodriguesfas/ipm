# Injury Prevention Monitor - IPM

# Description

# Dashboard (NodeJS)

## Install Dependent Libraries
    
    npm install

### Config Port in Server

    var mySerial = new SerialPort("/dev/ttyUSB0", {
        baudrate : 9600,
        parser : serialport.parsers.readline("\n")
        });

# Firmware (Arduino)

## Install Dependent Libraries   

[HX711](https://github.com/bogde/HX711)

### Configure Board
    ttyUSB0 = "Your Port USB"

    sudo chmod 777 /dev/ttyUSB0
	or
    sudo chmod a+rw /dev/ttyUSB0

# Run Server

    node-dev server.js

    http://localhost:3000 or http://127.0.0.1:3000

# Stop Server

    Crtl + c

# List os Components

- 2 Sensores de Peso 50Kg Célula de Carga.
- 1 Módulo Conversor HX711.
- 1 Arduino Uno.
- N Jumpers.

# Schematic Drawings (Fretzing)

# Credits

- [Conversor HX711: Balança Digital com Sensor de Peso e Arduino Uno](http://blog.baudaeletronica.com.br/conversor-hx711-para-balanca-eletronica/)

- [Criando uma Balança com o Arduino](https://www.robocore.net/tutoriais/celula-de-carga-hx711-com-arduino?fbclid=IwAR2aD6KqunSnPPSsosWZVWt0Pk9HB9HtG3jASjT7Ue2qxKIl7NotRoJ8ZkA)

- [SENSOR DE PESO COM ARDUINO – A VARIAÇÃO DE UM STRAIN GAGE](https://blog.usinainfo.com.br/sensor-de-peso-com-arduino-variacao-de-um-strain-gage/)

- [Humanan Atomy Illustrations Template](https://www.humananatomyillustrations.com/)