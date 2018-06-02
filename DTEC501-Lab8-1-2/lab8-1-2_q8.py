"""
The customer has requested the following modification to the program.

If the user enters option 1 in order to enter a new item, check to see if the item is in the list.

In order to reduce the risk of error, remove any leading and/or trailing spaces.
You can assume the item is a sequence of alphanumeric characters and does not include any spaces (e.g. multiple words).

The item is not capitalised.

If the item they entered is not in the list then add it to the list and display the message
[<Item>] has been added to the list. There is/are now <Total> item(s) in the list.
where <Item> is the item they entered and <Total> is the total number of items now in the list.
The above must be grammatically correct e.g.
[Apple] has been added to the list. There is now 1 item in the list.
[Banana] has been added to the list. There are now 2 items in the list.

If the item they entered is already in the list then display the message

[<Item>] is in the list, it was not added.

where <Item> is the item the user entered.

Use your code from Q8 as the basis for this task.

Attempt to add items that already exist in the list.

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
Option: 4
Item 1: One
Item 2: Two
Item 3: Three

Please select the number from one of the following options.
1) Enter a new item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
9) Exit.
Option: 1
Please enter new item: Three
[Three] is in the list, it was not added.

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
Item 3: Three

Please select the number from one of the following options.
1) Enter a new item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
9) Exit.
Option: 1
Please enter new item: One
[One] is in the list, it was not added.

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
Item 3: Three

Please select the number from one of the following options.
1) Enter a new item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
9) Exit.
Option: 1
Please enter new item: Two
[Two] is in the list, it was not added.

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
Item 3: Three

Please select the number from one of the following options.
1) Enter a new item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
9) Exit.
Option: 9
Bye.

# "Please enter new item: "
#
#
#
"""
"""
Terminal Menu
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
    display_list_failure = "Sorry, the list is empty."                       # option 4 empty list
    remove_all_items = "All the items have been removed from the list."      # option 5 populated list( remove all )
    remove_all_items_failure = "Sorry, the list is empty."                   # option 5 empty list( remove all )
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
    elif selection == 2:

        element_num = int(input(remove_one_item))
        if all([element_num <= len(items), element_num > 0]):
            items.pop(element_num-1)
            print(element_deletion_success.format(element_num))
        else:
            print(element_deletion_failure.format(element_num))

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

