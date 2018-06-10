
"""
In a manner similar to that of the previous question (Lab11-2Q3), take the code you wrote for Lab8-1-2Q3 and modify it
so it imports the display_menu function which has been saved in a file called lab11_2.py .
Your code must use (by calling or invoking) the display_menu function to display the menu so comment out or delete
any existing code in Lab8-1-2Q3 that displayed the menu.

This is not the same menu as displayed by Q3.

Remember that the vm that execute your code is Linux based and so the filenames are case sensitive.

Run your program and ensure it displays the menu and that you can exit using option 9 as before.

Step 1.  Take the code you wrote for Lab8-1-2Q3 and either remove or comment out the code to print the menu.

Step 2.  Import the display_menu function from lab11_2.py.  you can choose how to import it.

Step 3.  When you want to display the menu, call/invoke display_menu().

Step 4.  Upload Lab11-2Q4.py to Moodle.  Do not upload the display_menu function code from lab11_2.py.  Do not upload
the lab11_2.py file.

Paste your code below.  Do not include the code for the display_menu function as Moodle has a copy of that already.

Example output.

Please select the number from one of the following options.
1) Enter a new item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
9) Exit
Option: 9
Bye.

"""
from lab11_2 import display_menu

# Auth: Michael Devenport
# Email: croxleyway@gmail.com

valid_selection = range(1, 6)
exit_selection = 9
selection = ""
option_prompt = "Option: "

singular_list_evaluation = "[{}] has been added to the list. There is now {} item in the list."
plural_list_evaluation = "[{}] has been added to the list. There are now {} items in the list."

items = []  # aggregate assignment list object, required outside of loop for compiling.

while any([not selection == exit_selection, selection in valid_selection]):

    display_menu()

    # Call to input function
    selection = int(input(option_prompt))

    # Assign options to var's
    enter_item = "Please enter new item: "          # option 1 input field prompt
    remove_one_item = "Remove an item."             # option 2
    count_items = "Display the number of items."    # option 3
    display_list = "Display a list of items."       # option 4
    remove_all_items = "Remove all items."          # option 5
    exit_statement = "Bye."                         # exit option 9

    if selection == 1:
        items.append(input(enter_item).strip())
    elif selection == 2:
        print(remove_one_item)
    elif selection == 3:
        print(count_items)
    elif selection == 4:
        print(display_list)
    elif selection == 5:
        print(remove_all_items)
    elif selection == 9:
        print(exit_statement)
    else:
        continue

    items_count = len(items)
    if all([items_count > 0, selection == 1]):
        if items_count == 1:
            print(singular_list_evaluation.format(items[-1], items_count))
        else:
            print(plural_list_evaluation.format(items[-1], items_count))
