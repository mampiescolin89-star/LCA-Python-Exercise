5# Question 1
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)


# Question 2
count = 5
while count > 0:
    print(count)
    count -= 1


# Question 3
for i in range(1, 11):
    print(i * i)


# Question 4
import random

colors = ["red", "blue", "green", "yellow"]

for i in range(3):
    print(random.choice(colors))


# Question 5 (PART 1 - module)
# YOU MUST CREATE A NEW FILE for this part (see below)

import math_operations

# Question 5 (PART 2 - calculator)
while True:
    num1 = float(input("Enter first number: "))
    op = input("Enter +, -, *, /: ")
    num2 = float(input("Enter second number: "))

    if op == "+":
        print(math_operations.add(num1, num2))
    elif op == "-":
        print(math_operations.subtract(num1, num2))
    elif op == "*":
        print(math_operations.multiply(num1, num2))
    elif op == "/":
        print(math_operations.divide(num1, num2))
    else:
        print("Invalid operator")

    again = input("Again? (y/n): ")
    if again != "y":
        break