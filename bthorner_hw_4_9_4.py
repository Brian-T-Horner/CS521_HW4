"""
Brian Horner
CS 521 - Summer 1
Date: 6/1/2021
Homework Problem: 4_9_4
This program takes a dictionary and prints the keys, values, key value pairs,
key value pairs ordered by key, and key value pairs ordered by value.
"""

# Establishing the dictionary constant
MY_DICT = {'a': 15, 'c': 18, 'b': 20}

# Sorting my key
key_sorted = {key: MY_DICT[key] for key in sorted(MY_DICT)}
# Sorting by value using lambda to control
value_first = {key: value for key, value in sorted(MY_DICT.items(),
                                                   key=lambda item: item[1])}

# Printing keys, values, key-value pairs in standard form, ascending order by
# key, and ascending order by value
print(f"Keys: {list(MY_DICT.keys())}")
print(f"Values: {', '.join([str(value) for value in MY_DICT.values()])}")
print(f"Key value pairs: {MY_DICT}")
print(f"Key value pairs ordered by key: {key_sorted}")
print(f"Key value pairs ordered by value: {value_first}")
