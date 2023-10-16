import requests

def test_classname():
 assert url = "http://api.ipstack.com/check?access_key=ea37f7dd47cf2408fdaadd4003ae92a8"
 assert json_data = requests.get(url).json()
 assert className = (json_data["ip"])

