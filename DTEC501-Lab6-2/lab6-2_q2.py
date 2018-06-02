"""
The purpose of this lab is to troubleshoot existing code.

You can use the debugger if you want to but you don't have to.

You can use whatever debugging techniques you have been using so far if you prefer.

===================================================================================

The program is supposed to validate assessment marks and print out a valid/not valid message based on the mark entered.

Valid marks are between 0 and 30 inclusively.
There are mistakes in the code.
Leave the text inside the print and input sections as they are.
Use debugging techniques to correct the code.

Code
minimum_mark = 0
maximum_mark = 20

x = int(input("Enter your assessment mark: "))
if x == minimum_mark and x == minimum_mark:
    print("Your assessment mark is valid.")
else:
    print("Your assessment mark is not valid.")


Examples:

Enter your assessment mark: -1
Your assessment mark is not valid.

Enter your assessment mark: 0
Your assessment mark is valid.

Enter your assessment mark: 29
Your assessment mark is valid.

"""
# Auth: Michael Devenport.
# Email: croxleyway@gmail.com

# The following code is supposed to validate assessment marks
# and print out a valid/not valid message based on the mark entered.
# Valid marks are between 0 and 30 inclusively.
# There are mistakes in the code.
# Leave the text inside the print and input sections as they are.
# Use debugging techniques to correct the code.

minimum_mark = 0
maximum_mark = 30

x = int(input("Enter your assessment mark: "))
if all([x >= minimum_mark, x <= maximum_mark]):
    print("Your assessment mark is valid.")
else:
    print("Your assessment mark is not valid.")

