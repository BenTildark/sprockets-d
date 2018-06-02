"""
Write a program which asks the user to enter their first name followed by their age and then display if their age is odd or even.

The program should display

Please enter your first name:

followed by

Hi <FirstName>, please enter your age in years:

Assume only integers will be entered.

Work out if their age is an odd or even number and display the appropriate message from below:

<FirstName>, <Age> is an odd number of years.

<FirstName>, <Age> is an even number of years.



An ideal solution uses one if and one else.



Examples


Please enter your first name: dave
Hi Dave, please enter your age in years: 42
Dave, 42 is an even number of years.

Please enter your first name: dave
Hi Dave, please enter your age in years: 41
Dave, 41 is an odd number of years.


"""

# The lines of text you need to use to generate the output are given below for you.  Do not alter anything inside the quotes.
# "Please enter your first name: "
# "Hi {}, please enter your age in years: "
# "{}, {} is an odd number of years."
# "{}, {} is an even number of years."

first_name = input("Please enter your first name: ").capitalize()

age = int(input("Hi {}, please enter your age in years: ".format(first_name)))

two = 2
odd = bool(age % two)
if odd:
    print("{}, {} is an odd number of years.".format(first_name, age))
else:
    print("{}, {} is an even number of years.".format(first_name, age))
