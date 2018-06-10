"""
Create a function called valid_password which returns True or False depending on the validity of the password.

The function valid_password  expects 2 parameters

the_password and min_length

the_password contains the password to be tested.

min_length is an integer value for the minimum length of the password.

The valid_password function does not display any output.

The valid_password function returns the boolean value True if the length of the_password > min_length and the_password
is not comprised of only alphabetic characters.

The valid_password function returns the boolean value False if the length of the_password < min_length or if
the_password is comprised of only alphabetic characters.

Example test code and output

user_password = "very_short"
password_min_length = 12
password_secure = valid_password(user_password, password_min_length)
if password_secure:
    print("Your password meets the security requirements.")
else:
    print("Your password does not meet the security requirements.")

Your password does not meet the security requirements.

print(valid_password("too_short",20))

False

print(valid_password("g00d",3))

True

"""

# Student: Michael Devenport
# Email: croxleyway@gmail.com

# Q: 3


def valid_password(the_password, min_length):

    """returns True if password meets requirements else false"""

    # validation
    if all([len(the_password) > min_length, not the_password.isalpha()]):
        return True
    else:
        return False


print(valid_password("too_short", 20))
print(valid_password("g00d", 3))