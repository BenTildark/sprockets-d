"""
Write a program to loop from 10 to 1 inclusively.

Use a while loop for this task.

Each time you go around the loop, the program should display

Line x

where x is the loop counter.

The value x must be right aligned.



Example


Line 10
Line  9
Line  8
Line  7
Line  6
Line  5
Line  4
Line  3
Line  2
Line  1

Note.

There is only one space in "Line 10".

There are two spaces in "Line  9".

"""
# The line you need to use to generate the output is given below for you.  You need to put a formatter inside the {}'s to right justify the output.
# "Line {}"

count = 11

while count >= 2:
    count -= 1
    print("Line {:>2}".format(count))
