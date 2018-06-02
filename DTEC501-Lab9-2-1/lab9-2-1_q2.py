"""
Write a program to read the data in the userdata.txt file and display the data it contains.

The file is in the same directory as the program.

As per the previous question, the data is written as follows

Initial of first name followed by last name followed by age.  Age is always two characters.

There is no CrLf at the end of the line.

Example
Initial of the first name is: Y
The last name is: Person
The age is: 18

Example
Initial of the first name is: O
The last name is: Person
The age is: 42

In the first example above, userdata.txt will contain

YPerson18

In the second example above, userdata.txt will contain

OPerson42

Hints

The string you get from the file needs to be sliced into the three sections.
There is no user input to this program.
The solution is about 14 lines of code.

"""

# Auth: Michael Devenport
# Email: croxleyway@gmail.com

# Quest: lab9-2-1_q2

raw_data = open("userdata.txt", "r")

user_data = raw_data.read()

initial, last, age = user_data[:1], user_data[1:-2], user_data[-2:]

print("Initial of the first name is: {}".format(initial))
print("The last name is: {}".format(last))
print("The age is: {}".format(age))

raw_data.close()
