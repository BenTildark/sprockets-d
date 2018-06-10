"""
Create a function called string_length which returns the length of a string excluding the characters specified.

The function string_length  expects 2 parameters

the_string and excluded_character

the_string contains the string of characters to be be examined.

excluded_character is the character that should not be included in the length of the string.

The string_length function does not display any output.

The string_length function returns an integer which is the length of the_string without counting all
the instances of excluded_character.



Example test code and output


full_name = "Olaf_the_snowman"
unwanted_char = "_"
name_length = string_length(full_name, unwanted_char)
print("{} contains {} alphabetic characters.".format(full_name, name_length))

Olaf_the_snowman contains 14 alphabetic characters.





print(string_length("Dave","a"))

3


print(string_length("Jane"," "))

4


print(string_length("Abraham","a"))

5


"""

# Student: Michael Devenport
# Email: croxleyway@gmail.com

# Q: 5


def string_length(the_string, excluded_character):

    """returns string length"""

    # remove the excluded_char return length of refactored string
    refactored_string = the_string.replace(excluded_character, '')
    return len(refactored_string)


print(string_length("Dave", "a"))
print(string_length("Jane", " "))
print(string_length("Abraham", "a"))