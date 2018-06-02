"""
The customer has requested the following modification to the program.

If the user enters option 2 (Remove an item by its element number) then only ask the user to enter the element
number of the item to be deleted if the list has one or more items in it.

If there are one or more items in the list then display the message

Please enter the element number of the item to remove:

The user will enter the element number of the item they want removed from the list.

If the user enters an element number that is valid (there is an element in the list with that number) then delete
the element from the list and display the message:

Element <EnteredElementNumber> has been removed from the list.

If the user enters an element number that is not valid (there isn't an element in the list with that number)
then display the message:

Sorry element <EnteredElementNumber> does not exist in the list.

where <EnteredElementNumber> is the element number the user entered.

If there are no items in the list then display the message

Sorry, the list is empty.

Add two items to the list.  Attempt to remove an invalid element. Delete a present element, then exit.

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
Option: 2
Please enter the element number of the item to remove: 0
Sorry element 0 does not exist in the list.

Please select the number from one of the following options.
1) Enter a new item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
9) Exit.
Option: 2
Please enter the element number of the item to remove: 1
Element 1 has been removed from the list.

Please select the number from one of the following options.
1) Enter a new item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
9) Exit.
Option: 4
Item 1: Two

Please select the number from one of the following options.
1) Enter a new item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
9) Exit.
Option: 9
Bye.

Attempt to delete an element/item from an empty list.

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
Option: 2
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

# "Please enter the element number of the item to remove: "
# "Element {} has been removed from the list."
# "Sorry element {} does not exist in the list."
# "Sorry, the list is empty."

"""
Terminal Menu #9
=============
Written on: April 17 2018
Developed by: Michael Devenport
Email: croxleyway@gmail.com
"""

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

    # Assign options input strings & statements to var's
    enter_item = "Please enter new item: "                                   # option 1 input field prompt
    list_addition_singular = "[{}] has been added to the list." \
                             " There is now {} item in the list."            # singular statement for option 1 success
    list_addition_plural = "[{}] has been added to the list." \
                           " There are now {} items in the list."            # plural statement for option 1 success
    list_addition_failure = "[{}] is in the list, it was not added."         # item exists in list return option 1
    remove_one_item = "Please enter the" \
                      " element number of the item to remove: "              # option 2 int input field prompt
    element_deletion_success = "Element {} has been removed from the list."  # return statement for option 2 success
    element_deletion_failure = "Sorry element {}" \
                               " does not exist in the list."                # return statement for option 2 failure
    count_item = "There is {} item in the list."                             # option 3 only 1 item in list
    count_items = "There are {} items in the list."                          # option 3 zero or more than 1 item in list
    display_list = "Item {}: {}"                                             # option 4 is items in list
    list_failure = "Sorry, the list is empty."                              # options 4 & 5 empty list return
    remove_all_items = "All the items have been removed from the list."      # option 5 populated list( remove all )

    exit_statement = "Bye."                                                  # exit option 9

    if selection == 1:
        item_new = input(enter_item).replace(' ', '').strip()

        if item_new not in items:
            items.append(item_new)
            if len(items) == 1:
                print(list_addition_singular.format(item_new, len(items)))
                selection = ''
            else:
                print(list_addition_plural.format(item_new, len(items)))
                selection = ''
        else:
            print(list_addition_failure.format(item_new))
            selection = ''
    elif all([selection == 2, len(items) > 0]):

        element_num = int(input(remove_one_item))
        if all([element_num <= len(items), element_num > 0]):
            items.pop(element_num-1)
            print(element_deletion_success.format(element_num))
        else:
            print(element_deletion_failure.format(element_num))
    elif all([selection == 2, len(items) == 0]):
        print(list_failure)

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
        print(list_failure)

    elif all([selection == 5, len(items) > 0]):
        items.clear()
        print(remove_all_items)
    elif all([selection == 5, not items]):  # not items will evaluate to True if list empty
        print(list_failure)

    elif selection == 9:
        print(exit_statement)
    else:
        continue

    if all([len(items) > 0, selection == 1]):
        if len(items) == 1:
            print(singular_list_evaluation.format(items[-1], len(items)))
        else:
            print(plural_list_evaluation.format(items[-1], len(items)))

