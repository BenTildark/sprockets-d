"""
Modify the code from Q3 and implement the logic to accommodate displaying a list of items
for the user when they select option 4.

Remove the line of code which displays the

Display a list of items.

message.

Modify the code at that point to do the following:

If there are one or more items in the list, display the list as follows:

Item 1: <Item1>
Item 2: <Item2>
Item 3: <Item3>
etc


If there are no items in the list display the following message:
Sorry, the list is empty.

All other options must generate their output as per Q4.

Attempt to display a list of items when the list is empty.

Please select the number from one of the following options.
1) Enter a new item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
9) Exit.
Option: 4
Sorry, the list is empty.

Please select the number from one of the following options.
1) Enter a new item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
9) Exit.
Option: 9
Bye.

Display a list of items for a populated list.

Please select the number from one of the following options.
1) Enter a new item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
9) Exit.
Option: 1
Please enter new item: One
[One] has been added to the list. There is now 1 item in the list.

Please select the number from one of the following options.
1) Enter a new item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
9) Exit.
Option: 1
Please enter new item: Two
[Two] has been added to the list. There are now 2 items in the list.

Please select the number from one of the following options.
1) Enter a new item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
9) Exit.
Option: 4
Item 1: One
Item 2: Two

Please select the number from one of the following options.
1) Enter a new item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
9) Exit.
Option: 9
Bye.
"""

# Auth: Michael Devenport
# Email: croxleyway@gmail.com

valid_selection = range(1, 6)
exit_selection = 9
selection = ""

blank_line = " "
selection_prompt = "Please select the number from one of the following options."
new_item_prompt = "1) Enter a new item."
remove_one_item_prompt = "2) Remove an item by its element number."
count_items_prompt = "3) Display the number of items in the list."
display_items_prompt = "4) Display a list of the items."
remove_all_items_prompt = "5) Remove all items from the list."
exit_prompt = "9) Exit."

option_prompt = "Option: "

singular_list_evaluation = "[{}] has been added to the list. There is now {} item in the list."
plural_list_evaluation = "[{}] has been added to the list. There are now {} items in the list."

# Create a list of menu options
menu_options = [
    new_item_prompt,
    remove_one_item_prompt,
    count_items_prompt,
    display_items_prompt,
    remove_all_items_prompt,
    exit_prompt
]

items = []  # to be aggregate assignment list object, required outside of loop for compiling.

while any([not selection == exit_selection, selection in valid_selection]):

    print(" ")
    print(selection_prompt)

    # Iterate our aggregate( menu_options )
    for constituent in menu_options:
        print(constituent)

    # Call to input function
    selection = int(input(option_prompt))

    # Assign options to var's
    enter_item = "Please enter new item: "              # option 1 input field prompt
    remove_one_item = "Remove an item."                 # option 2
    count_items = "Display the number of items."        # option 3
    display_list = "Item {}: {}"                        # option 4 is items in list
    display_list_failure = "Sorry, the list is empty."  # option 4 empty list
    remove_all_items = "Remove all items."              # option 5
    exit_statement = "Bye."                             # exit option 9

    if selection == 1:
        items.append(input(enter_item).strip())
    elif selection == 2:
        print(remove_one_item)
    elif selection == 3:
        print(count_items)
    elif all([selection == 4, len(items) >= 1]):
        count = 0
        for item in items:
            count += 1
            print(display_list.format(count, item))
    elif all([selection == 4, len(items) == 0]):
        print(display_list_failure)
    elif selection == 5:
        print(remove_all_items)
    elif selection == 9:
        print(exit_statement)
    else:
        continue

    if all([len(items) > 0, selection == 1]):
        if len(items) == 1:
            print(singular_list_evaluation.format(items[-1], len(items)))
        else:
            print(plural_list_evaluation.format(items[-1], len(items)))
