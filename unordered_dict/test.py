"""
testing python 2.7 ( unordered dict > output > dif between 3 ordered calls to print[right order]
vs looping insertion data[wrong order, ie values returned not as inserted] )
"""

first_name_prompt = "Please enter your given name: "
last_name_prompt = "Please enter your surname: "
mob_prompt = "Please enter your mobile number: "
first_name_statement = "First name: {}"
last_name_statement = "Last name: {}"
mob_statement = "Mobile number: {}"

first_name = raw_input(first_name_prompt).strip().capitalize()
last_name = raw_input(last_name_prompt).strip().capitalize()

mob_number = raw_input(mob_prompt).strip()

user_credentials = {}

user_credentials.update({
    'first': first_name_statement.format(first_name),
    'last': last_name_statement.format(last_name),
    'mob': mob_statement.format(mob_number)
})

print(user_credentials['first'])
print(user_credentials['last'])
print(user_credentials['mob'])

print('')

for key in user_credentials.keys():     # Get the key's
    print(user_credentials[key])        # Print each value