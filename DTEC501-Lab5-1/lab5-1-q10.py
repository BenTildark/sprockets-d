"""
Write a program to loop from 10 to -10 inclusively in steps of -2.

Use a while loop for this task.

Each time you go around the loop, the program should display

Line x

where x is the loop counter.

The value x must be right aligned.

Example

Line  10
Line   8
Line   6
Line   4
Line   2
Line   0
Line  -2
Line  -4
Line  -6
Line  -8
Line -10

Note

There are 2 spaces in "Line  10".

There is 1 space in "Line -10".

"""

# The line you need to use to generate the output is given below for you.  You need to put a formatter inside the {}'s to right justify the output.
# "Line {}"

step_neg2_10_to_neg_2 = 12

while step_neg2_10_to_neg_2 >= -8:
    step_neg2_10_to_neg_2 -= 2
    print("Line {:>3}".format(step_neg2_10_to_neg_2))
