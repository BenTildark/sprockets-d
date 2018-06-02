"""
Create a function called is_odd which has one integer parameter and returns a boolean value.

The function must return True if the number it was passed is an odd number.
The function must return False if the number it was passed is an even number.

The function must include an appropriate docstring.

Hint.

See Presentation 4-2 for odd/even code.

Examples
print(is_odd(1))

True

print(is_odd(2))

False

You can choose how you test your function in the IDE.  Post the function code below.  Do not include your testing code.

"""


def is_odd(num):
    """Return True if integer is odd else False"""
    if num % 2 == 1:
        return True
    else:
        return False


print(is_odd.__doc__)
print(is_odd(1))
