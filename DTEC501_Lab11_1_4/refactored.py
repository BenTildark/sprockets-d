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


# REM: blot out tests before running this...
# py3 -c 'from refactored import check_computer_name; print("\n" + check_computer_name.__doc__ + "\n"); print(check_computer_name("S265-08"))'
