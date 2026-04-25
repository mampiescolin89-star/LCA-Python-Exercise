# LCA-Python-Exercise
# Question 1: Variable Assignment and String Manipulation

# Ask user for name
name = input("Enter your name: ")

# Ask user for age
age = input("Enter your age: ")

# Print greeting
print("Hello " + name + "! You are " + age + " years old.")


#------------------------------------------------------------------------------------
# Question 2: Integer Operations

# Ask for length
length = int(input("Enter the length of the rectangle: "))

# Ask for width
width = int(input("Enter the width of the rectangle: "))

# Calculate area
area = length * width

# Print result
print("The area of the rectangle is:", area)


#------------------------------------------------------------------------------------
# Question 3: Working with Floats

# Ask for temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Convert to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Print result rounded to 2 decimal places
print("Temperature in Fahrenheit is:", round(fahrenheit, 2))


#------------------------------------------------------------------------------------
# Extra examples (given in question)

# if else example
num = 10
if num > 0:
    print("Positive number")
else:
    print("Negative number or zero")


# elif example
height = 175
if height < 150:
    print("Short")
elif height < 180:
    print("Average height")
else:
    print("Tall")


# nested if example
age = 25
if age >= 18:
    if age < 65:
        print("Adult")
    else:
        print("Senior")
else:
    print("Minor")+