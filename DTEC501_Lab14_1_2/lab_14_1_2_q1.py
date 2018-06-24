"""
Create a function called validate_password

validate_password requires 2 parameters

first_pwd and second_pwd

first_pwd is the string containing the text from the first password window.
second_pwd is the string containing the text from the second password window.


The password is deemed to be valid if it matches all of the requirements below.

The password is >= 8 characters in length.
Both entered passwords are identical.
If the first and last characters of the password are alphabetic then the first character of the password must be
a different alphabetic letter to the last character of the password regardless of case.
e.g 1st char is A so last char cannot be A or a.
There are no more than 2 vowels in the password.
The password has at least 1 alphabetic character in upper case and 1 alphabetic character in lower case.
Not all alphabetic characters are in the same case (either all upper or all lower).


If the password is valid return the boolean value True.

If the password is not valid return the boolean value False.

Hints.

Use a for loop to iterate through the password when looking for vowels and upper/lower case.
You only need one loop.
A short solution has 22 lines of code inc, def, docstring and return.  Use that figure as a ball park.
If you have 30+ lines, revisit your design.  < 30 lines is ok.

Example test code and output

password1 = "abcd1234"
password2 = "abcd1234"
print(validate_password(password1, password2))

False

password1 = "Abcd1234"
password2 = "Abcd1234"
print(validate_password(password1, password2))

True

password1 = "Abedi23a"
password2 = "Abedi23a"
print(validate_password(password1, password2))

False

"""

# Student: Michael Devenport
# Email: croxleyway@gmail.com


def validate_password(first_pwd, second_pwd):

    """return True if valid password else False."""

    min_length = 8
    vowels = ['a', 'e', 'i', 'o', 'u']
    max_vowels = 2
    min_char_by_type = 1

    if all([len(first_pwd) >= min_length, first_pwd == second_pwd]):
        count_vowel, count_upper, count_lower = 0, 0, 0
        for char in first_pwd:
            if char.lower() in vowels:
                count_vowel += 1
            if char.isupper():
                count_upper += 1
            if char.islower():
                count_lower += 1

        if not first_pwd[0].isnumeric():
            if all([count_vowel <= max_vowels, count_upper >= min_char_by_type, count_lower >= min_char_by_type,
                    first_pwd[0].lower() != first_pwd[-1].lower()]):
                return True
            else:
                return False
        elif all([count_vowel <= max_vowels, count_upper >= min_char_by_type, count_lower >= min_char_by_type]):
            return True
        else:
            return False

    else:
        return False


password1 = "abcd1234"
password2 = "abcd1234"
print(validate_password(password1, password2))

# >>> False

password1 = "aBc12345"
password2 = "aBc12345"
print(validate_password(password1, password2))

# >>> True

password1 = "Abedi23a"
password2 = "Abedi23a"
print(validate_password(password1, password2))

# >>> False

password1 = "4bcD1234"
password2 = "4bcD1234"
print(validate_password(password1, password2))

# >>> True
