"""
Write a program to loop from 1 to 10 inclusively in steps of 2.

Use a for loop for this task.

Each time you go around the loop, the program should display

Line x

where x is the loop counter.



Example


Line 1
Line 3
Line 5
Line 7
Line 9

"""

# The line of text you need to use to generate the output is given below for you.  Do not alter anything inside the quotes.
# "Line {}"

step2_1_to_10 = range(1, 11, 2)
for count in step2_1_to_10:
    print("Line {}".format(count))