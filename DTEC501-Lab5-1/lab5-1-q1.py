"""
Write a program to loop from 1 to 10 inclusively.

Use a for loop for this task.

Each time you go around the loop, the program should display

Line x

where x is the loop counter.



Example


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

# The line of text you need to use to generate the output is given below for you.  Do not alter anything inside the quotes.
# "Line {}"

start = 1
stop = 11

one_to_ten = range(start, stop)

for each_value in one_to_ten:
    print("Line {}".format(each_value))