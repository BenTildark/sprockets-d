"""
Write a program to loop from 10 to 1 inclusively in steps of -2.

Use a for loop for this task.

Each time you go around the loop, the program should display

Line x

where x is the loop counter.



Example


Line 10
Line 8
Line 6
Line 4
Line 2

"""

# The line of text you need to use to generate the output is given below for you.  Do not alter anything inside the quotes.
# "Line {}"

step2_10_to_1 = range(10, 1, -2)
for count in step2_10_to_1:
    print("Line {}".format(count))