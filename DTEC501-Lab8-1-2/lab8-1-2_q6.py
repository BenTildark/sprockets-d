"""
Modify the code from Q6 and implement the logic to remove all items from the list when the user selects option 5.

Remove the line which displays the

Remove all items.

message.

Modify the code at that point to do the following:

If there are one or more items in the list, empty the list and display the message:

All the items have been removed from the list.

If there are no items in the list, display the message:

Sorry, the list is empty.

All other options must generate their output as per Q6.


Remove all items from a populated list.
=======================================
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
Option: 1
Please enter new item: Three
[Three] has been added to the list. There are now 3 items in the list.

Please select the number from one of the following options.
1) Enter a new item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
9) Exit.
Option: 3
There are 3 items in the list.

Please select the number from one of the following options.
1) Enter a new item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
9) Exit.
Option: 5
All the items have been removed from the list.

Please select the number from one of the following options.
1) Enter a new item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
9) Exit.
Option: 3
There are 0 items in the list.

Please select the number from one of the following options.
1) Enter a new item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
9) Exit.
Option: 1
Please enter new item: NewOne
[NewOne] has been added to the list. There is now 1 item in the list.

Please select the number from one of the following options.
1) Enter a new item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
9) Exit.
Option: 3
There is 1 item in the list.

Please select the number from one of the following options.
1) Enter a new item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
9) Exit.
Option: 9
Bye.

Attempt to delete all items from an empty list.
===============================================
Please select the number from one of the following options.
1) Enter a new item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
9) Exit.
Option: 3
There are 0 items in the list.

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
Option: 5
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
    enter_item = "Please enter new item: "                                  # option 1 input field prompt
    remove_one_item = "Remove an item."                                     # option 2
    count_item = "There is {} item in the list."                            # option 3 only 1 item in list
    count_items = "There are {} items in the list."                         # option 3 zero or more than 1 item in list
    display_list = "Item {}: {}"                                            # option 4 is items in list
    display_list_failure = "Sorry, the list is empty."                      # option 4 empty list
    remove_all_items = "All the items have been removed from the list."     # option 5 populated list( remove all )
    remove_all_items_failure = "Sorry, the list is empty."                  # option 5 empty list( remove all )
    exit_statement = "Bye."                                                 # exit option 9

    if selection == 1:
        items.append(input(enter_item).strip())
    elif selection == 2:
        print(remove_one_item)
    elif all([selection == 3, len(items) == 1]):
        print(count_item.format(len(items)))
    elif all([selection == 3, not len(items) == 1]):
        print(count_items.format(len(items)))
    elif all([selection == 4, len(items) >= 1]):
        count = 0
        for item in items:
            count += 1
            print(display_list.format(count, item))
    elif all([selection == 4, len(items) == 0]):
        print(display_list_failure)
    elif all([selection == 5, len(items) > 0]):
        items.clear()
        print(remove_all_items)
    elif all([selection == 5, not items]):  # not items will evaluate to True if list empty
        print(display_list_failure)
    elif selection == 9:
        print(exit_statement)
    else:
        continue

    if all([len(items) > 0, selection == 1]):
        if len(items) == 1:
            print(singular_list_evaluation.format(items[-1], len(items)))
        else:
            print(plural_list_evaluation.format(items[-1], len(items)))
