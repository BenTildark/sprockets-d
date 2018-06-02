"""
The customer has requested the following modification to the program.

Instead of

9) Exit.

they would like it to be

E) Exit.

The customer would like the E to be case sensitive and so pressing e will not result in the menu being exited.

All the other menu options stay as they are.

Hints.

Depending on how you have written your code, this might result in 1 line of code being removed if you have converted
the strings to integers on a separate line.
If you have treated the input as strings for all the questions, then you only have to change the menu line.
You should only need to modify the values of the option variables at the top of your code, not to have to visit each
section of code in turn.
If you are doing the latter, it means you have either magic numbers or string literals where variables should be used.
Remember the use of variables is encouraged, especially for the assessments.

Pressing enter, then 9 (invalid option) then exiting with E.

Please select the number from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
6) Count the instances of an item in the list.
E) Exit.
Option:

Please select the number from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
6) Count the instances of an item in the list.
E) Exit.
Option: 9

Please select the number from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
6) Count the instances of an item in the list.
E) Exit.
Option: E
Bye.

Attempting to exit from the menu.

Please select the number from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
6) Count the instances of an item in the list.
E) Exit.
Option: e

Please select the number from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
6) Count the instances of an item in the list.
E) Exit.
Option: E
Bye.

"""

"""
Terminal Menu #12
=============
Written on: April 18 2018
Developed by: Michael Devenport
Email: croxleyway@gmail.com

Implement case sensitive exit program with 'E'

Note from developer::To Customer, Please don't hesitate to contact for further changes.
Kind regards.
;-)  
"""
# Main assignments
valid_selection = range(1, 6)
exit_selection = 'E'
selection = ""

# Menu prompt/input assignments
blank_line = " "
selection_prompt = "Please select the number from one of the following options."
item_prompt = "1) Enter an item."
remove_one_item_prompt = "2) Remove an item by its element number."
count_items_prompt = "3) Display the number of items in the list."
display_items_prompt = "4) Display a list of the items."
remove_all_items_prompt = "5) Remove all items from the list."
instance_count_prompt = "6) Count the instances of an item in the list."
exit_prompt = "9) Exit.".replace('9', 'E')

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

    # Call to input function( menu options )
    selection = input(option_prompt)
    # check if selection value is numeric
    if selection.isnumeric():
        selection = int(selection)  # if True covert selection str_to_int for options evaluations below.
    # option 1 evaluation
    if selection == 1:
        item_new = input(enter_item_prompt).replace(' ', '_').strip()  # work around for multiple word input/whitespace
        if item_new not in items:
            items.append(item_new)
            if len(items) == 1:  # singular/plural evaluation
                print(list_addition_singular.format(item_new, len(items)))
            else:
                print(list_addition_plural.format(item_new, len(items)))
        else:
            confirmation_choice = input(append_confirmation_prompt.format(item_new)).strip().lower()
            if confirmation_choice == append_true:  # = 'Y'
                items.append(item_new)
                if len(items) == 1:
                    print(list_addition_singular.format(item_new, len(items)))
                else:
                    print(list_addition_plural.format(item_new, len(items)))
            else:
                print(list_addition_failure.format(item_new))
    # option 2 evaluation
    elif all([selection == 2, len(items) > 0]):
        element_num = int(input(remove_one_item))
        if all([element_num <= len(items), element_num > 0]):
            items.pop(element_num-1)
            print(element_deletion_success.format(element_num))
        else:
            print(element_deletion_failure.format(element_num))
    elif all([selection == 2, len(items) == 0]):
        print(list_failure)
    # option 3 evaluation
    elif all([selection == 3, len(items) == 1]):
        print(count_item_singular.format(len(items)))
    elif all([selection == 3, not len(items) == 1]):
        print(count_item_plural.format(len(items)))
    # option 4 evaluation
    elif all([selection == 4, len(items) >= 1]):
        count = 0
        for item in items:
            count += 1
            print(display_list.format(count, item))
    elif all([selection == 4, len(items) == 0]):  # 'len(items) == 0' will evaluate to True if list empty
        print(list_failure)
    # option 5 evaluation
    elif all([selection == 5, len(items) > 0]):
        items.clear()
        print(remove_all_items)
    elif all([selection == 5, not items]):  # 'not items' will evaluate to True if list empty
        print(list_failure)
    # option 6 evaluation
    elif all([selection == 6, items]):  # are there any items in our list object
        instance_query = input(enter_item_prompt).replace(' ', '_').strip()
        instance_count = items.count(instance_query)
        if instance_count == 1:
            print(instance_count_singular.format(instance_count, instance_query))
        elif any([instance_count > 1, instance_count == 0]):
            print(instance_count_plural.format(instance_count, instance_query))
    elif all([selection == 6, not items]):
        print(list_failure)
    # exit evaluation
    elif selection == exit_selection:
        print(exit_statement)
    else:
        continue
