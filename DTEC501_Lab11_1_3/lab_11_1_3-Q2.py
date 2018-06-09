"""
Assuming you have successfully completed Lab11-1-2, copy the is_palindromic function you created for Lab 11-1-2
and using Idle, paste it in a file called lab_11_1_3_module.py.

Do not change the function.

Do not put anything other than the function in the lab_11_1_3_module.py file.

Save the lab_11_1_3_module.py file and close it.

Modify the code you wrote for Q1 which is in the  lab_11_1_3-Q1.py file but import the is_palindromic function using
a wildcard.

Copy lab_11_1_3-Q1.py to lab_11_1_3-Q2.py

Use lab_11_1_3-Q2.py to do the following.

Import the is_palindromic function using a wildcard not by name from lab_11_1_3_module.

The rest of the task is the same as it was for Q1.

Ask the user to enter a phrase by displaying the message

Please enter a phrase:

Call the is_palindromic function and pass it the phrase the user entered.

If the is_palindromic function returns True display

<EnteredPhrase> is a palindrome.

If the is_palindromic function returns False display

<EnteredPhrase> is not a palindrome.

Hints.

This is a very short program, it's about 6 lines of code.
The important task is how you import the function.


Moodle and CodeRunner have other code present to test your code.  After ensuring you have imported the function as
per the question, use the examples below to test your code.

Examples.
Please enter a phrase: abba
abba is a palindrome.



Please enter a phrase: palindrome
palindrome is not a palindrome.


Paste the contents of  lab_11_1_3-Q2.py in the answer box below.

"""

from lab_11_1_3_module import *

phrase = input("Please enter a phrase: ")

if is_palindromic(phrase):
    print("{} is a palindrome.".format(phrase))
else:
    print("{} is not a palindrome.".format(phrase))
