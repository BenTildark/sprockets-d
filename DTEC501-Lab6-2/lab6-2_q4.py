"""
The purpose of this lab is to troubleshoot existing code.

You can use the debugger if you want to but you don't have to.

You can use whatever debugging techniques you have been using so far if you prefer.

===================================================================================

The program is supposed to print a pass or not passed message based on the mark that was input.

Valid marks are between 0 and 100 inclusively.
Assume the user will only enter valid marks.
A Pass is a mark between 50-100 inclusively.
A Fail is a mark is between 0 and 49 inclusively.
There are mistakes in the code.
Leave the text inside the print and input sections as they are.
Use debugging techniques to correct the code.



Code
pass_mark = 0

x = int(input("Enter your assessment mark: "))

if x > pass_mark:
    print("You have passed the assessment.")
else:
    print("You have not passed the assessment.")



Examples
Enter your assessment mark: 0
You have not passed the assessment.



Enter your assessment mark: 49
You have not passed the assessment.



Enter your assessment mark: 50
You have passed the assessment.



Enter your assessment mark: 99
You have passed the assessment.



Enter your assessment mark: 100
You have passed the assessment.

"""
# Auth: Michael Devenport.
# Email: croxleyway@gmail.com

# The following code is supposed to print a pass or not passed message
# based on the mark that was input.
# Valid marks are between 0 and 100 inclusively.
# A Pass is a mark between 50-100 inclusively
# A Fail is a mark is between 0 and 49 inclusively
# Assume the user will only enter valid marks.
# There are mistakes in the code.
# Leave the text inside the print and input sections as they are.
# Use debugging techniques to correct the code.

pass_mark = range(50, 101)

x = int(input("Enter your assessment mark: "))

if x in pass_mark:
    print("You have passed the assessment.")
else:
    print("You have not passed the assessment.")
