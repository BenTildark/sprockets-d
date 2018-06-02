"""
Write a program to ask the user to enter their name followed by a word.  The program needs to check if the entered word is a palindrome.

Ask the user to enter their first name by displaying the message:
Please enter your first name:

then display the message:
Hi <FirstName>, please enter a word and I will tell you if it is a palindrome:


If there was a full stop the end of the word they entered, work out if the word before the full stop is a palindrome.
If there was not a full stop the end of the word they entered, work out if the word they entered is a palindrome.


If the word is a palindrome, display the message
<word> is a palindrome.
If the word is not a palindrome, display the message
<word> is not a palindrome.

You must accommodate the user entering the word in a mixture of upper and lower case characters and display the entered word correctly capitalised. You must test the palindromic status of the word in a case insensitive manner.  See the example below.



Hint.

See the slide in the associated presentation for example palindrome code.


Examples


Please enter your first name: dave
Hi Dave, please enter a word and I will tell you if it is a palindrome: mum
mum is a palindrome.

Please enter your first name: Dave
Hi Dave, please enter a word and I will tell you if it is a palindrome: muM
Mum is a palindrome.

Please enter your first name: dave
Hi Dave, please enter a word and I will tell you if it is a palindrome: mUm
Mum is a palindrome.

Please enter your first name: Dave
Hi Dave, please enter a word and I will tell you if it is a palindrome: mUm.
Mum is a palindrome.

Please enter your first name: dave
Hi Dave, please enter a word and I will tell you if it is a palindrome: not
Not is not a palindrome.

"""

# Auth: Michael Devenport.

name_prompt = "Please enter your first name: "
word_prompt = "Hi {}, please enter a word and I will tell you if it is a palindrome: "
correct = "{} is a palindrome."
incorrect = "{} is not a palindrome."

first_name = input(name_prompt).capitalize()
word_input = input(word_prompt.format(first_name)).lower()

if word_input.endswith('.'):
    word_input = word_input[:-1]  # Slice off last char


def is_palindrome(word):
    if word == word[::-1]:  # Reverse order
        print(correct.format(word_input).capitalize())
    else:
        print(incorrect.format(word_input).capitalize())


is_palindrome(word_input)

