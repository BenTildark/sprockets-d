"""
The customer has requested the following modification to the program.

Add an option to report the number of times an item is in the list.

Hints.

This section is about 10 lines of code not including blank lines and comments.
Strip any spaces from the item that is entered.

Entering items then counting the instances of them.

Please select the number from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
6) Count the instances of an item in the list.
9) Exit.
Option: 1
Please enter the item: one
[one] has been added to the list. There is now 1 item in the list.

Please select the number from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
6) Count the instances of an item in the list.
9) Exit.
Option: 1
Please enter the item: two
[two] has been added to the list. There are now 2 items in the list.

Please select the number from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
6) Count the instances of an item in the list.
9) Exit.
Option: 1
Please enter the item: one
[one] is already in the list, please confirm that want to add another [Y/N]: y
[one] has been added to the list. There are now 3 items in the list.

Please select the number from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
6) Count the instances of an item in the list.
9) Exit.
Option: 6
Please enter the item: one
There are 2 instances of [one] in the list.

Please select the number from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
6) Count the instances of an item in the list.
9) Exit.
Option: 6
Please enter the item: two
There is 1 instance of [two] in the list.

Please select the number from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
6) Count the instances of an item in the list.
9) Exit.
Option: 9
Bye.

Attempt to counting instances of an item with an empty list.

Please select the number from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
6) Count the instances of an item in the list.
9) Exit.
Option: 4
Sorry, the list is empty.

Please select the number from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
6) Count the instances of an item in the list.
9) Exit.
Option: 6
Sorry, the list is empty.

Please select the number from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
6) Count the instances of an item in the list.
9) Exit.
Option: 9
Bye.

"""

# "Please enter the item: "
# "There is {} instance of [{}] in the list."
# "There are {} instances of [{}] in the list."
# "Sorry, the list is empty."
# "6) Count the instances of an item in the list."

"""
Terminal Menu #11
=============
Written on: April 17 2018
Developed by: Michael Devenport
Email: croxleyway@gmail.com

Changed program layout ( removed all assignments within while loop logic, set all variables just below ;-)
Found the BUG' <duplicate strings assigned to multiple var's & even dupe output execution code, Removed!> 
*re: Bug, was able to remove my work around 'setting selection var to nil'

Adding Option 6 to menu..
"""

valid_selection = range(1, 6)
exit_selection = 9
selection = ""

# Main menu prompt/input assignments
blank_line = " "
selection_prompt = "Please select the number from one of the following options."
item_prompt = "1) Enter an item."
remove_one_item_prompt = "2) Remove an item by its element number."
count_items_prompt = "3) Display the number of items in the list."
display_items_prompt = "4) Display a list of the items."
remove_all_items_prompt = "5) Remove all items from the list."
instance_count_prompt = "6) Count the instances of an item in the list."
exit_prompt = "9) Exit."

option_prompt = "Option: "

# Option input/function & return statement assignments
enter_item_prompt = "Please enter the item: "                                    # option 1 input field prompt
append_confirmation_prompt = "[{}] is already in the list," \
                             " please confirm that want to add another [Y/N]: "  # option 1 confirmation prompt
append_true = 'y'                                                                # option 1 confirm & proceed

list_addition_singular = "[{}] has been added to the list." \
                         " There is now {} item in the list."                 # singular statement for option 1 success
list_addition_plural = "[{}] has been added to the list." \
                       " There are now {} items in the list."                 # plural statement for option 1 success
list_addition_failure = "[{}] was not added."                                 # option 1 return confirm False
remove_one_item = "Please enter the" \
                  " element number of the item to remove: "                   # option 2 int input field prompt
element_deletion_success = "Element {} has been removed from the list."       # return statement for option 2 success
element_deletion_failure = "Sorry element {}" \
                           " does not exist in the list."                     # return statement for option 2 failure
count_item_singular = "There is {} item in the list."                         # option 3 only 1 item in list
count_item_plural = "There are {} items in the list."                         # option 3 zero / more than 1 item in list
display_list = "Item {}: {}"                                                  # option 4 is items in list
list_failure = "Sorry, the list is empty."                                    # options 4 & 5 empty list return
remove_all_items = "All the items have been removed from the list."           # option 5 populated list( remove all )

instance_count_singular = "There is {} instance of [{}] in the list."         # option 6 singular return
instance_count_plural = "There are {} instances of [{}] in the list."         # option 6 plural return

exit_statement = "Bye."  # exit option 9

# Create a list of menu options
menu_options = [
    item_prompt,
    remove_one_item_prompt,
    count_items_prompt,
    display_items_prompt,
    remove_all_items_prompt,
    instance_count_prompt,
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

    if selection == 1:
        item_new = input(enter_item_prompt).replace(' ', '_').strip()
        if item_new not in items:
            items.append(item_new)
            if len(items) == 1:
                print(list_addition_singular.format(item_new, len(items)))
            else:
                print(list_addition_plural.format(item_new, len(items)))
        else:
            confirmation_choice = input(append_confirmation_prompt.format(item_new)).strip().lower()
            if confirmation_choice == append_true:
                items.append(item_new)
                if len(items) == 1:
                    print(list_addition_singular.format(item_new, len(items)))
                else:
                    print(list_addition_plural.format(item_new, len(items)))
            else:
                print(list_addition_failure.format(item_new))
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
    elif all([selection == 6, items]):  # are there any items in our list object
        instance_query = input(enter_item_prompt).replace(' ', '_').strip()
        instance_count = items.count(instance_query)
        if instance_count == 1:
            print(instance_count_singular.format(instance_count, instance_query))
        elif any([instance_count > 1, instance_count == 0]):
            print(instance_count_plural.format(instance_count, instance_query))
    elif all([selection == 6, not items]):
        print(list_failure)
    elif selection == 9:
        print(exit_statement)
    else:
        continue
