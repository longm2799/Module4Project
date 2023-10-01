import requests 
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    className = 'cnit 381'

    return render_template('index.html', data=className)

@app.route('/about')
def about():
    return 'About'

@app.route('/another')
def another():
    return 'Another'

url = "http://api.ipstack.com/check?access_key=ea37f7dd47cf2408fdaadd4003ae92a8"
json_data = requests.get(url).json()
print("Ip Address: "+ (json_data["ip"]))
