import requests
import json

api_url = 'http://api.open-notify.org/astros.json'
response = requests.get(api_url)
json_data = response.json()

for this_person in json_data['people']:
    print(this_person['name'], this_person['craft'])
print()
print(f"there's {json_data['number']} person in space now.")