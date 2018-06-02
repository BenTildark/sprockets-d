"""
Write a program which asks the user to enter their first name and outputs an appropriate message depending on their name starting with the letter A or not.

Your program must display the following message:
Please enter your first name:

The user will enter their <FirstName> at this point.

The program should then output one of the following messages:

Hi <FirstName>, your first name starts with the letter A.

or

Hi <FirstName>, your first name does not start with the letter A.

depending on their first name starting with the letter A (upper case A) or not.

Example

Please enter your first name: dave
Hi Dave, your first name does not start with the letter A.

Please enter your first name: andy
Hi Andy, your first name starts with the letter A.

# The lines of text you need to use to generate the output are given below for you.  Do not alter anything inside the quotes.
# "Please enter your first name: "
# "Hi {}, your first name starts with the letter {}."
# "Hi {}, your first name does not start with the letter {}."

"""
first_name = input("Please enter your first name: ").capitalize()
if first_name.startswith('A'):
    print("Hi {}, your first name starts with the letter {}.".format(first_name, 'A'))
else:
    print("Hi {}, your first name does not start with the letter {}.".format(first_name, 'A'))