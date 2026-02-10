#Boolean - This is a data type that evaluates either true or false 

isRaining = False
print(isRaining)
print(type(isRaining))

paidloan = True
print(paidloan)

# comparison operators: They are used to compare two or more statement and they usually return a boolean answer

number1 = 2
number2 = 5

print("is number one greater than number two?", number1 > number2)
print("is number one less than number two?", number1 < number2)
print("is number one greater than or equal to number two?", number1 >= number2)
print("is number one less thanor equal to number two?", number1 <= number2)
print("is number one equal to  number two?", number1 == number2)

#Logical operators
#Logical AND 
#It returns true if and only if the condition/statement evaluates to true
print(3 > 1) and (7 > 6)

#Logical or
#It evaluates to true if one the statements/conditions is true
print((3 > 1) or (7 < 6))

#Logical not
#It is used to negate a statement/condition
print(not(90 > 70))