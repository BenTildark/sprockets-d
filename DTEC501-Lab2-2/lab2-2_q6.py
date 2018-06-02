"""
Write a program to ask the user to enter their first name.
Your program must display the following message;
Please enter your first name:


Your program must output the following:
Please enter the first integer:


and once they have entered it, display the following message:
Please enter the second integer:

The user enters the second integer at this point.
Multiply the first integer by the second integer display the following message:


EnteredFirstName, the answer to FirstInteger * SecondInteger is Result


where EnteredFirstName is the users first name and FirstInteger and SecondInteger are the respective integers the user entered.
Result is the product of the two integers.

Suppress the extra spaces added by the print function.



Example


Please enter your first name: Dave
Please enter the first integer: 5
Please enter the second integer: 4
Dave, the answer to 5 * 4 is 20

# The lines of text you need to use to generate the output are given below for you.  Do not alter anything inside the quotes.
# "Please enter your first name: "
# "Please enter the first integer: "
# "Please enter the second integer: "
# ", the answer to "
# " * "
# " is "
"""

"""
MULTIPLICATION & SUPPRESS extra WHITESPACE in STR'S within PRINT FUNCTION.
"""
first_name = input("Please enter your first name: ").capitalize()
first_addend = int(input("Please enter the first integer: "))
second_addend = int(input("Please enter the second integer: "))

def multiplication(arg_f, arg_s, arg_t): # first second & third args
    sum = arg_s * arg_t
    print(arg_f, ", the answer to ", arg_s, " * ".rstrip(), " is ", sum, sep="", end="")

multiplication(first_name, first_addend, second_addend)
