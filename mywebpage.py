from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__)

@app.route("/")
def render_main():
    with open('county_demographics.json') as demographics_data:
        demographicData = json.load(demographics_data)
    return render_template('home.html', states = get_state_options(demographicData), fact = '')

@app.route("/reply")
def render_reply():
    with open('county_demographics.json') as demographics_data:
        demographicData = json.load(demographics_data)
    return render_template('home.html', states = get_state_options(demographicData), fact = get_fact(demographicData, request.args['states']))

def get_state_options(counties):
    listOfStates = []
    option = ''
    for data in counties:
        if (data['State'] not in listOfStates):
            listOfStates.append(data['State'])
    for state in listOfStates:
        option = option + Markup("<option value=\"" + state + "\">" + state + "</option>")
    return option

def get_fact(counties, states):
     counter = 0
     for data in counties:
        if data['State'] == states:
            counter+=1
     fact = str(states) + ' has ' + str(counter) + ' percent of its population under the age of 5 in one if its counties.'
     return fact
    
if __name__=="__main__":
    app.run(debug=False)
