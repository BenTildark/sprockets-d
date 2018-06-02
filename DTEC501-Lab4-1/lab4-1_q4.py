"""
Write a program which asks the user to enter their first and last name.

Your program must display the following message:
Please enter your first name:

The user will enter their <FirstName> at this point.

Your program must display the following message:
Please enter your last name:

The user will enter their <LastName> at this point.

The program should output

Hi <FirstName> <LastName>.

followed by the appropriate messages from the following:

Your first name starts with the letter A.

Your first name does not start with the letter A.

Your last name ends with the letter n.

Your last name does not end with the letter n.

depending on their first name starting with the letter A or not and their last name ending in the letter n or not.

Any messages displayed must be in the order they appear above.



Example


Please enter your first name: AndY
Please enter your last name: Johnson
Hi Andy Johnson.
Your first name starts with the letter A.
Your last name ends with the letter n.

# The lines of text you need to use to generate the output are given below for you.  Do not alter anything inside the quotes.
# "Please enter your first name: "
# "Please enter your last name: "
# "Hi {} {}."
# "Your first name starts with the letter {}."
# "Your first name does not start with the letter {}."
# "Your last name ends with the letter {}."
# "Your last name does not end with the letter {}."
"""

first_name = input("Please enter your first name: ").capitalize()
last_name = input("Please enter your last name: ").capitalize()
print("Hi {} {}.".format(first_name, last_name))

first_name_first_char = first_name[:1]
last_name_last_char = last_name[-1:]

if first_name_first_char == 'A':
    print("Your first name starts with the letter {}.".format('A'))
    if last_name_last_char == 'n':
        print("Your last name ends with the letter {}.".format('n'))
    elif last_name_last_char != 'n':
        print("Your last name does not end with the letter {}.".format('n'))
if first_name_first_char != 'A':
    print("Your first name does not start with the letter {}.".format('A'))
    if last_name_last_char == 'n':
        print("Your last name ends with the letter {}.".format('n'))
    elif last_name_last_char != 'n':
        print("Your last name does not end with the letter {}.".format('n'))
