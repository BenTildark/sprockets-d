"""
Write a program to ask the user to enter a word that starts with a capital letter and with subsequent letters in lower case.

Display a message saying it is True or False that the word they entered met this requirement.

Example

Please enter a word that starts with a capital letter and with subsequent letters in lower case: Upper
It is True that Upper starts with a capital letter and all subsequent letters are in lower case.

# The lines of text you need to use to generate the output are given below for you.  Do not alter anything inside the quotes.
# "Please enter a word that starts with a capital letter and with subsequent letters in lower case: "
# "It is {} that {} starts with a capital letter and all subsequent letters are in lower case."
"""


word = input("Please enter a word that starts with a capital letter and with subsequent letters in lower case: ")

first_let = word[:1]
sub_let = word[1:]

first_validate = any(i.islower() for i in first_let)
sub_validate = any(i.isupper() for i in sub_let)
if first_validate == False & sub_validate == False:
    validation_result = "True"
else:
    validation_result = "False"

print("It is {} that {} starts with a capital letter and all subsequent letters are in lower case.".format(validation_result, word))