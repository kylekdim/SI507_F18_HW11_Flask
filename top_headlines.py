
from flask import Flask, render_template, url_for
import requests
from secrets_example import *
import json

app = Flask(__name__)

@app.route('/user/<word>')
def user_page(word):
baseurl = "http://api.nytimes.com/svc/search/v2/articlesearch.json"
params_diction = {}
params_diction["api-key"] = api_key # from secrets_example.py
params_diction["section"] = 'technology'
    
nyt_resp = requests.get(baseurl, params_diction)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)

