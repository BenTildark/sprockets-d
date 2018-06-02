"""
Write a program to ask the user to enter their first name.
Your program must display the following message:

Please enter your first name:

Your program must output the following:

Hi EnteredFirstName.
Please enter the first integer:

and once they have entered it, display the following message:

Please enter the second integer:

Divide the first integer by the second integer display the following message:

EnteredFirstName, the answer to FirstInteger divided by SecondInteger is Floor with a remainder of Remainder

where

EnteredFirstName is the users first name
FirstInteger and SecondInteger are the respective integers the user entered.
Floor is the floor division value of the two integers.
Remainder is the modulus value of the two integers.
.

Example

Please enter your first name: Steve
Hi Steve.
Please enter the first integer: 17
Please enter the second integer: 5
Steve, the answer to 17 divided by 5 is 3 with a remainder of 2

# The lines of text you need to use to generate the output are given below for you.  Do not alter anything inside the quotes.
# "Please enter your first name: "
# "Hi "
# "."
# "Please enter the first integer: "
# "Please enter the second integer: "
# ", the answer to "
# " divided by "
# " is "
# " with a remainder of "
"""

"""
Multi-line, Same-line Output division. DIVISION /% MODULUS
"""

first_name = input("Please enter your first name: ").capitalize()
print("Hi ", first_name, ".", sep="", end="\n")

first_addend = int(input("Please enter the first integer: "))
second_addend = int(input("Please enter the second integer: "))

answer = first_addend / second_addend
print(first_name, ", the answer to ", first_addend, " divided by ", second_addend, " is ", answer, sep="", end="")

