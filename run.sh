#!/bin/bash

echo "=== Starting the program ==="

#***********************************************************************#
# Part 1                                                                #
# The objective is to create a Python program that will create a valid  #
# JSON file that contains all of the State Capital addresses.           #
#                                                                       #
# This code create a dictionary of state capitals and their addresses   #
# and reads them to a JSON file.                                        #
# 								        #
# Part 2							        #
# Create a Python program that will read the file from part 1           #
# and produce a file that includes longitude                            #
# and latitude for each address.					#
#                                     					#
# This code utilizes geopy to look up the addresses and coordinates	#
# of these addresses and matches them, then updates the JSON file.	#
#***********************************************************************#



python3 state_capitals_part1.py
python3 state_capitals_part2.py

echo "=== Program finished ==="
