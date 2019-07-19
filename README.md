# Injury Prevention Monitor - IPM / Monitor de Prevenção de Lesões - MPL

![dashboard](https://github.com/rodriguesfas/Injury-Prevention-Monitor/blob/master/user-guide/screenshot/dashboard.png)

# DashBoard

O DashBoard do Monitor de Prevenção de Lesões, foi construido utilizando a tecnologia servidor [NodeJS](https://nodejs.org/en/). 

## Instalação de Bibliotecas Dependentes do DashBoard
    
    npm install

### Configuração da Porta do Servidor

    var mySerial = new SerialPort("/dev/ttyUSB0", {
        baudrate : 9600,
        parser : serialport.parsers.readline("\n")
        });

# Firmware
O código fonte do embarcado foi escrito na linguagem [Arduino](https://arduino.cc).

## Instalação de Bibliotecas Dependentes do Firmware do Arduino   

[HX711](https://github.com/bogde/HX711)

### Configurações da Placa Arduino
    ttyUSB0 = "Your Port USB"

    sudo chmod 777 /dev/ttyUSB0
	or
    sudo chmod a+rw /dev/ttyUSB0

# Iniciando o Servidor DashBoard

    node-dev server.js

    http://localhost:3000 or http://127.0.0.1:3000

# Parando o Servidor DashBoard

    Crtl + c

# Lista de Componentes do Protótipo

- 2 Sensores de Peso 50Kg Célula de Carga.
- 1 Módulo Conversor HX711.
- 1 Arduino Uno.
- N Jumpers.

# Desenho Esquemático Do Protótipo

O desenho esquemático do protótipo foi construido utilizando a ferramenta de modelagem [Fretzing](https://fritzing.org/home/).

# Referências

## Artigos
- [Sistema Automático de Prevençãode Úlceras por Pressão](https://repositorio.uma.pt/handle/10400.13/75)

## Paginas Web

### Tutoriais Arduino
- [Conversor HX711: Balança Digital com Sensor de Peso e Arduino Uno](http://blog.baudaeletronica.com.br/conversor-hx711-para-balanca-eletronica/)

- [Criando uma Balança com o Arduino](https://www.robocore.net/tutoriais/celula-de-carga-hx711-com-arduino?fbclid=IwAR2aD6KqunSnPPSsosWZVWt0Pk9HB9HtG3jASjT7Ue2qxKIl7NotRoJ8ZkA)

- [SENSOR DE PESO COM ARDUINO – A VARIAÇÃO DE UM STRAIN GAGE](https://blog.usinainfo.com.br/sensor-de-peso-com-arduino-variacao-de-um-strain-gage/)


- [O Arduino funciona como uma balança? Sim! Ele é capaz! - Módulo HX711](https://www.youtube.com/watch?v=-qLfybfvsHw&feature=push-u-sub&attr_tag=cvjlzRGy3V1M0wxC%3A6)

- [Arduíno Gerando Gráficos Com Socket.io](http://clubedosgeeks.com.br/programacao/arduino-gerando-graficos-com-socket-io)

### Desing Corpo Humando
- [Humanan Atomy Illustrations Template](https://www.humananatomyillustrations.com/)

### Gráficos
- [ChartJS](https://www.chartjs.org/)