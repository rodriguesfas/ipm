#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import app, socketio

if __name__ == '__main__':
    # TODO Remover IP e Port daqui e colocar em um aqruivo de configuração.
    socketio.run(app, host="127.0.0.1", port=9000)