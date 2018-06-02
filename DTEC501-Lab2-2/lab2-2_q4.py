"""
Write a program which asks the user to enter an integer by displaying the following message:

Please enter an integer:
Using an augmented assignment statement, multiply the integer by five and display the following message:

The answer to EnteredInteger * 5 is Result

where EnteredInteger is the value the user entered and Result is EnteredInteger * 5.

Suppress the extra spaces added by the print function.


Example
Please enter an integer: 2
The answer to 2 * 5 is 10

# The lines of text you need to use to generate the output are given below for you.  Do not alter anything inside the quotes.
# "Please enter an integer: "
# "The answer to "
# " * 5 is "
"""
"""
MULTIPY an INTEGER by FIVE(Using an augmented assignment statement) & SUPPRESS extra WHITESPACE in STR'S within PRINT FUNCTION.
"""

first_addend = int(input("Please enter an integer: "))

def multiply_by_five(params_1, params_2):
    params_1*=5
    print("The answer to ".rstrip(), params_2, " * 1 is ".strip(), params_1, sep=" ", end="")

multiply_by_five(first_addend, first_addend)