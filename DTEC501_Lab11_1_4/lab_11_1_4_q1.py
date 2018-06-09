"""
Your code must be commented.

Your function must include an appropriate docstring.

*************************************************

TechLabs needs a function to test the validity of the student computer names in the rooms.

The rooms that TechLabs uses are: S264, S265, S267 and S268.

The format of the computer name is

BuildingRoom-ComputerNumber

Building is currently "S" for S block.  Building is always upper case.

Room can be one of 264, 265, 267 or 268.

The - is a significant character and is always in the 4th position in the string.

ComputerNumber varies from 01 to 22 depending on the room. All rooms have 20 student computers except S265 which has 22.
ComputerNumber is always 2 digits.


Examples of valid computer names are

S264-01

S264-20

Create a function called check_computer_name

check_computer_name has 1 parameter

check_computer_name returns True if the string it received represents a valid computer name.

check_computer_name returns False if the string it received does not represent a valid computer name.

It is advisable that the code in your function be written in a manner which allows
TechLabs to expand into other buildings.  For this question though, only S block will be used.


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
"""


def check_computer_name(entry):
    
    """returns true if valid computer name for block S computing"""

    # initializing variables
    block = "S"
    valid_room_20 = ['264', '267', '268']
    valid_room_22 = ['265']
    one_to_20 = range(1, 21)
    one_to_22 = range(1, 23)

    # set list assignment for compiling valid computer names
    valid_pc_name = []

    # hash out valid computer name & store in valid_pc_name
    for room_number in valid_room_20:
        for pc_number in one_to_20:
            if pc_number in range(1, 10):
                pc_number = "0" + str(pc_number)
            valid_pc = block + room_number + "-" + str(pc_number)
            valid_pc_name.append(valid_pc)

    for room_number in valid_room_22:
        for pc_number in one_to_22:
            if pc_number in range(1,10):
                pc_number = "0" + str(pc_number)
            valid_pc = block + room_number + "-" + str(pc_number)
            valid_pc_name.append(valid_pc)

    # validate True if entry in our list
    if entry.replace('"', '') in valid_pc_name:
        return True
    else:
        return False


# Debugging

print(check_computer_name("S264-22"))
# py3 -c 'from lab_11_1_4_q1 import check_computer_name; print("\n" + check_computer_name.__doc__ + "\n"); print(check_computer_name("S265-08"))'