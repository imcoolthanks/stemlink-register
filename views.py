from flask import Flask, request, redirect, url_for
from flask import render_template
from . import app

import csv

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/thx', methods = ['GET', 'POST'])
def thx():
    if request.method == 'POST':

        email = request.form.get('email') 

        with open('emails.csv', 'a+', newline='') as file:

            arr = []
            arr.append(email)

            writer = csv.writer(file)
            writer.writerow(arr)

        print("rendering template")

        return render_template('Thanks.html')
    else:
        return render_template('Thanks.html')

    