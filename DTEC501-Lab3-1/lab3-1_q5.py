"""
Write a program to ask the user to enter their first name.
Your program must display the following message:

Please enter your first name:

Your program must then ask the user to enter their last name as follows:

Please enter your last name:



Concatenate the names using a variable called full_name and display the following message:


Pleased to meet you FullName, welcome to CourseCode.

Where FullName is the value of an appropriately named variable which contains the concatenated values of the first and last name the user entered.

FullName must be correctly capitalised.

FullName must be correctly spaced.

CourseCode is the value of an appropriately named variable which has been assigned the value "DTEC501".



Example


Please enter your first name: Dave
Please enter your last name: Bracken
Pleased to meet you Dave Bracken, welcome to DTEC501.


"""

# The lines of text you need to use to generate the output are given below for you.  Do not alter anything inside the quotes.
# "Please enter your first name: "
# "Please enter your last name: "
# "Pleased to meet you {}, welcome to {}."

first_name = input("Please enter your first name: ").capitalize()
second_name = input("Please enter your last name: ").capitalize()


def greeting(first_arg, second_arg):
    full_name = "{} {}".format(first_arg, second_arg)
    components = "Pleased to meet you {}, welcome to {}.".format(full_name, "DTEC501")
    print(components)


greeting(first_name, second_name)
