import json, time
#Nominatim converts addresses to coordinates
from geopy.geocoders import Nominatim

#reading from file
with open(r"C:\Users\Austin\Documents\GitHub\EMRTS\usa_state_capitals.json", "r") as f:
    capitals = json.load(f)

#checking to see if it loaded properly
print(capitals)

#Object to look up addresses
geolocator = Nominatim(user_agent="my_app")

#looping through the dictionary
for state, info in capitals.items():
    #looks up the coordinates and pulls the latitude and longitude
    location = geolocator.geocode(info["address"])
    if location:
        info["latitude"] = location.latitude
        info["longitude"] = location.longitude
    #Nominatim does not want too many quick requests, adding delay to prevent issues
    time.sleep(1)


with open(r"C:\Users\Austin\Documents\GitHub\EMRTS\usa_state_capitals.json", "w") as f:
    json.dump(capitals, f, indent=4)