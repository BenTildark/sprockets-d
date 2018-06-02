"""
Write a program which counts the number of comment lines in the file specified by the user.

The files specified are assumed to be in the same directory as the program.
Do not hard code any directories in your code as the vm (JobEngine) that executes your code for Moodle is a Linux
machine and does not understand Windows paths.

Example
Please enter the name of file to checked: NoSuchFile.txt
Sorry, I can't see a file called NoSuchFile.txt.

Example
Please enter the name of file to checked: 4comments4lines.txt
4comments4lines.txt contains 4 comment lines out of 4 lines in total.

Example
Please enter the name of file to checked: 3comments4lines.txt
3comments4lines.txt contains 3 comment lines out of 4 lines in total.

Example
Please enter the name of file to checked: 1comment4lines.txt
1comment4lines.txt contains 1 comment line out of 4 lines in total.

Where the scenarios in the examples above are ...

NoSuchFile.txt was not present in the current directory.

4comments4lines.txt contains

# Lab8-2Q3
# Dave Bracken, Dave.Bracken@ara.ac.nz
# 01/02/18
# print("4 lines of comments, 4 lines in total.")

3comments4lines.txt contains

# Lab8-2Q3
# Dave Bracken, Dave.Bracken@ara.ac.nz
# 01/02/18
print("3 lines of comments, 4 lines in total.")

1comment4lines.txt contains

# print("# Lab8-2Q3")
print("# Dave Bracken, Dave.Bracken@ara.ac.nz")
print("# 01/02/18")
print("# 1 line of comments, 4 lines in total.")

The files specified above are available  here

Hints.

See Presentation 9-1 for example code to check for presence of a file.
See Presentation 9-2 slide 18 for code to read multiple lines from a file.
Remember startswith()
The correct grammatical use of singular and plural phrases is required.
The solution is about 20 lines of code.

# "Please enter the name of file to checked: "
# "{} contains {} comment line out of {} lines in total."
# "{} contains {} comment lines out of {} lines in total."
# "Sorry, I can't see a file called {}."

"""
# Auth: Michael Devenport
# Email: croxleyway@gmail.com

# Lab9-2_q3

import os

test_file = input("Please enter the name of file to checked: ")

if not os.path.exists(test_file):
    print("Sorry, I can't see a file called {}.".format(test_file))
else:
    open_file = open(test_file)
    line_count, comment_count = 0, 0
    for line in open_file:
        line_count += 1
        if line.startswith('#'):
            comment_count += 1

    print("{} contains {} comment line out of {} lines in total.".format(test_file, comment_count, line_count)
          if comment_count == 1
          else "{} contains {} comment lines out of {} lines in total.".format(test_file, comment_count, line_count))
