"""
Write a program which reads the ReadMe.txt file which is in the same directory as your program and displays
the contents of that file in the following format:

['Hi,\n', 'This is the ReadMe.txt file.\n', 'This is the end of the file.\n']

There are no blank lines either at the start or the end of the output.

The example ReadMe.txt file can be found here.

Hint.

See slide 17 of Presentation 9-2.

"""
# Auth: Michael Devenport
# Email: croxleyway@gmail.com

# Lab9-2_q1

readme = "ReadMe.txt"
readme_file = open(readme)
read_all = readme_file.readlines()
print("{}".format(read_all))
