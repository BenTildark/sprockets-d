"""
Write a program to loop from 1 to 11 inclusively in steps of 2.

Use a while loop for this task.

Each time you go around the loop, the program should display

Line x

where x is the loop counter.

The value x must be right aligned.

Example

Line  1
Line  3
Line  5
Line  7
Line  9
Line 11

Note

There is 1 space in "Line 11".

There are 2 spaces in "Line  9".

"""

# The line you need to use to generate the output is given below for you.
# You need to put a formatter inside the {}'s to right justify the output.
# This is the rare occasion where you need to modify the string.

# "Line {}"

step2_1_to_11 = -1

while step2_1_to_11 <= 9:
    step2_1_to_11 += 2
    print("Line {:>2}".format(step2_1_to_11))