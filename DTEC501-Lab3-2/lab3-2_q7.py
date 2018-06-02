"""
Write a program to ask the user to enter a word that starts with the letter Z.

Display a message saying it is True or False that the word they entered started with Z.

The letter Z can be in either upper or lower case.

Examples

Please enter a word that starts with Z: zed
It is True that Zed starts with Z.

Please enter a word that starts with Z: Zebedee
It is True that Zebedee starts with Z.

# The lines of text you need to use to generate the output are given below for you.  Do not alter anything inside the quotes.
# "Please enter a word that starts with {}: "
# "It is {} that {} starts with {}."
"""

word = input("Please enter a word that starts with {}: ".format('Z')).capitalize()

validate = word[:1] == 'Z'

print("It is {} that {} starts with {}.".format(validate, word, "Z"))