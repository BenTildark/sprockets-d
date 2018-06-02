"""
Create a function called convert_to_celsius which has one parameter representing a temperature in
Fahrenheit and returns the equivalent temperature using the Celsius scale.

The returned value must be an integer.

The function must include an appropriate docstring.

Example
print(convert_to_celsius(50))

10

You can choose how you test your function in the IDE.  Post the function code below.  Do not include your testing code.


"""


def convert_to_celsius(fah):
    """Convert Fahrenheit to Celsius"""
    return int((fah - 32) * 5/9)


print(convert_to_celsius(32))