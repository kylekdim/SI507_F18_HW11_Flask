
from flask import Flask, render_template, url_for
import requests
from secrets_example import *
import json

app = Flask(__name__)

if __name__ == '__main__':
	app.run(debug=True)

