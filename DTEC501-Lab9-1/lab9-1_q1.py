"""
Display a directory listing of your current working directory.
It doesn't matter what or where your current working directory is.

The program will run from the current working directory, it is not important which directory that is.

For Moodle, as the code will be executed in a Linux vm, do not hard code any specific paths.

Hints.
Use slide 17 from Presentation 9-1 as the basis for this question.
The solution is 16 lines long.
The ideal solution has only one instance of print("{}: {} is a {}".format(...))
with one if statement with no else inside the loop.
You only need to check to see if the item is a file or a directory, choose one.  See slides 20 & 21
of Presentation 9-1.
Remember the use of singular and plural.

Example.
There are 4 items in your current working directory.
1: ReadMe.txt is a file.
2: Data is a directory.
3: PythonSource is a directory.
4: Lab9-1Q1.py is a file.

Example.
There is 1 item in your current working directory.
1: Lab9-1Q1.py is a file.

Example.
There are 2 items in your current working directory.
1: Lab9-1Q1.py is a file.
2: SourceCode is a directory.

"""
# Auth: Michael Devenport
# Email: croxleyway@gmail.com
# Lab9-1_q1
import os

return_singular = "There is {} item in your current working directory."
return_plural = "There are {} items in your current working directory."
return_subordinate_type = "{}: {} is a {}."

dir_content = os.listdir(os.getcwd())

print(return_singular.format(len(dir_content)) if dir_content == 1 else return_plural.format(len(dir_content)))
count = 0
for sub in dir_content:
    count += 1
    print(return_subordinate_type.format(count, sub, "directory") if os.path.isdir(sub)
          else return_subordinate_type.format(count, sub, "file"))

# OUTPUT: Py# 3.6
# There are 3 items in your current working directory.
# 1: .idea is a directory.
# 2: lab9-1_q1.py is a file.
# 3: venv is a directory.

# Process finished with exit code 0
