"""
Write a program to ask the user to enter a word whose letters are all lower case.

Display a message saying it is true or false (note the use of lower case) that the word they entered met this requirement.

Example's

Please enter a word whose letters are all lower case: lower
It is true that lower is in all lower case letters.

Please enter a word whose letters are all lower case: UPPeR
It is false that UPPeR is in all lower case letters.

# The lines of text you need to use to generate the output are given below for you.  Do not alter anything inside the quotes.
# "Please enter a word whose letters are all lower case: "
# "It is {} that {} is in all lower case letters."
"""
word = input("Please enter a word whose letters are all lower case: ")

validator = any(i.isupper() for i in word)
if validator == False:
    validator = "true"
else:
    validator = "false"

print("It is {} that {} is in all lower case letters.".format(validator, word))