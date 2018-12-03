#Kyle Chang HW11, Wed Section
from flask import Flask, render_template, url_for
import requests
from secrets_kyle import *
import json

app = Flask(__name__)

@app.route('/') #homepage
def index():
	return render_template('index.html')

@app.route('/user/<word>') #user page
def user_page(word):
	baseurl = "http://api.nytimes.com/svc/topstories/v2/technology.json"
	params_diction = {}
	params_diction["api-key"] = api_key # from secrets_example.py
	
	nyt_resp = requests.get(baseurl, params_diction)
	nyt_data = json.loads(nyt_resp.text)
	articles = []

	for result in nyt_data['results'][0:5]:
		title = result['title']
		url = result['url']
		article = title + ' ({})'.format(url)
		articles.append(article)

	return render_template('user.html', name = word, section = "technology", articles = articles)

if __name__ == '__main__':
	app.run(debug=True)
