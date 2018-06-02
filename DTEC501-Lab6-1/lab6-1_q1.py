"""
Ask the user to enter their first name by displaying the message:
Please enter your first name:

Display the message:
<FirstName>, please enter a line of text:

Display the following message:
The first character in the line is <FirstCharacter>

If the last character in the line of text is not a full stop then display the message:
The last character in the line is <LastCharacter>

If the last character in the line of text is a full stop then display the message:
The last character before the full stop is <LastCharacterBeforeFullStop>

Where
<FirstCharacter> is the first character in the line of text.
<LastCharacter> is the last character in the line of text.
<LastCharacterBeforeFullStop> is the last character in the line of text before the full stop.



Hints.

If Hello was entered "H" is the <FirstCharacter>.
If Hello was entered "o" is the <LastCharacter>.
If Hello. was entered "o" is the <LastCharacterBeforeFullStop>.
Check the associated presentation for example code showing using an index to access the last character and last character but one in a string.
You don't need to know the length of the string.


Examples
Please enter your first name: dave
Dave, please enter a line of text: Hello
The first character in the line is H
The last character in the line is o



Please enter your first name: dave
Dave, please enter a line of text: hello.
The first character in the line is h
The last character before the full stop is o

"""

# Auth: Michael Devenport.

# Sorry no time for comments
# The lines of text you need to use to generate the output are given below for you.
# Do not alter anything inside the quotes.


name_prompt = "Please enter your first name: "
text_prompt = "{}, please enter a line of text: "
s_1 = "The first character in the line is {}"
s_2 = "The last character before the full stop is {}"
s_3 = "The last character in the line is {}"


first_name = input(name_prompt).capitalize()

text = input(text_prompt.format(first_name))

print(s_1.format(text[0]))
last_char = text[-1:]
last_2_char = text[-2:]
second_to_last_char = last_2_char[0]
if last_char.endswith('.'):
    print(s_2.format(second_to_last_char))
elif last_char != '.':
    print(s_3.format(last_char))
