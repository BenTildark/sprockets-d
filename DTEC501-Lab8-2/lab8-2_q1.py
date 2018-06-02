"""
Write a program to ask the user to enter their first and last names and mobile number.

Store the user entered data in a dictionary and display as below.

Hint.

Treat the mobile number as a string.
Example
Please enter your given name: dave
Please enter your surname: bracken
Please enter your mobile number: 0225555555
First name: Dave
Last name: Bracken
Mobile number: 0225555555

"""
# Auth: Michael Devenport
# Email: croxleyway@gmail.com

first_name_prompt = "Please enter your given name: "
last_name_prompt = "Please enter your surname: "
mob_prompt = "Please enter your mobile number: "
first_name_statement = "First name: {}"
last_name_statement = "Last name: {}"
mob_statement = "Mobile number: {}"

first_name = input(first_name_prompt).strip().capitalize()
last_name = input(last_name_prompt).strip().capitalize()

mob_number = input(mob_prompt).strip()

user_credentials = {}

user_credentials.update({
    'first': first_name,
    'last': last_name,
    'mob': mob_number
})

print(first_name_statement.format(user_credentials['first']))
print(last_name_statement.format(user_credentials['last']))
print(mob_statement.format(user_credentials['mob']))
