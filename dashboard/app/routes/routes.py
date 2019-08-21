#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template, session, request, redirect, url_for
from app import app



@app.route('/patient')
def patient():
    return render_template("patient.html")




@app.errorhandler(400)
def page_not_found(e):
    return render_template('400.html'), 400

@app.errorhandler(403)
def page_not_found(e):
    return render_template('403.html'), 403

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(410)
def page_not_found(e):
    return render_template('410.html'), 410

@app.errorhandler(505)
def page_not_found(e):
    return render_template('404.html'), 505