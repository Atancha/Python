
# Qn 1: Function Without Parameters
def rectangle_area():
    length = 10
    width = 5
    area = length * width
    print("Area of rectangle:", area)


# Qn 2: Function With Parameters
def calculate_operations(num1, num2):
    sum_result = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    
    if num2 != 0:
        division = num1 / num2
    else:
        division = "Cannot divide by zero"
    
    return sum_result, difference, product, division


# Qn 3: Control Statement (if...elif...else)
def check_number():
    number = float(input("Enter a number: "))
    
    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")


# Qn 4: Loop with Arithmetic
def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


# Qn 5: While Loop
def squares_using_while():
    number = int(input("Enter a number: "))
    i = 1
    while i <= number:
        print("Square of", i, "is", i * i)
        i += 1


# Function Calls (Example Usage)
rectangle_area()

results = calculate_operations(10, 5)
print("Sum:", results[0])
print("Difference:", results[1])
print("Product:", results[2])
print("Division:", results[3])

check_number()

print("Sum from 1 to n:", sum_to_n(5))

squares_using_while()

