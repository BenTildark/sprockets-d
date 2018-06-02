"""
Write a program which asks the user to enter their first name and outputs an appropriate message depending on their name ending with the letter n or not.

Your program must display the following message:
Please enter your first name:

The user will enter their <FirstName> at this point.


The program should output one of the following messages:
Hi <FirstName>, your first name ends with the letter n.
or
Hi <FirstName>, your first name does not end with the letter n.
depending on their first name ending with the letter n or not.



Example


Please enter your first name: anna
Hi Anna, your first name does not end with the letter n.

Please enter your first name: John
Hi John, your first name ends with the letter n.

# The lines of text you need to use to generate the output are given below for you.  Do not alter anything inside the quotes.
# "Please enter your first name: "
# "Hi {}, your first name ends with the letter {}."
# "Hi {}, your first name does not end with the letter {}."
"""

first_name = input("Please enter your first name: ").capitalize()
if first_name.endswith('n'):
    print("Hi {}, your first name ends with the letter {}.".format(first_name, 'n'))
else:
    print("Hi {}, your first name does not end with the letter {}.".format(first_name, 'n'))