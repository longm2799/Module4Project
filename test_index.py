import requests
from api import index



assert index.url == "http://api.ipstack.com/check?access_key=ea37f7dd47cf2408fdaadd4003ae92a8"
assert index.json_data == requests.get(index.url).json()
assert index.className == (index.json_data["ip"])

