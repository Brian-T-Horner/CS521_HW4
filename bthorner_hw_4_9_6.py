"""
Brian Horner
CS 521 - Summer 1
Date: 6/1/2021
Homework Problem: 4_9_6
This program takes a user inputted number and converts it to a written out
number
"""


def number_written_out(user_input, number_dictionary):
    """This number takes a string from the user and converts it to a written
    out number"""
    # Establishing the loop
    while True:
        # Try and except clauses for KeyError and ValueError
        try:
            # Iterating through user_input
            for word in user_input:
                # Checking for duplicate decimals or negative signs
                if user_input.count('.') > 1 or user_input.count('-') > 1:
                    print("Error: More than one decimal or negative detected.")
                    # Printing error statement and re-prompting user
                    user_input = input("Enter a numeric number: ")
                    continue
                else:
                    # List comprehension to iterate through user_input to list
                    word_list = [word for word in user_input]
                    # Grabbing value from number dictionary for item in list
                    output = [number_dictionary[value] for value in word_list]
                    # Joining all output elements into a string
                    output_string = ' '.join([str(word) for word in output])
                    print(f"You entered the number {user_input}")
                    return output_string
            break
            # General error messages and re-prompts for KeyError and ValueError
        except ValueError:
            print("Error please enter a valid number with only numeric numbers and "
                  "decimal places.")
            user_input = input("Enter a numeric number: ")
        except KeyError:
            print("Error please enter a valid number with only numeric numbers and "
                  "decimal places.")
            user_input = input("Enter a numeric number: ")


if __name__ == '__main__':
    # Making sure this module was not imported
    # Establishing number dict and output list
    number_dict = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five',
                   '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine',
                   '.': 'Point', '-': 'Negative', '0': 'Zero'}
    # Prompting user
    user_input_str = input("Enter a numeric number: ")
    # Printing return of function
    print(f"Your number written out in words is: "
          f"{number_written_out(user_input_str, number_dict)}")
else:
    print("Error: This should not happen if you have not inported this module.")
