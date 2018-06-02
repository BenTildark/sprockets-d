"""
Write a program which asks the user to enter their first name.

Your program must display the following message:
Please enter your first name:

The user will enter their <FirstName> at this point.

The program should then output the message:

Hi <FirstName>.

followed by the appropriate message(s) from the following:

Your first name starts with the letter A.

Your first name does not start with the letter A.

Your first name ends with the letter y.

Your first name does not end with the letter y.

depending on their first name starting with the letter A or not and ending in the letter y or not.


Example

Please enter your first name: andy
Hi Andy.
Your first name starts with the letter A.
Your first name ends with the letter y.



Please enter your first name: noah
Hi Noah.
Your first name does not start with the letter A.
Your first name does not end with the letter y.

# The lines of text you need to use to generate the output are given below for you.  Do not alter anything inside the quotes.
# "Please enter your first name: "
# "Hi {}."
# "Your first name starts with the letter {}."
# "Your first name does not start with the letter {}."
# "Your first name ends with the letter {}."
# "Your first name does not end with the letter {}."
"""

first_name = input("Please enter your first name: ").capitalize()
print("Hi {}.".format(first_name))

first_char = first_name[:1]
last_char = first_name[-1:]

if first_char == 'A':
    print("Your first name starts with the letter {}.".format('A'))
    if last_char == 'y':
        print("Your first name ends with the letter {}.".format('y'))
    elif last_char != 'y':
        print("Your first name does not end with the letter {}.".format('y'))
if first_char != 'A':
    print("Your first name does not start with the letter {}.".format('A'))
    if last_char == 'y':
        print("Your first name ends with the letter {}.".format('y'))
    elif last_char != 'y':
        print("Your first name does not end with the letter {}.".format('y'))












