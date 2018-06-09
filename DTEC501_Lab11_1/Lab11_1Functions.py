# functions module


def starts_with_capital(string):
    """Returns True if first char is uppercase else False"""
    if string[:1].isupper():
        return True
    else:
        return False


def is_punctuated_correctly(string):
    """return True if the last char full stop, or question mark"""
    last_char = ['.', '!', '?']
    if string[-1:] in last_char:
        return True
    else:
        return False


def is_odd(num):
    """Return True if integer is odd else False"""
    if num % 2 == 1:
        return True
    else:
        return False


def is_even(num):
    """Return True if integer is even else False"""
    if num % 2 == 0:
        return True
    else:
        return False


def convert_to_celsius(fah):
    """Convert Fahrenheit to Celsius"""
    return int((fah - 32) * 5/9)


def convert_to_fahrenheit(cel):
    """Convert Celsius to Fahrenheit"""
    return int((9 / 5) * cel + 32)