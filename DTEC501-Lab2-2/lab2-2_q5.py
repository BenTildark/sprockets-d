"""
Write a program to ask the user to enter two integers.

Your program must display the following message:
Please enter the first integer:

The user will enter the first integer at this point.  Then display the following message:
Please enter the second integer:

The user will enter the second integer at this point.

Multiply the first integer by the second integer display the following message:

The answer to FirstInteger * SecondInteger is Result

where FirstInteger and SecondInteger are the respective integers the user entered.

Suppress the extra spaces added by the print function.

Example

Please enter the first integer: 2
Please enter the second integer: 3
The answer to 2 * 3 is 6

# The lines of text you need to use to generate the output are given below for you.  Do not alter anything inside the quotes.
# "Please enter the first integer: "
# "Please enter the second integer: "
# "The answer to "
# " * "
# " is "
"""
"""
MULTIPLICATION & SUPPRESS extra WHITESPACE in STR'S within PRINT FUNCTION.
"""

first_addend = int(input("Please enter the first integer: "))
second_addend = int(input("Please enter the second integer: "))

def multiplication(arg_f, arg_s): # first & second args
    sum = arg_f * arg_s
    print("The answer to ".rstrip(), arg_f, " * ".strip(), arg_s, " is ".strip(), sum, sep=" ", end="")

multiplication(first_addend, second_addend)