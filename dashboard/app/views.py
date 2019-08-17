#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template

from app import app

@app.route('/')
def monitor():
    return render_template("monitor.html")