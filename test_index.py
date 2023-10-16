import requests


def test_classname():
 assert data.url == "http://api.ipstack.com/check?access_key=ea37f7dd47cf2408fdaadd4003ae92a8"
 assert data.json_data == requests.get(data.url).json()
 assert data.className == (data.json_data["ip"])

