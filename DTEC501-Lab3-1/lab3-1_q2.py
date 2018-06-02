"""
Write a program to ask the user to enter two integers.
Your program must display the following messages

Please enter the first integer:

The user will enter the first integer at this point.
Please enter the second integer:

The user will enter the second integer at this point.

Multiply the first integer by the second integer display the following message:


The answer to FirstInteger * SecondInteger is Result


where FirstInteger and SecondInteger are the respective integers the user entered and Result is the product of the two integers.



Example


Please enter the first integer: 3
Please enter the second integer: 4
The answer to 3 * 4 is 12

"""

# The lines of text you need to use to generate the output are given below for you.  Do not alter anything inside the quotes.
# "Please enter the first integer: "
# "Please enter the second integer: "
# "The answer to {} * {} is {}"

first_addend = int(input("Please enter the first integer: "))
second_addend = int(input("Please enter the second integer: "))


def multiplication(first_arg, second_arg):
    answer = first_arg * second_arg
    result = "The answer to {} * {} is {}".format(first_arg, second_arg, answer)
    print(result)


multiplication(first_addend, second_addend)
