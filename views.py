import email
from flask import Flask, request
from flask import render_template

import database

import flask

app = flask.Flask(__name__)

import csv

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/thx', methods = ['GET','POST'])
def thx():
    if request.method == 'POST':

        email = request.form.get('email') 

        database.new_email(email)

    return render_template('Thanks.html')


@app.route('/ayden/display_all')
def display_all():
    emails = database.list_emails()

    return render_template('emails.html', emails=emails)