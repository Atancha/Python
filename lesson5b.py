# functions with parameters
#parameters->they are values that get past as arguments given to a function inside of the parenthesis  

def greeting(name):
    print(f"{name} How are you?Hope everything is fine.")

greeting("Johnson")
greeting("Maloba")

print("==============================")
def message():
    print("Hello,we shall be having a meeting on Friday evening,please avail yourself.")

for x in range(4):
    message()
    print(x)

print("=============================================")
#create a function that accepts parameters to  add two numbers
def addition(x,y):
    sum = x + y
    print("The sum of the numbers is: ", sum)

addition(45,79)
