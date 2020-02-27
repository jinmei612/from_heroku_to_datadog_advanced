from flask import Flask
  
from datadog import initialize, statsd
import time
import random
import requests


app = Flask(__name__)

@app.route('/')
def bubble_tea():
        resp=requests.get("https://gentle-plains-40923.herokuapp.com/")
        return "another bubbletea webapp"

if __name__ == '__main__':
  app.run()
