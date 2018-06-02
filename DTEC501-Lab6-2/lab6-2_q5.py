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
passing_score = 30

x = int(input("Enter your assessment score: "))

if x == passing_score:
    print("You have passed the assessment.")
else:
    print("You have not passed the assessment.")



Examples
Enter your assessment score: 0
You have not passed the assessment.

Enter your assessment score: 49
You have not passed the assessment.

Enter your assessment score: 50
You have passed the assessment.

Enter your assessment score: 99
You have passed the assessment.

Enter your assessment score: 100
You have passed the assessment.

"""
# Auth: Michael Devenport.
# Email: croxleyway@gmail.com

# The following code is supposed to print a pass or fail message
# based on the mark that was input.
# A Pass is a mark between 50-100 inclusively
# A Fail is a mark is between 0 and 49 inclusively
# Assume the user will only enter valid marks.
# There are mistakes in the code.
# Leave the text inside the print and input sections as they are.
# Use debugging techniques to correct the code.

passing_score = range(50, 101)
fail_score = range(0, 50)

x = int(input("Enter your assessment score: "))

if x in passing_score:
    print("You have passed the assessment.")
elif x in fail_score:
    print("You have not passed the assessment.")