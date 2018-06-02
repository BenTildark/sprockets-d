"""
The customer has requested the following modification to the program.

If the user enters option 1 (Enter a new item) then check to see if the item is already in the list..

If the item is already in the list, ask the user to confirm that they want it to be added.
If they confirm they want it to be added, append the item to the list.

If the item is not already in the list, append the item to the list.

The customer has requested that the menu message be changed from

1) Enter a new item.

to

1) Enter an item.

and the prompt to enter the item to be changed from

Please enter new item:

to

Please enter the item:


Hints.

The enter an item section is now 19 lines of code not including blank lines and comments.
When looking at the confirmation input, only check to see if the character is a letter Y.
Removing any spaces and converting it to lower case is suggested.
There is no need for a loop to validate the input, nor is one expected.
There are a few ways of implementing the code.
One of the shorter ways will result in about 20 lines of code for this section.
Ideally have only one instance of each of the following lines in your "enter item" code.
"[{}] is already in the list, please confirm that want to add another [Y/N]: "
"[{}] has been added to the list. There is now {} item in the list."
"[{}] has been added to the list. There are now {} items in the list."
"[{}] was not added."
Ideally have only one instance of appending the new item to the list. Any more would indicate code duplication.

Attempt to add an existing item but then decline to add it.

Please select the number from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
9) Exit.
Option: 1
Please enter the item: ItemOne
[ItemOne] has been added to the list. There is now 1 item in the list.

Please select the number from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
9) Exit.
Option: 1
Please enter the item: ItemTwo
[ItemTwo] has been added to the list. There are now 2 items in the list.

Please select the number from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
9) Exit.
Option: 1
Please enter the item: ItemOne
[ItemOne] is already in the list, please confirm that want to add another [Y/N]: N
[ItemOne] was not added.

Please select the number from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
9) Exit.
Option: 4
Item 1: ItemOne
Item 2: ItemTwo

Please select the number from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
9) Exit.
Option: 9
Bye.

Successfully add an existing item to the list.

Please select the number from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
9) Exit.
Option: 1
Please enter the item: ItemOne
[ItemOne] has been added to the list. There is now 1 item in the list.

Please select the number from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
9) Exit.
Option: 1
Please enter the item: ItemTwo
[ItemTwo] has been added to the list. There are now 2 items in the list.

Please select the number from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
9) Exit.
Option: 1
Please enter the item: ItemThree
[ItemThree] has been added to the list. There are now 3 items in the list.

Please select the number from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
9) Exit.
Option: 1
Please enter the item: ItemTwo
[ItemTwo] is already in the list, please confirm that want to add another [Y/N]: y
[ItemTwo] has been added to the list. There are now 4 items in the list.

Please select the number from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
9) Exit.
Option: 4
Item 1: ItemOne
Item 2: ItemTwo
Item 3: ItemThree
Item 4: ItemTwo

Please select the number from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
9) Exit.
Option: 1
Please enter the item: Itemone
[Itemone] has been added to the list. There are now 5 items in the list.

Please select the number from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
9) Exit.
Option: 4
Item 1: ItemOne
Item 2: ItemTwo
Item 3: ItemThree
Item 4: ItemTwo
Item 5: Itemone

Please select the number from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
9) Exit.
Option: 9
Bye.

"""

"""
Terminal Menu #10
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
new_item_prompt = "1) Enter an item."
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
    enter_item_prompt = "Please enter the item: "                                    # option 1 input field prompt
    append_confirmation_prompt = "[{}] is already in the list," \
                                 " please confirm that want to add another [Y/N]: "  # option 1 confirmation prompt
    append_true = 'y'                                                                # option 1 confirm & proceed

    list_addition_singular = "[{}] has been added to the list." \
                             " There is now {} item in the list."             # singular statement for option 1 success
    list_addition_plural = "[{}] has been added to the list." \
                           " There are now {} items in the list."             # plural statement for option 1 success
    list_addition_failure = "[{}] was not added."                             # option 1 return confirm False
    remove_one_item = "Please enter the" \
                      " element number of the item to remove: "               # option 2 int input field prompt
    element_deletion_success = "Element {} has been removed from the list."   # return statement for option 2 success
    element_deletion_failure = "Sorry element {}" \
                               " does not exist in the list."                 # return statement for option 2 failure
    count_item_singular = "There is {} item in the list."                     # option 3 only 1 item in list
    count_item_plural = "There are {} items in the list."                     # option 3 zero / more than 1 item in list
    display_list = "Item {}: {}"                                              # option 4 is items in list
    list_failure = "Sorry, the list is empty."                                # options 4 & 5 empty list return
    remove_all_items = "All the items have been removed from the list."       # option 5 populated list( remove all )

    exit_statement = "Bye."                                                   # exit option 9

    if selection == 1:
        item_new = input(enter_item_prompt).replace(' ', '').strip()
        if item_new not in items:
            items.append(item_new)
            selection = ''
            if len(items) == 1:
                print(list_addition_singular.format(item_new, len(items)))
            else:
                print(list_addition_plural.format(item_new, len(items)))
        else:
            confirmation_choice = input(append_confirmation_prompt.format(item_new)).strip().lower()
            if confirmation_choice == append_true:
                items.append(item_new)
                selection = ''
                if len(items) == 1:
                    print(list_addition_singular.format(item_new, len(items)))
                else:
                    print(list_addition_plural.format(item_new, len(items)))
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
        print(count_item_singular.format(len(items)))
    elif all([selection == 3, not len(items) == 1]):
        print(count_item_plural.format(len(items)))

    elif all([selection == 4, len(items) >= 1]):
        count = 0
        for item in items:
            count += 1
            print(display_list.format(count, item))
    elif all([selection == 4, len(items) == 0]):  # 'len(items) == 0' will evaluate to True if list empty
        print(list_failure)

    elif all([selection == 5, len(items) > 0]):
        items.clear()
        print(remove_all_items)
    elif all([selection == 5, not items]):  # 'not items' will evaluate to True if list empty
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

