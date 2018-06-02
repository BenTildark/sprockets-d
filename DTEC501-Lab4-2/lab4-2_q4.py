"""
Write a program which asks the user to enter their first name followed by three different integers.

The program needs to determine if any of the numbers are the same.

The program should display

Please enter your first name:

followed by

Hi <FirstName>, please enter the first number:

followed by

Thank you. Please enter the second number:

followed by

Thank you. Please enter the third number:

Treat all numbers as integers.

If any of the numbers are the same, display the message

Some of the numbers are the same.

If all of the numbers are different, display the message

All of the numbers are different.



You should test your program with different sets of numbers.

A short version of the code would use one if, two or's and one else.  Alternatively one if any and one else can be used.  The choice is yours.  If you can, try both.



Examples


Please enter your first name. different
Hi Different, please enter the first number: 1
Thank you. Please enter the second number: 2
Thank you. Please enter the third number: 3
All of the numbers are different.

Please enter your first name. same
Hi Same, please enter the first number: 1
Thank you. Please enter the second number: 1
Thank you. Please enter the third number: 1
Some of the numbers are the same.


"""

# The lines of text you need to use to generate the output are given below for you.  Do not alter anything inside the quotes.
# "Please enter your first name: "
# "Hi {}, please enter the first number: "
# "Thank you. Please enter the second number: "
# "Thank you. Please enter the third number: "
# "Some of the numbers are the same."
# "All of the numbers are different."

# This is a bad approach. There must be a better way! What if we had hundreds of comparisions?
first_name = input("Please enter your first name: ").capitalize()
first_int = int(input("Hi {}, please enter the first number: ".format(first_name)))
second_int = int(input("Thank you. Please enter the second number: "))
third_int = int(input("Thank you. Please enter the third number: "))

if any([first_int == second_int, first_int == third_int, second_int == first_int, second_int == third_int,
        third_int == first_int, third_int == second_int]):
    print("Some of the numbers are the same.")
else:
    print("All of the numbers are different.")