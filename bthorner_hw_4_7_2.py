"""
Brian Horner
CS 521 - Summer 1
Date: 6/1/2021
Homework Problem: 4_7_2
This program take a constant list of integers and generates a new list with
the same number of elements such that each integer is the sum of its nearest
neighbors
"""

# Establishing integer list and result list
INPUT_LIST = [10, 20, 30, 40, 50]
result_list = []

# For enumerating through input list to get index and value
for index, value in enumerate(INPUT_LIST):
    # Calculations if value is not the first item in the list
    if index != 0:
        calc_list = INPUT_LIST[index-1:index+2]
        result_list.append(sum(calc_list))
    # Calculation if value is the first item in the list
    else:
        calc_list = INPUT_LIST[index:index+2]
        result_list.append(sum(calc_list))

# F string print statements
print(f"Input List: {INPUT_LIST}")
print(f"Result List: {result_list}")
