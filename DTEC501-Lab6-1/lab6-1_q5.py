"""
If the sentence starts with a capital letter and ends with a full stop then count the number of spaces in the sentence and display the appropriate grammatically correct message from the following two messages:

There are <SpaceCount> spaces in the sentence.

There is <SpaceCount> space in the sentence.



If the sentence does not start with a capital letter and end with a full stop then display the message:
Sorry <FirstName>, a sentence must start with a capital letter and end with a full stop.
and loop back to the section that displays the message "Hi <FirstName>, please enter a sentence. Enter Stop! to stop running the program: "

If the user enters Stop! (case sensitive) then display the following message

Thanks for using the program <FirstName>.
and exit from the program.



Hints.

Loop while you haven't been told to Stop!
Check the slides for using an index to find the first and last character in a string.


Examples


Please enter your first/given name: Dave
Dave, please enter a sentence. Enter Stop! to stop running the program: This is not a sentence
Sorry Dave, a sentence must start with a capital letter and end with a full stop.
Dave, please enter a sentence. Enter Stop! to stop running the program: Stop!
Thanks for using the program Dave.



Please enter your first/given name: dave
Dave, please enter a sentence. Enter Stop! to stop running the program: This is a sentence.
There are 3 spaces in the sentence.
Dave, please enter a sentence. Enter Stop! to stop running the program: Stop!
Thanks for using the program Dave.



Please enter your first/given name: dave
Dave, please enter a sentence. Enter Stop! to stop running the program: Short sentence.
There is 1 space in the sentence.
Dave, please enter a sentence. Enter Stop! to stop running the program: Stop!
Thanks for using the program Dave.


"""

# Auth: Michael Devenport.

name_prompt = "Please enter your first/given name: "
sentence_prompt = "{}, please enter a sentence. Enter Stop! to stop running the program: "
return_statement = "There is {} space in the sentence."
plural_return_statement = "There are {} spaces in the sentence."
error = "Sorry {}, a sentence must start with a capital letter and end with a full stop."
exit_statement = "Thanks for using the program {}."
exit_loop = 'Stop!'

first_name = input(name_prompt).capitalize()
while first_name:
    sentence = input(sentence_prompt.format(first_name))

    if sentence[0].isupper() and sentence.endswith('.'):

        count_blank_space = sentence.count(' ')

        if count_blank_space == 1:
            print(return_statement.format(count_blank_space))
        else:
            print(plural_return_statement.format(count_blank_space))

    elif sentence == exit_loop:
        print(exit_statement.format(first_name))
        exit()
    else:
        print(error.format(first_name))


