#***********************************************************************#
# Part 1                                                                #
# The objective is to create a Python program that will create a valid  #
# JSON file that contains all of the State Capital addresses.           #
#                                                                       #
# This code create a dictionary of state capitals and their addresses   #
# and reads them to a JSON file.                                        #
#                                                                       #
# Part 2                                                                #
# Create a Python program that will read the file from part 1           #
# and produce a file that includes longitude                            #
# and latitude for each address.                                        #
#                                                                       #
# This code utilizes geopy to look up the addresses and coordinates     #
# of these addresses and matches them, then updates the JSON file.      #
#***********************************************************************#


from geopy.geocoders import Nominatim
#Having issues with timing out, importing for error handling
from geopy.exc import GeocoderTimedOut
from pathlib import Path
import json, time

# Check if the file exists first
json_file = Path("usa_state_capitals.json")

if json_file.exists():
	with open(json_file, "r", encoding="utf-8") as f:
		capitals = json.load(f)
	print("File loaded successfully!")
else:
	print("Error: usa_state_capitals.json not found. Run part 1 first!")
#reading from file
with open("usa_state_capitals.json", "w") as f:
	json.dump(capitals, f, indent = 4)

#checking to see if it loaded properly
print(capitals)

#Object to look up addresses
geolocator = Nominatim(user_agent="my_app")

#looping through the dictionary
for state, info in capitals.items():
	#Noticed service might time out, adding multiple attempts to complete
	for attempt in range(3):
		try:
			#looks up the coordinates and pulls the latitude and longitude
			address = f"{info['street']}, {info['city']}, {info['state_abbr']} {info['zip']}"
			location = geolocator.geocode(address)
			if location:
				info["latitude"] = location.latitude
				info["longitude"] = location.longitude
				#printing states that are completed while running
				print(f"{state} done!")
			break
		except GeocoderTimedOut:
			print(f"{state} timed out, retrying... (attempt {attempt + 1})")
			time.sleep(3) #adding longer retry time
	#Nominatim does not want too many quick requests, adding delay to prevent issues
	time.sleep(1)


# ✅ Cross-platform - works everywhere
with open("usa_state_capitals.json", "w", encoding="utf-8") as f:
	json.dump(capitals, f, indent = 4)
