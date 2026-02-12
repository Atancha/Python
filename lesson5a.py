#PYTHON FUNCTIONS
#Function-are a block of code/statements that performs a given task/action
#They can be re-used throughout the programme different tasks
#Functions are defined using the 'def' standing for define
#We have two main types of functions:
#1.In built functions->they come preinstalled with the interpreter i.e. print(),pop(),range()
#2.User defined functions => They are created by a programmer to solve a given task.
#To define a function you need to give a need followed by parenthesis.
#For the functions,it is usually indented and to invoke a function we use the function name.

def greetings():
    print("Hello,how are you?")

#Below we call the function by use of its name
greetings()

print("==========================================")
#Addition function

def addition():
    num1 = 40
    num2 = 50
    sum = num1 + num2
    print("The sum of the numbers is:", sum)

addition()

print("====================================================")

#create a function that is able to multiply 3 values

def multiply():
    num1 = 5
    num2 = 8
    num3 = 15
    product = num1 * num2 * num3
    print("The product of the numbers is: ", product)


multiply()

print("============================================================")
#create a division function where the user get to input the value

def division():
    number1 = int(input("X: "))
    number2 = int(input("Y: "))
    quotient = number1 / number2
    print("The answer is: ", quotient)

division()

#creating a loop
for function in range(2):
    division
