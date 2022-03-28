"""
Brian Horner
CS 521 - Summer 1
Date: 6/1/2021
Homework Problem: 4_9_3
This program using zip to combine first and last names into a full name
dictionary.
"""

# Establishing first and last name constants
FIRST_NAMES = ['Jane', 'John', 'Jack']
LAST_NAMES = ['Doe', 'Deer', 'BLack']

# Checking to make sure there is an even number of first names and last names
if len(FIRST_NAMES) == len(LAST_NAMES):
    # Using zip to create full name dictionary with last names as keys and
    # first names as values
    full_name_dict = dict(zip(LAST_NAMES, FIRST_NAMES))
    # Exit with error message if lists sizes are different
else:
    print("Error: First and Last name lists are not the same length.")

# Printing out first names, last names and full name dictionary
print(f"First Names: {FIRST_NAMES}")
print(f"Last Names: {LAST_NAMES}")
print(f"Full Name Dictionary: {full_name_dict}")
