"""
Write a program to ask the user for their name and then ask them to enter a sentence.  Your program must decide if the text they entered was a sentence.

Ask the user to enter their first name by displaying the message:

Please enter your first name:

Then display the message:
<FirstName>, please enter a sentence:


If the sentence the user entered at this point ends with a full stop then display the following message:
The sentence contains <SentenceLength> characters.
where <SentenceLength> is the length of the sentence not including the full stop character.

If the sentence did not end with a full stop then display the following message:
Sorry <FirstName>, a sentence must end with a full stop.


Hints.

No loop is needed.
Check the associated presentation for using an index to access the last character in a string or for using an appropriately named method.


Example


Please enter your first name: dave
Dave, please enter a sentence: This is a sentence.
The sentence contains 18 characters.
"""
# Auth: Michael Devenport.

name_prompt = "Please enter your first name: "
sent_prompt = "{}, please enter a sentence: "
return_statement = "The sentence contains {} characters."
error = "Sorry {}, a sentence must end with a full stop."


first_name = input(name_prompt).capitalize()
sentence = input(sent_prompt.format(first_name))

sentence_count = len(sentence)-1


if sentence.endswith('.'):
    print(return_statement.format(sentence_count))
else:
    print(error.format(first_name))

