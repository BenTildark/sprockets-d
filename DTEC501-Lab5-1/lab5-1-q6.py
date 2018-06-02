"""
Write a program which asks the user to enter their first name and start, stop(end) and step values for the loop. The start and stop(end) values are inclusive.

The start value can be greater than or less than the stop value.

The program should display

Please enter your first name:

followed by

Hi <FirstName>, please enter the start value:

Thank you <FirstName>, please enter the end value:

Thank you <FirstName>, please enter the step value:

Use a for loop to count from the start to the end using the step specified.

Display the following each time you go around the loop

Line x

where x is the loop counter.



Example
Please enter your first name: dave
Hi Dave, please enter the start value: 0
Thank you Dave, please enter the end value: 10
Thank you Dave, please enter the step value: 1
Line 0
Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7
Line 8
Line 9
Line 10
"""

# The lines of text you need to use to generate the output are given below for you.  Do not alter anything inside the quotes.
# "Please enter your first name: "
# "Hi {}, please enter the start value: "
# "Thank you {}, please enter the end value: "
# "Thank you {}, please enter the step value: "
# "Line {}"

first_name = input("Please enter your first name: ").capitalize()
first_value = int(input("Hi {}, please enter the start value: ".format(first_name)))
second_value = int(input("Thank you {}, please enter the end value: ".format(first_name)))
step_value = int(input("Thank you {}, please enter the step value: ".format(first_name)))

if first_value > second_value:
    opp_addend = -1
else:
    opp_addend = +1

start = first_value
end = second_value + opp_addend
step = step_value

user_range_count = range(start, end, step)
for count in user_range_count:
    print("Line {}".format(count))
