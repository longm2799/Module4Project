import requests 
from flask import Flask, render_template

url = "http://api.ipstack.com/check?access_key=ea37f7dd47cf2408fdaadd4003ae92a8"
json_data = requests.get(url).json()
print("Ip Address: "+ (json_data["ip"]))

app = Flask(__name__)
@app.route('/')
def home():
url = "http://api.ipstack.com/check?access_key=ea37f7dd47cf2408fdaadd4003ae92a8"
json_data = requests.get(url).json()
    className = (json_data["ip"])

    return render_template('index.html', data=className)

@app.route('/about')
def about():
    return 'About'

@app.route('/another')
def another():
    return 'Another'


