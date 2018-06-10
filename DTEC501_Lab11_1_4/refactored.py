# REFACTORED CODE lab_11_1_4.py IMPROVED TESTS


def check_computer_name(entry):

    """returns True if valid computer name for block S computing"""

    valid_pc_name = []

    block = "S"
    valid_room = {'1': '264', '2': '265', '3': '267', '4': '268'}

    count_twenty_two = ['2']

    for key in valid_room:
        if key not in count_twenty_two:
            pc_number = range(1, 21)
        else:
            pc_number = range(1, 23)
        for i in pc_number:
            if i in range(1, 10):
                i = "0" + str(i)
            valid_pc = block + valid_room[key] + "-" + str(i)
            valid_pc_name.append(valid_pc)

    # validate True if entry in our list
    if entry.replace('"', '') in valid_pc_name:
        return True
    else:
        return False


# TESTING: all tests should follow the "> True > False > False > True" convention to pass.

# check inside outside param requirement for our room with 22 pc's
pcn_22 = ['22', '23', '00', '01']
for pcn_y in pcn_22:
    print("S265-{}".format(pcn_y))
    print(check_computer_name("S265-{}".format(pcn_y)))  # > True > False > False > True

# check inside outside param requirement for all rooms with 20 pc's
rm_20 = ['S264', 'S267', 'S268']
pcn_20 = ['20', '21', '00', '01']
for rm in rm_20:
    for pcn_z in pcn_20:
        print("{}-{}".format(rm, pcn_z))
        print(check_computer_name("{}-{}".format(rm, pcn_z)))

# development env test results

"""

S265-22
True
S265-23
False
S265-00
False
S265-01
True
S264-20
True
S264-21
False
S264-00
False
S264-01
True
S267-20
True
S267-21
False
S267-00
False
S267-01
True
S268-20
True
S268-21
False
S268-00
False
S268-01
True

Process finished with exit code 0

"""

# REM: blot out tests before running this...
# py3 -c 'from refactored import check_computer_name; print("\n" + check_computer_name.__doc__ + "\n"); print(check_computer_name("S265-08"))'

# MOODLE TEST RESULTS

"""
TechLabs needs a function to test the validity of the student computer names in the rooms.

The rooms that TechLabs uses are: S264, S265, S267 and S268.

 

The format of the computer name is

BuildingRoom-ComputerNumber

Building is currently "S" for S block.  Building is always upper case.

Room can be one of 264, 265, 267 or 268.

The - is a significant character and is always in the 4th position in the string.

ComputerNumber varies from 01 to 22 depending on the room. All rooms have 20 student computers except S265 which has 22.  ComputerNumber is always 2 digits.

 

Examples of valid computer names are

S264-01

S264-20

Create a function called check_computer_name

check_computer_name has 1 parameter

check_computer_name returns True if the string it received represents a valid computer name.

check_computer_name returns False if the string it received does not represent a valid computer name.

 

It is advisable that the code in your function be written in a manner which allows TechLabs to expand into other buildings.  For this question though, only S block will be used.

 

Hints.

Think about the requirements and how they map onto conditional statements.
The conditional statements are not complex, subsequently there is no need for complex nested conditional statements.
After the variables have been declared, the main section of code is about 17 lines in length.
Remember how to use the index to get to individual characters in a string.
 

Examples
 
print(check_computer_name("S264-01"))

True

 

print(check_computer_name("S264-00"))

False

 

print(check_computer_name("X264-00"))

False

 

 

Post the function code below, not your testing code.

 

Answer:(penalty regime: 10, 20, ... %)


Feedback
Test	Expected	Got	
Correct	
print(check_computer_name("S264-01"))
True
True
Correct
Correct	
print(check_computer_name("S264-20"))
True
True
Correct
Correct	
print(check_computer_name("S265-01"))
True
True
Correct
Correct	
print(check_computer_name("S265-22"))
True
True
Correct
Correct	
print(check_computer_name("S267-01"))
True
True
Correct
Correct	
print(check_computer_name("S267-20"))
True
True
Correct
Correct	
print(check_computer_name("S268-01"))
True
True
Correct
Correct	
print(check_computer_name("S268-20"))
True
True
Correct
Correct	
print(check_computer_name("S264-00"))
False
False
Correct
Correct	
print(check_computer_name("S264-21"))
False
False
Correct
Correct	
print(check_computer_name("S265-00"))
False
False
Correct
Correct	
print(check_computer_name("S265-23"))
False
False
Correct
Correct	
print(check_computer_name("S267-00"))
False
False
Correct
Correct	
print(check_computer_name("S267-21"))
False
False
Correct
Correct	
print(check_computer_name("S268-00"))
False
False
Correct
Correct	
print(check_computer_name("S268-21"))
False
False
Correct
Correct	
print(check_computer_name("S263-01"))
False
False
Correct
Correct	
print(check_computer_name("S263-20"))
False
False
Correct
Correct	
print(check_computer_name("X264-20"))
False
False
Correct
Correct	
if (check_computer_name.__doc__):
    print("docstring present")
else:
    print("docstring not present")
docstring present
docstring present
Correct
Correct	
# Check the return type
pc_id = "S263-20"
valid_pc = check_computer_name(pc_id)
if type(valid_pc) == bool:
    print("The function returned a boolean. :-)")
else:
    print("The function did not return a boolean. :-(")
The function returned a boolean. :-)
The function returned a boolean. :-)
Correct
Correct	
print(check_computer_name("s264-20"))
False
False
Correct
Correct	
print(check_computer_name("S-26420"))
False
False
Correct
Correct	
print(check_computer_name("S-264-20"))
False
False
Correct
Correct	
print(check_computer_name("S264-1"))
False
False
Correct
Passed all tests!  Correct
"""