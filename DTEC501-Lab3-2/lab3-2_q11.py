"""
Write a program to ask the user to enter a word whose letters are all upper case.

Display a message saying it is true or false (note the use of lower case) that the word they entered met this requirement.

Example

Please enter a word whose letters are all upper case: SHOUTiNG
It is false that SHOUTiNG is in all upper case letters.

# The lines of text you need to use to generate the output are given below for you.  Do not alter anything inside the quotes.
# "Please enter a word whose letters are all upper case: "
# "It is {} that {} is in all upper case letters."
"""

word = input("Please enter a word whose letters are all upper case: ")

validator = any(i.islower() for i in word)
if validator == False:
    validator = "true"
else:
    validator = "false"

print("It is {} that {} is in all upper case letters.".format(validator, word))