"""
Brian Horner
CS 521 - Summer 1
Date: 6/1/2021
Homework Problem: 4_9_5
This program takes a string and gives a dictionary with the letters as keys
and their frequency as values, finds the most common letters and returns them
 with their counts, and prints each letter times their frequency in a histogram.
"""


def add_word(word, word_dict):
    """ This function takes a string and a dictionary as its arguments. It
    adds 1 to the value if the word exists as a key. If it does not exist it
    adds the word as a key with the frequency of one."""
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1


def letters_or_letter(count_list):
    """ This function takes a list and determines if letter or letters should
    be used sentence context wise"""
    for i in count_list:
        count = count_list.count(i)
        if count > 1:
            return "letters"
        else:
            return "letters"
# Could have maybe been included in most_common_letters function


def letter_counts(input_str):
    """ This function takes a string and returns a dictionary of the letters
    as keys and the frequency as values. Uses add_word func to add words to
    dictionary"""
    word_count_dict = {}
    # Stripping the input sentence and adding word to word list if it isalpha
    word_count_list = [word for word in input_str.strip() if word.isalpha()]
    # Making the words uniform and using the add_word function
    for word in word_count_list:
        word = word.upper()
        add_word(word, word_count_dict)
    return word_count_dict


def most_common_letter(input_str):
    """" This function takes a string and returns a string of the most common
    letters."""
    # Assigning result of letter_counts function
    common_letter_dict = letter_counts(input_str)
    # Adding word to list if the value is the max in the dictionary
    # This will add multiple words if their values are the same
    max_str_list = [(key, value) for (key, value) in
                    common_letter_dict.items()\
                    if value == max(common_letter_dict.values())]
    # Joining the letters in a pretty string
    most_common_letters = ", ".join(str(word) for word, value in max_str_list)
    # Assigning max value of dictionary to variable for printing
    count_most_common_letters = str(max(common_letter_dict.values()))
    # F string for return. Soooo nice to use.
    return f"{most_common_letters} appeared {count_most_common_letters} times."



def string_count_histogram(input_str):
    """ This function takes a string and returns a list of unique letters
    with the letters repeating each time they appear in the string when
    printed."""
    output = ""
    # Assigning result of letter_counts function
    output_dict = letter_counts(input_str)
    # Iterating over keys and multiplying the string by its value
    for key in output_dict.keys():
        count = output_dict[key]
        # Added a line break here to make the histogram
        output += (key * count) + "\n"
    return output

def pretty_print(user_str):
    """ This function takes the inputs of all functions and cleans them up
    for clean print statements. I did this to clean up the code"""
    print(f"The string being analyzed is: {user_input}")
    print(f"1. Dictionary of letter counts: {letter_counts(user_input)}")
    print("2. Most frequent {}: {}".format(letters_or_letter(
        most_common_letter(user_input)), most_common_letter(user_input)))
    print(f"3. Histogram of letters: \n{string_count_histogram(user_input)} ")

# Making sure the file has not been imported, else an error statement prints.

if __name__ == '__main__':
    """Assigning string to user_input. I believe I could take an input without
    any errors due to the .iaslpha check"""
    user_input = """Hello my name is Brian. I absolutely adore Python! I am 
so happy to be finished this problem. I am honestly super happy with my 
work, it is clean, and functional! (I think.)"""

    pretty_print(user_input)

else:
    print("Error: Why did you import this? Consult the developer for "
          "clarification.")

# Original print statements below
#     print(f"The string being analyzed is: {user_input}")
#     print(f"1. Dictionary of letter counts: {letter_counts(user_input)}")
#     print("2. Most frequent {}: {}".format(letters_or_letter(
#         most_common_letter(user_input)), most_common_letter(user_input)))
#     print(f"3. Histogram of letters: \n{string_count_histogram(user_input)} ")
