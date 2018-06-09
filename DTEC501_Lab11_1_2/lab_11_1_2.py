"""
Use the code you wrote for Lab6-1Q7 as the basis for this question and modify it to create a function called
is_palindromic which has 1 parameter and returns True if the value is palindromic and False if it is not palindromic.

If the value received by the function is empty ("") then return True.

If the value received by the function is 1 character in length, return True.

If the value received by the function is palindromic return True, if it is not palindromic, return False.

Treat the value in a case insensitive manner.

The function must include an appropriate docstring.

Remove any code from the Lab6-1Q7 file which handled the presence of a full stop, it is not needed for this question.

Examples

print(is_palindromic(121))

True

print(is_palindromic("A"))

True

print(is_palindromic("Not"))

False

print(is_palindromic("aba"))

True

print(is_palindromic("Abba"))

True

"""
# Student: Michael Devenport
# Email: croxleyway@gmail.com

# Lab11-1-2 Q1


def is_palindromic(value):
    """function checks if value passed is palindromic"""
    val = str(value).lower()
    if val == val[::-1]:  # Reverse order
        return True
    else:
        return False
