"""
Create a function called valid_name which returns True or False depending on the validity of the name.

The function valid_name  expects 2 parameters

the_name and min_length

the_name contains the name to be tested.

min_length is an integer value for the minimum length of the name.

The valid_name function does not display any output.

The valid_name function returns the boolean value True if the length of the_name > min_length and the_name
is comprised of only alphabetic characters.

The valid_name function returns the boolean value False if the length of the_name < min_length or if the_name
is not comprised of only alphabetic characters.



Example test code and output


first_name = "Dave"
name_length = 2

name_valid = valid_name(first_name, name_length)
if name_valid:
    print("Your name meets the requirements.")
else:
    print("Your name does not meet the requirements.")

Your name meets the requirements.





first_name = "0lafTheSnowman"
name_length = 2

name_valid = valid_name(first_name, name_length)
if name_valid:
    print("Your name meets the requirements.")
else:
    print("Your name does not meet the requirements.")

Your name does not meet the requirements.





print(valid_name("Dave",2))

True



print(valid_name("Dave",2))

False
"""

# Student: Michael Devenport
# Email: croxleyway@gmail.com

# Q: 4


def valid_name(the_name, min_length):

    """returns True if name meets req"""

    # validation
    if all([len(the_name) > min_length, the_name.isalpha()]):
        return True
    else:
        return False


print(valid_name("Dave", 2))
print(valid_name("Jane", 5))
