"""
Write a program to loop from 1 to 10 inclusively.

Use a while loop for this task.

Each time you go around the loop, the program should display

Line x

where x is the loop counter.

The value x must be right aligned.



Example


Line  1
Line  2
Line  3
Line  4
Line  5
Line  6
Line  7
Line  8
Line  9
Line 10



Note.

There is only one space in "Line 10".

There are two spaces in "Line  9".

count = 0
 while count <= 10:
...     count += 1
...     print(count)
"""
# The line you need to use to generate the output is given below for you.  You need to put a formatter inside the {}'s to right justify the output.
# "Line {}"

count = 0

while count <= 9:
    count += 1
    print("Line {:>2}".format(count))
