#create a python programme that is able to determine whether a number entered is an odd number or an even number
#number = int(input("Enter a number: "))

#

#create a python programme that is able to determine whether a person can donate blood based on the age and weight of a person.If the weight is greater that 50kg and age is above 18,then the person   can dolate ,else not possible. 
age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kg: "))

if age > 18 and weight > 50:
    print("You can donate blood.")
else:
    print("Blood donation not possible.")