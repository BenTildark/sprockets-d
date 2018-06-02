"""
Write a program which asks the user to enter their first name and then display each character of their name on a separate line.

The program should display

Please enter your first name:

Use a for loop to display the character number and each character of their name on a separate line.

Examples
Please enter your first name: dave

1 D
2 a
3 v
4 e
There are 4 characters in Dave.

And if a single character is entered:

Please enter your first name: d

1 D
There is 1 character in D.

And if no characters were entered:

Please enter your first name:
You did not enter any characters.

Note, the use of singular and plural must be correct in the messages above.
"""

# The lines of text you need to use to generate the output are given below for you.  Do not alter anything inside the quotes.
# "Please enter your first name: "
# "{} {}"
# "There is {} character in {}."
# "There are {} characters in {}."
# "You did not enter any characters."

count = 0
name_prompt = "Please enter your first name: "
char_counter = "{} {}"
plur_count_name_char = "There are {} characters in {}."
sing_count_name_char = "There is {} character in {}."
error_prompt = "You did not enter any characters."


first_name = input(name_prompt).capitalize()

len_first_name = len(first_name)

for each_char in first_name:
    count += 1
    print(char_counter.format(count, each_char))

if count == 0:
    print(error_prompt)
elif len_first_name == 1:
    print(sing_count_name_char.format(len_first_name, first_name))
else:
    print(plur_count_name_char.format(len_first_name, first_name))



   