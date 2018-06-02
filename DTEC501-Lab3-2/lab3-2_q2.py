"""
Write a program to ask the user to enter their name and two integers where the second integer is greater than the first integer.

Your program must display the following message:
Please enter your first name:

The user enters their first name <FirstName> at this point.

Your program then displays the message:
Hi <FirstName>, please enter the first integer:

The user enters the first integer <FirstInteger> at this point.  Next, display the message:
Thank you. Please enter the second integer. This integer should be greater than <FirstInteger>:

The user enters the second integer <SecondInteger> at this point.

Your program must output the following:
It is <Answer> that <SecondInteger> is greater than <FirstInteger>.

where <Answer> has a boolean value of true or false based on <SecondInteger>  being greater than  <FirstInteger>

<FirstInteger> and <SecondInteger> are the respective integers the user entered.



Example


Please enter your first name: dave
Hi Dave, please enter the first integer: 5
Thank you. Please enter the second integer. This integer should be greater than 5: 6
It is True that 6 is greater than 5.

# The lines of text you need to use to generate the output are given below for you.  Do not alter anything inside the quotes.
# "Please enter your first name: "
# "Hi {}, please enter the first integer: "
# "Thank you. Please enter the second integer. This integer should be greater than {}: "
# "It is {} that {} is greater than {}."
"""

first_name = input("Please enter your first name: ").capitalize()
first_int = int(input("Hi {}, please enter the first integer: ".format(first_name)))
second_int = int(input("Thank you. Please enter the second integer. This integer should be greater than {}: ".format(first_int)))

bool = first_int < second_int

print("It is {} that {} is greater than {}.".format(bool, second_int, first_int))