"""
Write a program to ask the user to enter their first/given name.

Your program must display the following message:

Please enter your first name:

Then output the following:


Hi EnteredFirstName, please enter the first integer:

and once the user has entered the integer, display the following message:


Please enter the second integer:

Divide the first integer by the second integer display the following message:

EnteredFirstName, the answer to FirstInteger floor divided by SecondInteger is Result with a remainder of Remainder


where EnteredFirstName is the users first name and FirstInteger and SecondInteger are the respective integers the user entered.
Result is the floored division value of the two integers.
Remainder is the modulus value of the two integers.



Example


Please enter your first name: Harry
Hi Harry, please enter the first integer: 30
Please enter the second integer: 4
Harry, the answer to 30 floor divided by 4 is 7 with a remainder of 2.

"""

# The lines of text you need to use to generate the output are given below for you.  Do not alter anything inside the quotes.
# "Please enter your first name: "
# "Hi {}, please enter the first integer: "
# "Please enter the second integer: "
# "{}, the answer to {} floor divided by {} is {} with a remainder of {}."

first_name = input("Please enter your first name: ")
first_addend = int(input("Hi {}, please enter the first integer: ".format(first_name)))
second_addend = int(input("Please enter the second integer: "))


def equation(first_arg, second_arg, third_arg):
    answer = second_arg // third_arg
    modulus = second_arg % third_arg
    result = "{}, the answer to {} floor divided by {} is {} with a remainder of {}.".format(first_arg, second_arg, third_arg, answer, modulus)
    print(result)


equation(first_name, first_addend, second_addend)