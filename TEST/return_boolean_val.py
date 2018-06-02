"""

"""

first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))


def dupe(first, second):
    return True\
        if first == second\
        else False


print(
    "{} == {}".format(first_num, second_num)
    if dupe(first_num, second_num)
    else "{} != {}".format(first_num, second_num)
)