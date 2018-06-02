"""
Write a program to ask the user for their name and then to enter a sentence.  The program needs to identify the
character(s) in the middle of the sentence.

Ask the user to enter their first name by displaying the message:
Please enter your first name:

Display the message:
Hi <FirstName>, please enter a sentence:

If the sentence the user enters starts with a capital letter and ends with a full stop and if the sentence is an odd
number of characters in length excluding the full stop then display the message:
The character <MiddleCharacter> is in the middle of the sentence.

If the sentence the user enters starts with a capital letter and ends with a full stop and if the sentence is an even
number of characters in length excluding the full stop then display the message:
The characters <MiddleTwoCharacters> are in the middle of the sentence.

If the sentence does not start with a capital letter and end with a full stop then display the message:

Sorry <FirstName>, a sentence must start with a capital letter and end with a full stop.

Hints.

Look closely at the first two examples. Is the length in each case an odd or even number?
Use floor division to find the middle of the string.

Use the odd/even code to find if the length is odd or even. !!!!

There is no loop. !!!!

The simplest solution only needs two if's and two else's.
Use len() to find the length of the sentence.  Don't forget what to do with the full stop though.
Look at the sentences above that start with the word "If".  Use those as pseudo code.

Examples

Please enter your first name: dave
Dave, please enter a sentence: A simple sentence.
The character [ ] is in the middle of the sentence.

Please enter your first name: dave
Dave, please enter a sentence: A short sentence.
The characters [ s] are in the middle of the sentence.

Please enter your first name: dave
Dave, please enter a sentence: A short sentence
Sorry Dave, a sentence must start with a capital letter and end with a full stop.

Please enter your first name: dave
Dave, please enter a sentence: a short sentence.
Sorry Dave, a sentence must start with a capital letter and end with a full stop.


"""

# Auth: Michael Devenport.

name_prompt = "Please enter your first name: "
sentence_prompt = "{}, please enter a sentence: "
plural_return_statement = "The characters [{}] are in the middle of the sentence."
return_statement = "The character [{}] is in the middle of the sentence."
error = "Sorry {}, a sentence must start with a capital letter and end with a full stop."


first_name = input(name_prompt).capitalize()
sentence = input(sentence_prompt.format(first_name))

if sentence[0].isupper() and sentence.endswith('.'):

    if len(sentence) % 2 == 1:  # if odd True get center + preceding = true_center
        center = int(len(sentence) / 2)
        precede = sentence[center-1]
        true_center = precede + sentence[center]
        print(plural_return_statement.format(true_center))
    else:
        true_center = int(len(sentence) / 2 - 1)
        print(return_statement.format(sentence[true_center]))

else:
    print(error.format(first_name))

