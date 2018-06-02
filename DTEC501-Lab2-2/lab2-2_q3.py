"""
Write a program which asks the user to enter an integer by displaying the following message:
Please enter an integer:
Using an augmented assignment statement, decrement the integer by one and display the following message:

The answer to EnteredInteger - 1 is Result

where EnteredInteger is the value the user entered and Result is decremented value.

Suppress the extra spaces added by the print function.


Example
Please enter an integer: 15
The answer to 15 - 1 is 14

# The lines of text you need to use to generate the output are given below for you.  Do not alter anything inside the quotes.
# "Please enter an integer: "
# "The answer to "
# " - 1 is "
"""
"""
DEINCREMENTING AN INTEGER & SUPPRESS extra WHITESPACE in STR'S within PRINT FUNCTION. tornado!
"""

first_addend = int(input("Please enter an integer: "))

def subtract_by_one(params_1, params_2):
    params_1-=1
    print("The answer to ".rstrip(), params_2, " - 1 is ".strip(), params_1, sep=" ", end="")

subtract_by_one(first_addend, first_addend)