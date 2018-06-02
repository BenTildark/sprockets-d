"""
Ask the user to enter their first name by displaying the message:
Please enter your first name:

Display the message:
<FirstName>, please enter a sentence. Enter Stop! to stop running the program:



If the sentence ends with a full stop then count the number of spaces in the sentence and display the appropriate (grammatically correct) message from below:
There are <SpaceCount> spaces in the sentence.

There is <SpaceCount> space in the sentence.



If the sentence does not end with a full stop then display the message:
Sorry <FirstName>, a sentence must end with a full stop.
and loop back to the section that displays the message

Hi <FirstName>, please enter a sentence. Enter Stop! to stop running the program:



If the user enters Stop! (case sensitive) then stop running the program.


Hint.

Loop while you haven't been told to Stop!


Examples


Please enter your first name: dave
Dave, please enter a sentence. Enter Stop! to stop running the program: Short sentence.
There is 1 space in the sentence.
Dave, please enter a sentence. Enter Stop! to stop running the program: Stop!




Please enter your first name: Dave
Dave, please enter a sentence. Enter Stop! to stop running the program: This is a sentence.
There are 3 spaces in the sentence.
Dave, please enter a sentence. Enter Stop! to stop running the program: This is not a sentence
Sorry Dave, a sentence must end with a full stop.
Dave, please enter a sentence. Enter Stop! to stop running the program: This is a sentence
Sorry Dave, a sentence must end with a full stop.
Dave, please enter a sentence. Enter Stop! to stop running the program: Stop!

"""

# Auth: Michael Devenport.

name_prompt = "Please enter your first name: "
sentence_prompt = "{}, please enter a sentence. Enter Stop! to stop running the program: "
return_statement = "There is {} space in the sentence."
plural_return_statement = "There are {} spaces in the sentence."
error = "Sorry {}, a sentence must end with a full stop."

exit_loop = 'Stop!'

first_name = input(name_prompt).capitalize()
while first_name:
    sentence = input(sentence_prompt.format(first_name))

    if sentence.endswith('.'):

        count_blank_space = sentence.count(' ')

        if count_blank_space == 1:
            print(return_statement.format(count_blank_space))
        else:
            print(plural_return_statement.format(count_blank_space))

    elif sentence == exit_loop:
        exit()
    else:
        print(error.format(first_name))
