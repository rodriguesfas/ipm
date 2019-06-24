"use strict";

/**
 * Software: IPM
 * @autor: RodriguesFAS
 * @site: http://rodriguesfas.com.br
 * @license: MIT
 * @data: 24/06/2019
 * @vesion: 0.0.1
 */

var express = require("express");

var app = require("express")();
app.use(express.static(__dirname + "/public"));
var http = require("http").Server(app);

var io = require("socket.io")(http);

const SerialPort = require("serialport");
const Readline = SerialPort.parsers.Readline;
const parser = new Readline();

app.get("/", function(req, res) {
    res.sendfile("view/index.html");
});

const mySerial = new SerialPort("/dev/ttyUSB0", {
    baudRate: 9600
});

mySerial.pipe(parser);

mySerial.on("open", function() {
    console.log("Arduino conexão estabelecida!");
});

mySerial.on("data", function(data) {
    // Send data in page web.
    io.emit("dataDuino", {
        value: data.toString()
    });

    // Exibe no console o dado recebido do Arduino.
    console.log(data.toString());
});

var usuarios = 0;

io.on("connection", function(socket) {
    console.log("Usuário Conectado!");
    usuarios++;

    io.emit("usuarios online", usuarios);
    socket.on("mensagem", function(msg) {
        io.emit("mensagem", msg);
    });

    socket.on("disconnect", function() {
        console.log("Usuário Desconectado!");
        usuarios--;
        io.emit("users", usuarios);
    });
});

http.listen("3000", function() {
    console.log("Servidor on-line em http://localhost:3000 - para sair Ctrl+C.");
});