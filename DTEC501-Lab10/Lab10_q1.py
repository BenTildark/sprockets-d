"""
Modify the code supplied and add exception handling code to prevent any exceptions that might arise from the
following actions

Entering an option
Creating a directory
Removing a directory

Examples of exceptions could be

Entering a non-numeric option
Pressing the enter key (non numeric)
Entering a key word (nine)
Attempting to create a directory where you don't have permissions.  On the Ara pc's, this could be attempting
to create C:\YourName
Attempting to remove an existing empty directory where you don't have permissions to do so.  On the Ara pc's,
this could be attempting to remove an empty directory underneath C:\Windows on the Ara pc's.

As JobEngine is a Linux vm, do not hard code any paths in your code.  The only task you have to do is add
exception handling code.

Hint.

Look for the keyword "try" in the comments.  Remember how that keyword relates to an exception handler.
=========================================================================================================

# The line of text you need to use to generate the output is given below for you.
Do not alter anything inside the quotes.
# " "
# "Please select the number from one of the following options."
# "1) Create a directory."
# "2) Remove a directory."
# "9) Exit"
# "Option: "
# "The option must be an integer."                           valueError++++++++++++++++++
# "Please enter the name of the directory to be created: "
# "Sorry, {} is already present."
# "An error occurred while attempting to create the dir."
# "{} has been created."
# "Please enter the name of the directory to be removed: "
# "Can't delete dir, subordinates present."
# "An error occurred while attempting to delete the dir."    permissionsError++++++++++++
# "{} has been removed."
# "Sorry, {} does not exist."


EXAMPLES:

Create and remove a directory.

Please select the number from one of the following options.
1) Create a directory.
2) Remove a directory.
9) Exit
Option: 1
Please enter the name of the directory to be created: temp
temp has been created.

Please select the number from one of the following options.
1) Create a directory.
2) Remove a directory.
9) Exit
Option: 2
Please enter the name of the directory to be removed: temp
temp has been removed.

Please select the number from one of the following options.
1) Create a directory.
2) Remove a directory.
9) Exit
Option: 9
Bye.

Create a directory and attempt to create it again.

Please select the number from one of the following options.
1) Create a directory.
2) Remove a directory.
9) Exit
Option: 1
Please enter the name of the directory to be created: temp
temp has been created.

Please select the number from one of the following options.
1) Create a directory.
2) Remove a directory.
9) Exit
Option: 1
Please enter the name of the directory to be created: temp
Sorry, temp is already present.

Please select the number from one of the following options.
1) Create a directory.
2) Remove a directory.
9) Exit
Option: 9
Bye.

Attempt to remove a directory that has a subordinate.

Please select the number from one of the following options.
1) Create a directory.
2) Remove a directory.
9) Exit
Option: 1
Please enter the name of the directory to be created: temp1
temp has been created.

Please select the number from one of the following options.
1) Create a directory.
2) Remove a directory.
9) Exit
Option: 1
Please enter the name of the directory to be created: temp1/temp2
temp/temp has been created.

Please select the number from one of the following options.
1) Create a directory.
2) Remove a directory.
9) Exit
Option: 2
Please enter the name of the directory to be removed: temp1
Can't delete dir, subordinates present.

Please select the number from one of the following options.
1) Create a directory.
2) Remove a directory.
9) Exit
Option: 9
Bye.

"""
# Auth: Michael Devenport
# croxleyway@gmail.com

# Lab10-1Q1

import os

# Initialize variables
option = 0

create_directory = 1
remove__directory = 2
exit_option = 9

no_dir_entries = 0

while option != exit_option:
    # Display the menu
    print(" ")
    print("Please select the number from one of the following options.")
    print("1) Create a directory.")
    print("2) Remove a directory.")
    print("9) Exit")

    option = input("Option: ")

    try:
        option = int(option)
    except ValueError:
        print("The option must be an integer.")
    else:
        try:
            if option == create_directory:
                # Create a directory option
                dir_name = input("Please enter the name of the directory to be created: ")
                dir_present = os.path.exists(dir_name)

                if dir_present:
                    # Entered directory is already present, can't create it
                    print("Sorry, {} is already present.".format(dir_name))

                else:
                    # Entered directory is not present, try to create it
                    os.mkdir(dir_name)
                    print("{} has been created.".format(dir_name))

            elif option == remove__directory:
                # Remove a directory option
                dir_name = input("Please enter the name of the directory to be removed: ")
                dir_present = os.path.exists(dir_name)

                if dir_present:
                    # Entered directory is already present, get subordinates
                    dir_contents = os.listdir(dir_name)

                    if len(dir_contents) != no_dir_entries:
                        # Entered directory is not empty, it can't be removed
                        print("Can't delete dir, subordinates present.")

                    else:
                        # Entered directory is empty, try to remove it
                        try:
                            os.rmdir(dir_name)
                            print("{} has been removed.".format(dir_name))
                        except PermissionError:
                            print("An error occurred while attempting to delete the dir.")
                else:
                    # Entered directory is not present, it can't be removed
                    print("Sorry, {} does not exist.".format(dir_name))
        except PermissionError:
            print("Oh no, permissions error was raised, naughty you!")

print("Bye.")
