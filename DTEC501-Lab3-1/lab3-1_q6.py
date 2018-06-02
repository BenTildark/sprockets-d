"""
Write a program to ask the user to enter their first name.
Your program must display the following message:

Please enter your first name:

Your program must then display::

Pleased to meet you FirstName. I hope you are reading all the lab instructions FirstName!


Then ask the user to enter the course code:

FirstName, please enter the course code:
There are lots of instructions in the labs for the CourseCode course.
Make sure you create appropriately named variables FirstName.



Where FirstName is correctly capitalised and CourseCode is in upper case.



Example


Please enter your first name: dAVe
Pleased to meet you Dave. I hope you are reading all the lab instructions Dave!
Dave, please enter the course code: dTeC501
There are lots of instructions in the labs for the DTEC501 course.
Make sure you create appropriately named variables Dave.

"""

# The lines of text you need to use to generate the output are given below for you.  Do not alter anything inside the quotes.
# "Please enter your first name: "
# "Pleased to meet you {0}. I hope you are reading all the lab instructions {0}!"
# "{}, please enter the course code: "
# "There are lots of instructions in the labs for the {} course."
# "Make sure you create appropriately named variables {}."

"""
Loved it! This exercise lead to the python doc's 7.1 string, where I learnt about format(indices) in the Format
examples I found this( thought it's worth a share )

>>> '{0}{1}{0}'.format('abra', 'cad')
'abracadabra'

arguments' indices can be repeated. Very cool right?
"""

first_name = input("Please enter your first name: ").capitalize()

print("Pleased to meet you {0}. I hope you are reading all the lab instructions {0}!".format(first_name))

course_code = input( "{}, please enter the course code: ".format(first_name)).upper()

print("There are lots of instructions in the labs for the {} course.".format(course_code))

print("Make sure you create appropriately named variables {}.".format(first_name))