"""
You have been tasked with writing a password checking program.  The password is valid if it matches the following
requirements:

The password must contain 8 or more characters.
The password must contain alphanumeric characters.
The first character of the password must be a number.


Ask the user to enter their first name by displaying the message:
Please enter your first name:

then display the following messages:

The password must contain 8 or more characters.
The password must contain alphanumeric characters.
The first character of the password must be a number.
<FirstName>, please enter the password :

If the password matches the requirements above then display the message:

The password [<EnteredPassword>] meets the security standard.

If the password matches the requirements above then display the message:

The password [<EnteredPassword>] does not meet the security standard.

If the user accidentally put a space or spaces at either the start or the end of the password, your code must remove
it/them and then work out if the remaining password is valid.

Hints.

There's no loop.
Don't forget that users accidentally put spaces into input text and that needs to be removed.

Examples

Please enter your first name: dave
The password must contain 8 or more characters.
The password must contain alphanumeric characters.
The first character of the password must be a number.
Dave, please enter the password: short
The password [short] does not meet the security standard.


Please enter your first name: dave
The password must contain 8 or more characters.
The password must contain alphanumeric characters.
The first character of the password must be a number.
Dave, please enter the password: ThisIsLongEnough
The password [ThisIsLongEnough] does not meet the security standard.


Please enter your first name: Dave
The password must contain 8 or more characters.
The password must contain alphanumeric characters.
The first character of the password must be a number.
Dave, please enter the password: 1ThisIsLongEnough
The password [1ThisIsLongEnough] meets the security standard.


Please enter your first name: dave
The password must contain 8 or more characters.
The password must contain alphanumeric characters.
The first character of the password must be a number.
Dave, please enter the password:  1ExtraSpaceAtTheStart
The password [1ExtraSpaceAtTheStart] meets the security standard.



Please enter your first name: Dave
The password must contain 8 or more characters.
The password must contain alphanumeric characters.
The first character of the password must be a number.
Dave, please enter the password:  1ExtraSpaceAtTheStartAndAtTheEnd
The password [1ExtraSpaceAtTheStartAndAtTheEnd] meets the security standard.

"""
# Auth: Michael Devenport.

name_prompt = "Please enter your first name: "
eight_char = "The password must contain 8 or more characters."
al_num = "The password must contain alphanumeric characters."
pass_first_char = "The first character of the password must be a number."
pass_prompt = "{}, please enter the password: "
success_statement = "The password [{}] meets the security standard."
error = "The password [{}] does not meet the security standard."

# CONDITIONS:
# first char digit
# min_count = 8
# must be alphanumeric

first_name = input(name_prompt).capitalize()
instructions = [eight_char, al_num, pass_first_char]
for i in instructions:
    print(i)

password = input(pass_prompt.format(first_name)).strip()
pass_sub_string = password[1:]

if password[0].isdigit() and len(password) >= 8 and password.isalnum():
    print(success_statement.format(password))
else:
    print(error.format(password))

# THIS CODE RETURNED PARTIAL CORRECT @ MOODLE LAB6-1 NOT SUBMITED !!!!
# I forgot the strip call to function on password input. ;-(