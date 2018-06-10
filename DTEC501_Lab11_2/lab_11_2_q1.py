"""
For Q1 you will need to remove any spaces from the string received by the function.
The string replace() method is needed.  The syntax is

string.replace(old, new)

The following code snippet below illustrates the use of the replace() method.

single_space = " "
empty_string = ""
#
the_string = "This is a string"
print("[{}]".format(the_string))
the_string = the_string.replace(single_space, empty_string)
print("[{}]".format(the_string))
#
the_string = "ThisIsAstring"
print("[{}]".format(the_string))
the_string = the_string.replace(single_space, empty_string)
print("[{}]".format(the_string))
#
the_string = "This Is A string"
print("[{}]".format(the_string))
the_string = the_string.replace(single_space, empty_string)
print("[{}]".format(the_string))

Note that replace() does not generate an error if there are no spaces to be replaced,
that means you don't need to test for the presence of spaces in a string before replacing them.

QUESTION 1

Use the code you wrote for Lab11-1-2Q1 as the basis for this question and modify it to create a function which supports
being passed a string which possibly contains a phrase not just a single word. The function is still called
is_palindromic and has 1 parameter and returns True if the string is palindromic.

If the string received by the function is empty ("") then return the boolean value True.

If the string received by the function is palindromic then return the boolean value True, if it is not palindromic then
return the boolean value False.

Treat the string in a case insensitive manner.

Remove any code from the Lab6-1Q7 file which handled the presence of a full stop, it is not needed for this question.



Examples
print(is_palindromic(""))

True

print(is_palindromic("121"))

True

print(is_palindromic("A"))

True

print(is_palindromic("Not"))

False

print(is_palindromic("I prefer pi"))

True

print(is_palindromic("Did Hannah see bees Hannah did"))

True

print(is_palindromic("A nut for a jar of tuna"))

True

print(is_palindromic("Was it a cat I saw"))

True

print(is_palindromic(" A Toyota Race fast safe car A Toyota"))

True

print(is_palindromic("If I had a hifi"))

True

print(is_palindromic("Never odd or even"))

True

print(is_palindromic("Ok that is enough palindromes"))

False
"""
# Student: Michael Devenport
# Email: croxleyway@gmail.com

# Q: lab 11-2 q1


def is_palindromic(phrase):
    """function checks if phrase passed is palindromic"""

    val = str(phrase).lower().replace(" ", "")
    if val == val[::-1]:  # Reverse order
        return True
    else:
        return False


print(is_palindromic(""))
print(is_palindromic("121"))
print(is_palindromic("I prefer pi"))
print(is_palindromic("Ok that is enough palindromes"))
print(is_palindromic("Was it a cat I saw"))