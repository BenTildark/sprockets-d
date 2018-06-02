"""
You need to find a user whose first name starts with A and whose last name ends with n.

Write a program which asks the user to enter their first name.

Your program must display the following message:
Please enter your first name:

The user will enter their <FirstName> at this point.

If their first name starts with the letter A then do the following:
Ask them to enter their last name by displaying:

Hi <FirstName>. Please enter your last name:

The user will enter their <LastName> at this point.
If their last name ends with the letter n then display the following two messages:
Your first name starts with the letter A and your last name ends with the letter n.
Your names match the criteria.

If their last name does not end with the letter n then display the following message:
Sorry, your last name does not match the criteria.


If their first name does not start with the letter A then display the following message:
Sorry, your first name does not match the criteria.

Examples

Please enter your first name: anna
Hi Anna. Please enter your last name: Johnson
Your first name starts with the letter A and your last name ends with the letter n.
Your names match the criteria.

Please enter your first name: John
Sorry John, your first name does not match the criteria.

Please enter your first name: anna
Hi Anna. Please enter your last name: smith
Sorry Anna, your last name does not match the criteria.

# The lines of text you need to use to generate the output are given below for you.  Do not alter anything inside the quotes.
# "Please enter your first name: "
# "Hi {}. Please enter your last name: "
# "Your first name starts with the letter {} and your last name ends with the letter {}."
# "Your names match the criteria."
# "Sorry {}, your last name does not match the criteria."
# "Sorry {}, your first name does not match the criteria."
"""
first_name_first_char = 'A'
last_name_last_char = 'n'

first_name = input("Please enter your first name: ").capitalize()

if first_name.startswith(first_name_first_char):
    last_name = input("Hi {}. Please enter your last name: ".format(first_name))
    if last_name.endswith(last_name_last_char):
        print("Your first name starts with the letter {} and your last name ends with the letter {}."
              .format(first_name_first_char, last_name_last_char))
        print("Your names match the criteria.")
    else:
        print("Sorry {}, your last name does not match the criteria.".format(first_name))
else:
    print("Sorry {}, your first name does not match the criteria.".format(first_name))






