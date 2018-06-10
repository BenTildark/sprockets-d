"""
This is a "think a little bit outside the box" type question.

Create 2 functions

is_even
find_even

is_even expects 1 parameter
the_value
the_value is an integer.

is_even will return the boolean value True if the_value is an even number.
is_even will return the boolean value False if the_value is not an even number.

The is_even function does not display any output

find_even expects 1 parameter.

the_list
the_list is a list object containing integers.

The find_even function does not display any output

The find_even function will return a list of even integers. It will make use of the is_even function by
calling/invoking it.

Example test code and output

print(is_even(99))

False

print(is_even(20))

True

age = 41
even_age = is_even(age)
print("It is {} that your age is even.".format(even_age))

It is False that your age is even.

a_list = [50,23,30,41,99]
print(find_even(a_list))

[50, 30]

a_list = [17,11,22,21,44]
print(find_even(a_list))

[22, 44]

"""

# Student: Michael Devenport
# Email: croxleyway@gmail.com

# Q: 2


def is_even(the_value):

    """return True if value is even else False"""

    if the_value % 2 == 0:
        return True
    else:
        return False


def find_even(the_list):

    """return list of even entries"""

    even_list = []
    for x in the_list:
        if x % 2 == 0:
            even_list.append(x)
    return even_list


age = 41
even_age = is_even(age)
print("It is {} that your age is even.".format(even_age))


a_list = [17, 11, 22, 21, 44]
print(find_even(a_list))


a_list = [50, 23, 30, 41, 99]
print(find_even(a_list))