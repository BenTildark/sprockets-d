"""
Write a program which asks the user to enter an integer by displaying the following message:



Please enter an integer:



Using an augmented assignment statement, increment the integer by one and display the following message:


The answer to EnteredInteger + 1 is Result



where EnteredInteger is the value the user entered and Result is incremented value.

Suppress the extra spaces added by the print function.

Example
Please enter an integer: 15
The answer to 15 + 1 is 16

# The lines of text you need to use to generate the output are given below for you.  Do not alter anything inside the quotes.
# "Please enter an integer: "
# "The answer to "
# " + 1 is "
"""
"""
INCREMENTING AN INTEGER & SUPPRESS extra WHITESPACE in STR'S within PRINT FUNCTION. django!
"""

first_addend = int(input("Please enter an integer: "))

def incrementation(first_arg, second_arg):
    first_arg+=1
    print("The answer to ".rstrip(), first_arg, " + 1 is ".strip(), second_arg, sep=" ", end="" )

incrementation(first_addend, first_addend)