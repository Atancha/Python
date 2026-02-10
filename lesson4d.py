#python while loop
#while loop executes a block of code repeatedly as long as a certain condition is true.The syntax of a while loop in python is as follow:
"""
while keyword,
followed by the condition/statement to be evaluated,
followed by a full colon(:),
code to be printed out,
increment/decrement
"""
number = 0
while number < 5:
    print("Hello Moses",number)
    number = number + 1

print('========================================')
# Program to print even numbers from 50 to 70 using a while loop

number = 50

while number <= 70:
    print(number)
    number += 2
