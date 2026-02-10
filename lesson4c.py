#A for loop can also be used to iterate through a list,tuple,string or even a dictionary

name = "Johnson"

for letter in name:
    if letter == "n" :
        print("This is letter n")
    else:
        print(letter)

print("==========================================")
#Below is a list of counties
counties = ["Nairobi", "Mombasa", "Kisumu", "Nakuru","Eldoret","Kajiado", "Machakos", "Meru", "Embu"]

print(counties)

for county in counties:
    print(county)

print('============================================')

for county in counties:
    if county == "Nakuru":
        print("County found")
        break
else:
    print("County not found")
print('===========================================')
#The for loop can also be used to iterate through a dictionary

player ={
    "name":"Mbappe",
    "age" : 25,
    "teams" : ["PSG","Monaco","France"],
    "nationality": "French"
}

for key in player :
    print(key)

print('=======================================')
for value in player:
    print(player[value])