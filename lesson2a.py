#python list- A list in python is a collection of items that are ordered in a certain way.
#A list is introduced by the use of square brackets[]
#The items of a list are stored inside of indexes
#In programming we start counting from index zero(o)
#A list is mutable i.e the contents of a list can be changed.

cars = ["BMW", "Benze", "Hiace", "prado", "Probox", "MClaren", "Range"]

print(cars)
print(type(cars))

#Accessing items in a list
print(cars[2])

print("The car on index four is:", cars[4])

#List slicing - This is creating a list from a given bigger list
print(cars[4:])

#Printing from index zero(0) to three(3)
print(cars[:4])

#printing from hiance to probox
print(cars[2:5])

#List - Mutability
#We use the function append to add an item at the end of a list
cars.append("Mercedes")
print(cars)

cars.append("subaru")
print(cars)

#we use the pop function to remove an item at the end of the list
cars.pop()
print(cars)

#we can use an index to add items to a list
cars[5] = "Pajero"
print(cars)

# we can use the sort function to sort our items in alphabetical order
cars.sort()
print(cars)

#Deleting an item on the list
del cars[4]
print(cars)

#another alternative to deleting an item
cars.pop(4)
print(cars)

#Specific removal of an item
cars.remove("BMW")
print(cars)