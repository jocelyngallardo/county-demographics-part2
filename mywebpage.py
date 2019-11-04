from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__)

@app.route("/")

def get_state_options(states):
    listOfStates = []
    for data in states:
        if (data['State'] not in listOfStates):
            listOfStates.append(data['State'])
    return listOfStates

def render_main():
    with open('county_demographics.json') as demographics_data:
        states = json.load(demographics_data)
    return render_template('home.html', states=listOfStatess)

if __name__=="__main__":
    app.run(debug=False)
