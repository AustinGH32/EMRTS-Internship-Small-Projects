import json
from geopy.geocoders import Nominatim

#reading from file
with open("usa_state_capitals.json", "r") as f:
    capitals = json.load(f)

#checking to see if it loaded properly
print(capitals)    


