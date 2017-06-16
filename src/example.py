import json
import requests

location_url = 'https://developers.zomato.com/api/v2.1/locations'
header = {"user-key": "e1834ce4678d0c4d605fe24e0eb99b54"}
paramaters = {
    'query': 'Vaishali%20Nagar'
}
response = requests.get(location_url, params=paramaters, headers=header)
location_data = json.loads(response.text)

search_url = 'https://developers.zomato.com/api/v2.1/search'

if location_data['location_suggestions'][0]['entity_type'] and location_data['location_suggestions'][0]['entity_id']:
    paramaters = {
        'entity_type': location_data['location_suggestions'][0]['entity_type'],
        'entity_id': location_data['location_suggestions'][0]['entity_id'],
        'count': '1'
    }
    response = requests.get(search_url, params=paramaters, headers=header)
    restaurant_data = json.loads(response.text)
    if restaurant_data['restaurants'][0]['restaurant']:
        restaurant_data = restaurant_data['restaurants'][0]['restaurant']
        print restaurant_data['name']
