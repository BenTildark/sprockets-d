"""
Write a program to ask the user to enter a word that ends with the letter z.

Display a message saying it is True or False that the word they entered ended with z.

The character z must be lower case.

Example

Please enter a word that ends with z: Buzz
It is True that Buzz ends with z.

# The lines of text you need to use to generate the output are given below for you.  Do not alter anything inside the quotes.
# "Please enter a word that ends with {}: "
# "It is {} that {} ends with {}."
"""

word = input("Please enter a word that ends with {}: ".format('z')).capitalize()

validate = word[-1:] == 'z'

print("It is {} that {} ends with {}.".format(validate, word, "z"))