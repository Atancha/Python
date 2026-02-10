#Loops ->sometimes we may need to do a piece of work a number of  repeated times and in such cases scenario we may use loops.
#A loop is a controlled structure that allows us to execute a block of code repeatedly until a certain condition is met.
#There are two types of loops in python i.e. The for loop and the while loop.

#Below is the syntax of a for loop in python:
""""
for variable in range(n):
    # block of code to be executed
"""

print("Hello Moses")

for greeting in range(5):
    print("Hello Moses" , greeting)


print("==============================================")

for number in range(10,20):
    print(number)


print("=======================================")

#find the even numbers in the range of 50 to 71
for number in range(50,71,2):
    print(number)

print("=============================================")

#create a python program that prints the odd numbers from 100 to 150
for number in range(101,151,2):
    print(number)

print('===============================================')
#create a program that prints the multiples of 3 starting from 201 to 150

for number in range(201, 149, -3):
    print(number)

    #OR
print("===================================================")
for number in range(201, 149, -1):
    if number % 3 == 0:
        print(number)

print("========================================================")
#create a python programme that prints the leap years in between 2000 and 2024

for year in range(2000,2025,4):
    print(year)

print("=======================================")


for year in range(2000, 2025):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year)