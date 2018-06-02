
# Create a function called is_punctuated_correctly which has one string parameter and returns a boolean value.

# The function must return True if the last character is a full stop or an exclamation mark or a question mark.
# the function must return False if the last character is a character other than one of the above.

# The function must include an appropriate docstring.

# Hint.

# Use index of -1 for getting the last character of a string.  See Presentation 6-1.


# Examples
# user_sentence = "This is a correctly terminated sentence."
# properly_punctuated = is_punctuated_correctly(user_sentence)
# print(properly_punctuated )

# True

# user_sentence = "This is a correctly terminated sentence."
# properly_punctuated  = is_punctuated_correctly(user_sentence)
# print(type(properly_punctuated ))

# <class 'bool'>

# user_sentence = "This is a correctly terminated sentence."
# print(is_punctuated_correctly(user_sentence))

# True

# user_sentence = "This is a proper sentence"
# print(is_punctuated_correctly(user_sentence))

# False

# user_sentence = "Is this a question?"
# print(is_punctuated_correctly(user_sentence))

# True

# You can choose how you test your function in the IDE.  Post the function code below, not your testing code.


def is_punctuated_correctly(string):

    """return True if the last char full stop, or question mark"""
    last_char = ['.', '!', '?']
    if string[-1:] in last_char:
        return True
    else:
        return False


print(is_punctuated_correctly.__doc__)
print(is_punctuated_correctly("88 is the answer!"))
