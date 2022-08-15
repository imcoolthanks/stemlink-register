from flask import Flask, request
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

        return render_template('thanks.html')

    else:
        return render_template('base.html')