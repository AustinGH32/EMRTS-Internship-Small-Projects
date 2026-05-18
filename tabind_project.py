#**************************************************************************************#
# The objective of this project is to develop a program that                           #
# takes the letter combination “tabind” only once and creates                          #
# an alphabetical list of all the words,                                               #    
# from a Scrabble dictionary that can be found with those letters.                     #
#                                                                                      #
# This programs will read in a txt file of scrabble words,                             #
# and will compare the letter counts of each word with the letter counts of "tabind".  #
# If the word can be made with the letters in "tabind", it will be printed out.        #
#                                                                                      #
#**************************************************************************************#

from collections import Counter

#Counter counts the number of each letter, so we can compare with other letter counts
tabind_count = Counter("tabind")

#word total
word_total = 0

#empty list to hold the scrabble words
scrabble = []

scrabble.sort() #sort the scrabble list alphabetically

#read in a txt file for scrabble words
with open(r"C:\Users\Austin\Downloads\TWL06.txt", "r") as file:
    for line in file:
        # adding in each word to the scrabble list
        # removes white space and makes all letters lowercase for easier comparison
        scrabble.append(line.strip().lower())

scrabble.sort() #sort the scrabble list alphabetically

#iterating for every word in the scrabble list
for word in scrabble:
    #word has to be less than or equal to 6 letters, since we can only use the letters in "tabind" once
    if len(word) <= 6:

        # initially assume the word is valid, then check if it is valid by comparing the letter counts of the 
        # word and "tabind"
        is_valid = True

        #count the number of each letter in the word
        word_count = Counter(word)

        #if the count of each letter in the word is less than or equal to the count of each letter in "tabind", 
        # then we can use that word
        for letter in word_count:
            # if the letter is not in "tabind", then we cannot use that word
            if letter not in tabind_count:
                is_valid = False
                break
            
            #checking to see if the count of the letters in the word is less than or equal to tabind
            if letter in tabind_count:
                # if the count is <= tabind, we can keep the word as a valid word, 
                if word_count[letter] <= tabind_count[letter]:
                    is_valid = True
                # if the word isnot, we can break out of the loop and move on to the next word
                else:
                    is_valid = False
                    break
        if is_valid:
            word_total +=1
            print(word)   

print(f"Total number of words that can be made with the letters in 'tabind': {word_total}")


