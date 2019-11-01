from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

def main():
    with open('county_demographics.json') as demographics_data:
        states = json.load(demographics_data)

def fun_fact(states):
  state = {}
