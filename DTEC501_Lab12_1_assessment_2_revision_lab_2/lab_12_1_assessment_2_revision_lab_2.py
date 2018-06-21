"""
Write a function called get_birth_year which asks the user to enter the year they were born in and if it is valid,
return it as an integer.  If the value they enter is not valid, the function must ask them to enter it again.
The value is deemed to be invalid if it is outside the acceptable values or if it is a floating point number or if it
contains alphabetic characters.

The function get_birth_year expects two parameters

min_year

max_year

min_year is the lowest (earliest) valid year that can be accepted.

max_year is the highest (latest) valid year that can be accepted.

The year the user was born in must be between the min_year and the max_year inclusively.

The get_birth_year function must include a docstring.

The get_birth_year function must include comments.

The function get_birth_year returns an integer which is the year the user was born in.

Example test code and output

current_year = 2017
minimum_age = 17
maximum_age = 20
lowest_valid_year = current_year - maximum_age
highest_valid_year = current_year - minimum_age
year_born = get_birth_year(lowest_valid_year, highest_valid_year)
print(year_born)

Please enter your year of birth: 2000
2000

current_year = 2017
minimum_age = 17
maximum_age = 20
lowest_valid_year = current_year - maximum_age
highest_valid_year = current_year - minimum_age
year_born = get_birth_year(lowest_valid_year, highest_valid_year)
print(year_born)

Please enter your year of birth: 2006
2006 was outside the range of 1997 and 2000
Please enter your year of birth: 1996
1996 was outside the range of 1997 and 2000
Please enter your year of birth: The year two thousand
The year must be an integer.
Please enter your year of birth: 2001.5
The year must be an integer.
Please enter your year of birth: 1999
1999

lowest_valid_year = 1980
highest_valid_year = 1990
print(get_birth_year(lowest_valid_year, highest_valid_year))



Please enter your year of birth: 1985
1985

"""

# Student: Michael Devenport
# Email: croxleyway@gmail.com


def get_birth_year(min_year, max_year):

    """return year of birth if within min max params"""

    inside_range = True

    while inside_range:
        if min_year < max_year:
            yob = input("Please enter your year of birth: ")
            if yob.isnumeric():
                if all([int(yob) >= min_year, int(yob) <= max_year]):
                    return int(yob)
                else:
                    print("{} was outside the range of {} and {}".format(yob, min_year, max_year))
            else:
                print("The year must be an integer.")


print(get_birth_year(1980, 1990))
