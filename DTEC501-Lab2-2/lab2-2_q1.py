"""
The questions in this lab require more than one item to be displayed on one line.
The code from Presentation 2-3 is applicable here.



# Written by Dave Bracken
# Dave.Bracken@ara.ac.nz

course_code = "DTEC501"
your_name = input("What is your name? ")
print("Hi ", your_name, ", welcome to ", course_code, ".", sep='')



What is your name? Dave
Hi Dave, welcome to DTEC501.

# The lines of text you need to use to generate the output are given below for you.  Do not alter anything inside the quotes.
# "Please enter an integer: "
# "The answer to "
#  " + 1 is "

Example output
Please enter an integer: 15
The answer to 15 + 1 is 16
"""
"""
PRINT ON SAME LINE 

Turns out only python3 have keywords arguments for print() & my project interpreter was py2.7. PyCharm. During googling 
I found all these keywords we can use -  needed to import sys for(file=sys.stdout). I understand sep= & end, but still
have some reading up to do on the other two. 
"""
import sys

first_addend = int(input("Please enter an integer: "))
sum = first_addend + 1

print("The answer to ", first_addend, " + 1 is ", sum, sep="", end="", file=sys.stdout, flush=True)
