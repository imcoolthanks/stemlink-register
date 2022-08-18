from flask import Flask, request, redirect
from flask import render_template
from . import app

import csv

@app.route('/', methods = ['POST', 'GET'])
def home():
    if request.method == 'POST':

        email = request.form.get('email') 

        with open('emails.csv', 'a+', newline='') as file:

            arr = []
            arr.append(email)

            writer = csv.writer(file)
            writer.writerow(arr)

        return redirect('/thanks')

    else:
        return render_template('Home.html')

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')