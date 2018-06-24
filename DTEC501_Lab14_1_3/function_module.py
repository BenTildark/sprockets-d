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


# password1 = "abcd1234"
# password2 = "abcd1234"
# print(validate_password(password1, password2))

# >>> False

# password1 = "aBc12345"
# password2 = "aBc12345"
# print(validate_password(password1, password2))

# >>> True
