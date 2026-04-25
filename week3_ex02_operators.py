# -------------------------------
# Question 1: Arithmetic and Assignment Operators

x = 10
y = 5

# Add 3 to x
x += 3

# Multiply y by 2
y *= 2

# Divide x by y
result = x / y

# Print result
print("Result:", result)


# -------------------------------
# Question 2: Comparison and Logical Operators

a = 10
b = 4
c = 8

# Conditions
condition1 = a > b
condition2 = b % 2 == 0
condition3 = c <= a

# Final condition
final_condition = condition1 or (condition2 and condition3)

# Print result
print("Final Condition:", final_condition)


# -------------------------------
# Question 3: Conditional Statements

score = int(input("Enter your test score (0-100): "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")


# -------------------------------
# Question 4: Combining Operators and Conditionals

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    print("Result:", num1 + num2)
elif operation == "-":
    print("Result:", num1 - num2)
elif operation == "*":
    print("Result:", num1 * num2)
elif operation == "/":
    if num2 == 0:
        print("Error: Cannot divide by zero")
    else:
        print("Result:", num1 / num2)
else:
    print("Invalid operation")