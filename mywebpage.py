from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__)

@app.route("/")
def render_main():
    with open('county_demographics.json') as demographics_data:
        states = json.load(demographics_data)
    return render_template('home.html')

if __name__=="__main__":
    app.run(debug=False)
