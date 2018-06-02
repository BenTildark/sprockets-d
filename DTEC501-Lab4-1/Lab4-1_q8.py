"""
Write a program which asks the user to enter their first name and a number and then display an appropriate message about the number.

Ask the user to enter their first name by displaying the message:

Please enter your first name:

The user will enter their <FirstName> at this point.

The program should then display the following:

<FirstName>, please enter an integer:

The user will enter <EnteredInteger> at this point.


The program should then test to see if EnteredInteger is less than 10, equal to 10 or greater than 10 and display the appropriate message from the following:

<EnteredInteger> is less than 10.

<EnteredInteger> is equal to 10.

<EnteredInteger> is greater than 10.



Examples


Please enter your first name: dave
Dave, please enter an integer: 5
5 is less than 10.

Please enter your first name: dave
Dave, please enter an integer: 20
20 is greater than 10.

"""

# The lines of text you need to use to generate the output are given below for you.  Do not alter anything inside the quotes.
# "Please enter your first name: "
# "{}, please enter an integer: "
# "{} is less than {}."
# "{} is equal to {}."
# "{} is greater than {}."
first_name = input("Please enter your first name: ").capitalize()
integer = int(input("{}, please enter an integer: ".format(first_name)))

ten = 10
less_than_10 = integer < 10
equal_to_10 = integer == 10
greater_than_10 = integer > 10

if less_than_10:
    print("{} is less than {}.".format(integer, ten))
elif equal_to_10:
    print("{} is equal to {}.".format(integer, ten))
else:
    print("{} is greater than {}.".format(integer, ten))