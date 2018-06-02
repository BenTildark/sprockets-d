"""
Write a program which asks the user to enter their first name followed by three different integers.

If the entered integers are different then the program will display the smallest of the numbers.

The program should display

Please enter your first name:

followed by

Hi <FirstName>, please enter the first number:

followed by

Thank you. Please enter the second number:

followed by

Thank you. Please enter the third number:

Using conditional statements, work out if all the numbers are the different. If all the numbers are the different, work out which is the smallest number that was entered and then display the following message:

Thank you <FirstName>, <FirstNumber>, <SecondNumber>, <ThirdNumber> are all different and <Smallest> is the smallest of them.

If any of the numbers were the same, display the message

Sorry <FirstName>, some of the numbers are the same.



Use the code you wrote for Q5 as the basis for this question.

Use if elif, else and or for this question.





Examples


Please enter your first name: same
Hi Same, please enter the first number: 1
Thank you. Please enter the second number: 1
Thank you. Please enter the third number: 1
Sorry Same, some of the numbers are the same.

Please enter your first name: different
Hi Different, please enter the first number: 3
Thank you. Please enter the second number: 9
Thank you. Please enter the third number: 6
Thank you Different, 3, 9, 6 are all different and 3 is the smallest of them.

"""

# The lines of text you need to use to generate the output are given below for you.  Do not alter anything inside the quotes.
# "Please enter your first name: "
# "Hi {}, please enter the first number: "
# "Thank you. Please enter the second number: "
# "Thank you. Please enter the third number: "
# "Sorry {}, some of the numbers are the same."
# "Thank you {}, {}, {}, {} are all different and {} is the smallest of them."

first_name = input("Please enter your first name: ").capitalize()
first_int = int(input("Hi {}, please enter the first number: ".format(first_name)))
second_int = int(input("Thank you. Please enter the second number: "))
third_int = int(input("Thank you. Please enter the third number: "))

if all([first_int != second_int, first_int != third_int, second_int != first_int, second_int != third_int,
        third_int != first_int, third_int != second_int]):
    # This seemed the best approach with my current skill set..
    # Get the smallest number
    entered_integers = [first_int, second_int, third_int]  # create a list object
    min_value = min(entered_integers)  # return the smallest of the iterable list.
    # Find a ton of these bad guys @ docs.python.org/library/functions.html ;-)
    print("Thank you {}, {}, {}, {} are all different and {} is the smallest of them.".format(first_name, first_int,
                                                                                              second_int, third_int,
                                                                                              min_value))
else:
    print("Sorry {}, some of the numbers are the same.".format(first_name))
