#A dictionary is a data type that stores data in terms of key - value pair
#It is introduced by the use of curly braces {}
#The values stored inside of a dictionary can be of any data type.
#To access the values in a dictionary we use the keys


phonebook = {
    "Kitaka" : "254712345678",
    "Mary" : "25445842857",
    "Stephen" : "25404235982" 
}

#showing the entire dictionary
print(phonebook)

#print out Kitaka's number
print(phonebook["Kitaka"])

print('=============================')

player = {
    "name" : "Messi",
    "age"  :  40,
    "team" : ["PSG", "Barcelona", "Argentina"],
    "more" : {
        "children" : 3,
        "residence" : "US",
        "phone" : (25424067020,254765344,254745842857)
    }
}

#print the second team messi played for
print(player["team"][1])

print(player["more"]["phone"][1])