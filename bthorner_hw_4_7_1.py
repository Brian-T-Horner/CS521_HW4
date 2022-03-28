"""
Brian Horner
CS 521 - Summer 1
Date: 6/1/2021
Homework Problem: 4_7_1
This program using list comprehension to find the sum of even and odd numbers
in a given list.
"""

# Establishing integer constant
INTEGER_INPUT = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List comprehension for odd and even evaluation

user_evens = []
user_odds = []
[user_evens.append(num) if num % 2 == 0 else user_odds.append(num) for num in
 INTEGER_INPUT]


# Below is an alternate way to do the list comprehension with two lists
# It allows you to not have to define the lists like previously

# user_evens = [num for num in INTEGER_INPUT if num % 2 == 0]
# user_odds = [num for num in INTEGER_INPUT if num % 2 == 1]

# Print statements with f strings and list comprehension for string from
# integer constant list
print(f"Evaluating the numbers in: "
      f"{', '.join([str(number) for number in INTEGER_INPUT])}")
print(f"Number of evens: {sum(user_evens)}")
print(f"Number of odds: {sum(user_odds)}")


