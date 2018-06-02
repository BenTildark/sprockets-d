"""
Write a program which asks the user to enter their first name and two numbers.  The program will then display the relationship between the two numbers.

The program should display the message

Please enter your first name:

followed by

Hi <FirstName>, please enter the first number:

followed by

Thank you. Please enter the second number:

Based on the numbers that were entered, using the most efficient conditional statement(s), display the appropriate message from the following:

<FirstNumber> is greater than <SecondNumber>

<FirstNumber> is less than <SecondNumber>

<FirstNumber> is equal to <SecondNumber>



An ideal solution uses one if, one elif and one else.

Example


Please enter your first name: dave
Hi Dave, please enter the first number: 5
Thank you. Please enter the second number: 2
5 is greater than 2

"""

# The lines of text you need to use to generate the output are given below for you.  Do not alter anything inside the quotes.
# "Please enter your first name: "
# "Hi {}, please enter the first number: "
# "Thank you. Please enter the second number: "
# "{} is greater than {}"
# "{} is equal to {}"
# "{} is less than {}"

first_name = input("Please enter your first name: ").capitalize()

first_number = int(input("Hi {}, please enter the first number: ".format(first_name)))

second_number = int(input("Thank you. Please enter the second number: "))

if first_number > second_number:
    print("{} is greater than {}".format(first_number, second_number))
elif first_number == second_number:
    print("{} is equal to {}".format(first_number, second_number))
else:
    print("{} is less than {}".format(first_number, second_number))
