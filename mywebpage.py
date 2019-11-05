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
def render_reply(state):
    with open('county_demographics.json') as demographics_data:
        demographicData = json.load(demographics_data)
    funFact = []
    for data in counties:
        if (data['Percent Under 5 Years'] not in funFact):
            funFact.append(data['Percent Under 5 Years'])
        return(state + 'has' + funFact + 'percent of their population under the age of five.')
    return render_template('home.html', states = get_state_options(demographicData), fact = 'yes')

def get_state_options(counties):
    listOfStates = []
    option = ''
    for data in counties:
        if (data['State'] not in listOfStates):
            listOfStates.append(data['State'])
    for state in listOfStates:
        option = option + Markup("<option value=\"" + state + "\">" + state + "</option>")
    print(option)
    return option

if __name__=="__main__":
    app.run(debug=False)
