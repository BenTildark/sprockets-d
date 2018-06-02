"""
Write a program to ask the user to enter their name and two different integers.

Your program must display the following message:
Please enter your first name:

The user enters their first name <FirstName> at this point.

Then display the message:
Hi <FirstName>, please enter the first integer:

The user enters the first integer <FirstInteger> at this point.  Next, display:
Thank you. Please enter the second integer. This integer should not be equal to <FirstInteger>:

The user enters the second integer <SecondInteger> at this point.

Your program must output the following:
It is <Answer> that <SecondInteger> is not equal to <FirstInteger>.

where <Answer> has a boolean value of true or false based on <SecondInteger>  being not equal to  <FirstInteger>

<FirstInteger> and <SecondInteger> are the respective integers the user entered.



Example


Please enter your first name: dave
Hi Dave, please enter the first integer: 1
Thank you. Please enter the second integer. This integer should not be equal to 1: 0
It is True that 0 is not equal to 1.

# The lines of text you need to use to generate the output are given below for you.  Do not alter anything inside the quotes.
# "Please enter your first name: "
# "Hi {}, please enter the first integer: "
# "Thank you. Please enter the second integer. This integer should not be equal to {}: "
# "It is {} that {} is not equal to {}."
"""

first_name = input("Please enter your first name: ").capitalize()
first_int = int(input("Hi {}, please enter the first integer: ".format(first_name)))
second_int = int(input("Thank you. Please enter the second integer. This integer should not be equal to {}: ".format(first_int)))

bool = first_int != second_int

print("It is {} that {} is not equal to {}.".format(bool, second_int, first_int))