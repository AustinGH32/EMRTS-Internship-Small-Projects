tabind = "tabind"

scrabble = []

#read in a txt file for scrabble words
with open(r"C:\Users\Austin\Downloads\dictionary.txt", "r") as file:
    for line in file:
        scrabble.append(line.strip())

#checking if read in
print(scrabble)

