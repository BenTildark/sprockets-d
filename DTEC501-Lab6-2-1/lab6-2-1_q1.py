"""
Specification
The following code is supposed to do the following:

Validate the users first name.
Validate the users last name.
Validate their assessment mark.
Once all the data is valid, print a pass or a fail message.
A valid first name is one containing only alphabetic characters and 2 or more characters in length.
If the entered first name is not valid, inform the user and then ask them to enter it (again).

A valid last name is one containing only alphabetic characters and 2 or more characters in length.
If the entered last name is not valid, inform the user and then ask them to enter it (again).

Valid marks are integers between 0 and 10 inclusively.
If the entered mark is not an integer, inform the user and then ask them to enter it (again).
If the entered mark is out of range, inform the user and then ask them to enter it (again).

A Pass mark is between 5-10 inclusively.
A Fail mark is between 0 and 4 inclusively.

Inform the user if they have passed or not passed the assessment.

Copy the code below into the IDE.

There are mistakes in the code.
Leave the text inside the quotes for the print and input lines as they are.
Use debugging techniques to correct the code.

Hints.
Notice the spacing in the bullet points above.  Only 3 while loops are needed. There are no nested loops.
The first while loop validates the first name
The second while loop validates the last name
The first two loops are *very* similar

The third while loop validates the assessment mark
Don't assume the user will enter a numeric value for an assessment mark. See the last example.

Once you have exited from the third loop, then work out if the user has passed or failed.

Examples:

Not passing with the minimum assessment mark of 0
Please enter your first name: Not
Please enter your last name: Passed
Enter your assessment mark: 0
Sorry Not, you have not passed the assessment.

Just passing with the minimum pass marks of 5
Please enter your first name: Not
Please enter your last name: Passed
Enter your assessment mark: 0
Sorry Not, you have not passed the assessment.

Passing with the highest valid mark of 10
Please enter your first name: Well
Please enter your last name: Passed
Enter your assessment mark: 10
Well done Well Passed, you have passed the assessment.

The first and last names are too short and therefore they do not meet the minimum requirements and so need to be re-entered.
It took 4 attempts before the assessment mark was entered correctly.
Please enter your first name: T
Invalid first name.
Please enter your first name: Too
Please enter your last name: S
Invalid last name.
Please enter your last name: Short
Enter your assessment mark: -10
The entered mark was not a positive number.
Enter your assessment mark: Eleven
The entered mark was not a positive number.
Enter your assessment mark: 11
The entered mark was too high.
Enter your assessment mark: 9
Well done Too Short, you have passed the assessment.

The Code Riddle:

lowest_mark = 0
highest_mark = 10
passing_mark = 5
problem = True
while problem:
    n1 = input("Please enter your first name: ").capitalize()
    if len(n1) >= 2:
        problem = False
    else:
        print("Invalid first name.")
problem = True
while problem:
    n2 = input("Please enter your last name: ").capitalize()
    if len(n2) >= 2:
        problem = False
    else:
        print("Invalid last name.")
while problem:
    x = input("Enter your assessment mark: ")
    x=int(x)
    if x < 0 or x > 10
        print("The entered mark was too high.")
        print("The entered mark was not a positive number.")
    problem = False
if x > lowest_mark:
    print("Sorry {}, you have not passed the assessment.".format(n1))
if x < passing_mark:
    print("Well done {} {}, you have passed the assessment.".format(n1, n2))

"""
# Auth: Michael Devenport.
# Email: croxleyway@gmail.com

# Code

valid_mark = range(0, 11)
pass_mark = range(5, 11)

highest_mark = 10


problem = True
while problem:
    first_name = input("Please enter your first name: ").capitalize()
    if all([len(first_name) >= 2, first_name.isalpha()]):
        problem = False
    else:
        print("Invalid first name.")
problem = True
while problem:
    last_name = input("Please enter your last name: ").capitalize()
    if all([len(last_name) >= 2, last_name.isalpha()]):
        problem = False
    else:
        print("Invalid last name.")
problem = True
while problem:
    mark = input("Enter your assessment mark: ")
    # IMPROVEMENT: better to explicitly check for num val, it covers all possible errors. like; '2k' 'Four' '<7/?>'
    if mark.isnumeric():

        mark = int(mark)  # safe to preform action only if 'mark=num value'

        if mark in valid_mark:
            if mark in pass_mark:
                # first_name & last_name are being high-lighted as undefined in IDE,
                # I assume, as this does run, they're defined if mark is in pass_mark range.. ? ASK ABOUT THIS !
                print("Well done {} {}, you have passed the assessment.".format(first_name, last_name))
                problem = False
            else:
                # Look, my first_name format attribute is defined.. I'm outside mark_pass block.
                print("Sorry {}, you have not passed the assessment.".format(first_name))
                problem = False
        elif mark > highest_mark:
            print("The entered mark was too high.")
        else:
            print("The entered mark was not a positive number.")
    else:
        print("The entered mark was not a positive number.")