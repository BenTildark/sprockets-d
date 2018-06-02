"""
Write a program which asks the user to enter their first name followed by a number and based the number being less than 10, display an appropriate message about the number.

Your program must display the following message:
Please enter your first name:

The user will enter their <FirstName> at this point.

The program should output the following message
Hi <FirstName>. Please enter an integer less than 10:

The user will enter an integer at this point.

The program should then test to see if <EnteredNumber> is less than 10 and display the appropriate message from the following:
<EnteredNumber> is less than 10.
<EnteredNumber> is not less than 10.


Examples

Please enter your first name: dave
Hi Dave. Please enter an integer less than 10: 5
5 is less than 10.

Please enter your first name: dave
Hi Dave. Please enter an integer less than 10: 50
50 is not less than 10.

# The lines of text you need to use to generate the output are given below for you.  Do not alter anything inside the quotes.
# "Please enter your first name: "
# "Hi {}. Please enter an integer less than {}: "
# "{} is less than {}."
# "{} is not less than {}."
"""

first_name = input("Please enter your first name: ").capitalize()

max_number = 10

input_number = int(input("Hi {}. Please enter an integer less than {}: ".format(first_name, max_number)))

if max_number > input_number:
    print("{} is less than {}.".format(input_number, max_number))
else:
    print("{} is not less than {}.".format(input_number, max_number))
