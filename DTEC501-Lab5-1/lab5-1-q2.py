"""
Write a program to loop from 10 to 1 inclusively.

Use a for loop for this task.

Each time you go around the loop, the program should display

Line x

where x is the loop counter.



Example


Line 10
Line 9
Line 8
Line 7
Line 6
Line 5
Line 4
Line 3
Line 2
Line 1

# The line of text you need to use to generate the output is given below for you.  Do not alter anything inside the quotes.
# "Line {}"
"""

# have you taught us about .reversed() yet?

ten_to_one = reversed(range(1, 11))
for count in ten_to_one:
    print("Line {}".format(count))

