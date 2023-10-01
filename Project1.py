import requests

url = "http://api.ipstack.com/check?access_key=ea37f7dd47cf2408fdaadd4003ae92a8"
json_data = requests.get(url).json()
print("Ip Address: "+ (json_data["ip"]))