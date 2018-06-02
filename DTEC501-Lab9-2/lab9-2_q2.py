"""
Write a program which reads the ReadMe.txt file which is in the same directory as your program and displays
the contents of that file in the following format:

1: Hi,
2: This is the ReadMe.txt file.
3: This is the end of the file.

There are no blank lines either at the start or the end of the output.

The example ReadMe.txt file can be found here.

Hints

Use the code fro the previous question as the basis for this one.
The code in slide 18 of Presentation 9-2 is still applicable.

"""

# Auth: Michael Devenport
# Email: croxleyway@gmail.com

# Lab9-2_q2

readme = "ReadMe.txt"
readme_file = open(readme)
count = 0
for each_line in readme_file:
    count += 1
    print("{}: {}".format(count, each_line), end="")

