"""
*****************************OVERALL INSTRUCTION*****************************

As an example, consider the code in the presentation for multiplying a number by two.

If the question says to create a function called times_two which returns double the value that was
passed to the function then the function below is the correct one to use.

def times_two(multiplicand):

The function returns 2 * multiplicand

multiplier = 2

product = multiplicand * multiplier

return product

To test your code you could write the following code

entered_number = int(input("Please enter a number: "))

result = times_two(entered_number)

print("{} * 2 = {}".format(number, result))

5 * 2 = 10

or you could use a short cut.

entered_number = 2
print(times_two(entered_number))
4

entered_number = 3
print(times_two(entered_number))
6

entered_number = 5
print(times_two(entered_number))
10


Either way, it is important that you only paste the function code to Moodle so in this case,
submit the following, nothing else:


def times_two(multiplicand):

The function returns 2 * multiplicand

multiplier = 2

product = multiplicand * multiplier

return product

**************************************************************************

Create a function called starts_with_capital which has one parameter and returns a boolean value.
The function must return True if the first character of the parameter that is passed to it is a capital letter.
The function must return False if the first character of the parameter that is passed to it is not a capital letter.

The function must include an appropriate docstring.

Hints.

Use index 0 to get the first character of a string.  See Presentation 6-1.
Use isalpha() for getting the alphabetic status.
Use isupper() for getting the upper case status.  See Presentation 3-2.

Examples
user_sentence = "This sentence starts with a capital letter."
correctly_capitalised = starts_with_capital(user_sentence)
print(correctly_capitalised)

True

user_sentence = "This sentence starts with a capital letter."
print(starts_with_capital(user_sentence))

True

user_sentence = "this sentence starts with a capital letter."
print(starts_with_capital(user_sentence))

False

user_sentence = "42 is the answer."
print(starts_with_capital(user_sentence))

False

Example showing the correct return type
user_sentence = "This sentence starts with a capital letter."
correctly_capitalised = starts_with_capital(user_sentence)
print(type(correctly_capitalised))

<class 'bool'>


You can choose how you test your function in the IDE.  Post the function code below, not your testing code.

"""


def starts_with_capital(string):
    """Returns True if first char is uppercase else False"""
    if string[:1].isupper():
        return True
    else:
        return False


print(starts_with_capital.__doc__)
print(starts_with_capital("45 is the answer."))

# user_sentence = "This sentence starts with a capital letter."
# correctly_capitalised = starts_with_capital(user_sentence)
# print(type(correctly_capitalised))

# user_sentence = "This sentence starts with a capital letter."
# correctly_capitalised = starts_with_capital(user_sentence)
# print(correctly_capitalised)

# user_sentence = "this sentence starts with a capital letter."
# print(starts_with_capital(user_sentence))

# user_sentence = "42 is the answer."
# print(starts_with_capital(user_sentence))
