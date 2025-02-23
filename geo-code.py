'''
Adapted from:
https://github.com/googlemaps/google-maps-services-python
https://github.com/googlemaps/google-maps-services-python/tree/master/tests

Enable the following APIs in the GCP console:
    Places API
    Geocoding API

Install libraries listed in requirements.txt (activate virtual env first):
pip3 install -r requirements.txt    

API_KEY must be defined in .env file in the project folder.
API_KEY='YOUR API KEY'    ## NO SPACES
'''

import googlemaps
from dotenv import load_dotenv
import json
import os

load_dotenv()

API_KEY = os.environ.get('API_KEY')

gmaps = googlemaps.Client(key=API_KEY)

address = input('Input an address (street, city, state): ')

geocode_result = gmaps.geocode(address)
pretty_json = json.dumps(geocode_result, indent=4)

# Comment out to see entire json result
# print(pretty_json)

lat, lon = (geocode_result[0]['navigation_points'][0]['location']['latitude'],
           geocode_result[0]['navigation_points'][0]['location']['longitude'])
geo_loc = {"lat":lat, "lon":lon}
print(f"The adddress '{address}' is located at: {geo_loc}") 


