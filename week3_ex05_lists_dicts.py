# Question 1: Creating and Modifying Lists

# TODO: Create a list of fruits
fruits = ["apple", "banana", "orange"]

# TODO: Add a fruit to the end of the list
fruits.append("grape")

# TODO: Insert a fruit at the beginning of the list
fruits.insert(0, "mango")

# TODO: Remove a fruit from the list
fruits.remove("banana")

# TODO: Print the modified list
print(fruits)


#-------------------------------------------------------------------------
# Question 2: List Operations

# TODO: Create a list of numbers from 1 to 5
numbers = [1, 2, 3, 4, 5]

# TODO: Create a new list with each number squared
squared = [n**2 for n in numbers]

# TODO: Find the sum and average of the original numbers
total = sum(numbers)
average = total / len(numbers)

# TODO: Print the results
print(f"Squared: {squared}")
print(f"Sum: {total}")
print(f"Average: {average}")


#-------------------------------------------------------------------------
# Question 3: Creating and Modifying Dictionaries

# TODO: Create a dictionary of countries and their capitals
countries = {"France": "Paris", "Japan": "Tokyo", "Germany": "Berlin"}

# TODO: Add a new country-capital pair
countries["Italy"] = "Rome"

# TODO: Update the capital of an existing country
countries["France"] = "Lyon"

# TODO: Remove a country-capital pair
countries.pop("Japan")

# TODO: Print the modified dictionary
print(countries)


#-------------------------------------------------------------------------
# Question 4: Dictionary Operations

# TODO: Create a dictionary of fruit colors
fruit_colors = {"apple": "red", "banana": "yellow", "grape": "purple"}

# TODO: Print all the fruits (keys)
print(fruit_colors.keys()) 

# TODO: Print all the colors (values)
print(fruit_colors.values())

# TODO: Print each fruit and its color
for fruit, color in fruit_colors.items():
    print(f"{fruit}: {color}")

# TODO: Check if a fruit is in the dictionary and print its color
if "apple" in fruit_colors:
    print(f"Apple is {fruit_colors['apple']}")