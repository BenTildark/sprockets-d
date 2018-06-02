"""
Create a function called convert_to_fahrenheit which has one parameter representing a temperature in Celsius
and returns the equivalent temperature using the Fahrenheit scale.

The returned value must be an integer.

The function must include an appropriate docstring.



Example
print(convert_to_fahrenheit(10))

50



You can choose how you test your function in the IDE.  Post the function code below.  Do not include your testing code.
"""


def convert_to_fahrenheit(cel):
    """Convert Celsius to Fahrenheit"""
    return int((9 / 5) * cel + 32)


print(convert_to_fahrenheit(10))