"""
Write a function called get_initials which returns the initials of the full name that is passed to the function.

The function get_initials  expects one parameter

full_name

full_name contains the full name of the user.

The get_initials function does not display any output.

The get_initials function returns a string which is the initials of the user in upper case.

Assume the user will only have two names.

Example test code and output

print(get_initials("Dave bracken"))

DB

first_name = "dave"
last_name = "bracken"
name_separator = " "
full_name = first_name + name_separator + last_name

user_initials = get_initials(full_name)
print(user_initials)

DB

"""

# Student: Michael Devenport
# Email: croxleyway@gmail.com

# Q: 1


def get_initials(full_name):

    """return initials of full name"""

    # In this instance we assume full_name param is '2 words string' separated by white-space.
    # >>> full_name = "Michael devenport"

    # Calling split on full_name creates a list object of the 2 words in string.
    # >>> full_name.split()
    # ['Michael', 'devenport'] "the ghost"

    # Using "".join() we grab the first index of each item in our "ghost" list object
    # & join them without-whitespace
    # assign a variable for readability & return

    initials = "".join(item[0].upper() for item in full_name.split())
    return initials

    # This algorithm could be written on multi lines with assignments for simplicity

    # >>> full_name = "Michael devenport"
    # NOW full_name is: "Michael devenport"
    # >>> first_last = full_name.split()
    # NOW first_last is: ['Michael', 'devenport']
    # >>> initials = "".join(item[0].upper() for item in first_last)
    # NOW initials is: 'MD'


print(get_initials("Foo bar baSh"))
print(get_initials("Davey sprocket"))
