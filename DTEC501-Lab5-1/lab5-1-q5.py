"""
Write a program which asks the user to enter their first name and start and stop(end) values for the loop.

The start value can be greater than or less than the end value.

The program should display

Please enter your first name:

followed by

Hi <FirstName>, please enter the start value:

Thank you <FirstName>, please enter the end value:

Use a for loop to count from the start to the end.

Display the following each time you go around the loop

Line x

where x is the loop counter.



Example
Please enter your first name: dave
Hi Dave, please enter the start value: 1
Thank you Dave, please enter the end value: 5
Line 1
Line 2
Line 3
Line 4
Line 5

"""

# The lines of text you need to use to generate the output are given below for you.  Do not alter anything inside the quotes.
# "Please enter your first name: "
# "Hi {}, please enter the start value: "
# "Thank you {}, please enter the end value: "
# "Line {}"

first_name = input("Please enter your first name: ").capitalize()

first_value = int(input("Hi {}, please enter the start value: ".format(first_name)))
second_value = int(input("Thank you {}, please enter the end value: ".format(first_name)))

start = first_value
end = second_value

user_range_count = range(start, end+1)
for count in user_range_count:
    print("Line {}".format(count))
