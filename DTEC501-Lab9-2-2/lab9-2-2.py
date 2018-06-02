"""
Modify the code you wrote for Lab8-1-2 and make changes to accommodate the menu entries for saving and loading data.

As the data is in a list, using Pickle is suggested but feel free to choose a different method.

The menu needs to look like:

Please select from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
6) Count the instances of an item in the list.
s) Save data.
l) Load data.
E) Exit.
Option:

Note the modified first line.

If the user selects option s  (case insensitive) and the file you save the data to exists,
the program must ask the user to confirm if the file is to be overwritten by displaying the message:

The file exists, overwrite? (Y/N):

If the user enters "Y" (case insensitive) then overwrite the file with the current content of the list and then
display the message:

Data has been saved.

If the user did not enter  "Y" (case insensitive) then display the message:
Data was not saved.

If the user selects option s (case insensitive) and the file you save the data to does not exist then display
the message:

Data has been saved.

If the user selects option l  (case insensitive) and there is one or more items in the list then ask the user
to confirm that the current items in the list are to be overwritten by displaying the message:

Data already exists in the list, overwrite? (Y/N):

If the user enters "Y" (case insensitive) then read the data from the disk and overwrite the list and then display
the message:

Data has been loaded.

If the user did not enter "Y" (case insensitive)  then display the message:

Data was not loaded.

Hints.

Using Pickle is suggested.
Saving the data is about 11 lines of code.
Loading the data is about 11 lines of code.
There is a degree of similarity between the two sections.
The data file is in the same directory as the program file.
Do not specify any directories in your code as the vm (JobEngine) that executes your code will not understand
those directories.

::::::::::::::::::EXAMPLES::::::::::::::::

Data in the list is overwritten by a confirmed request to load data from the file.

Please select from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
6) Count the instances of an item in the list.
s) Save data.
l) Load data.
E) Exit.
Option: 1
Please enter the item: One
[One] has been added to the list. There is now 1 item in the list.

Please select from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
6) Count the instances of an item in the list.
s) Save data.
l) Load data.
E) Exit.
Option: 1
Please enter the item: Two
[Two] has been added to the list. There are now 2 items in the list.

Please select from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
6) Count the instances of an item in the list.
s) Save data.
l) Load data.
E) Exit.
Option: S
Data has been saved.

Please select from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
6) Count the instances of an item in the list.
s) Save data.
l) Load data.
E) Exit.
Option: 4
Item 1: One
Item 2: Two

Please select from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
6) Count the instances of an item in the list.
s) Save data.
l) Load data.
E) Exit.
Option: 5
All the items have been removed from the list.

Please select from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
6) Count the instances of an item in the list.
s) Save data.
l) Load data.
E) Exit.
Option: 1
Please enter the item: Three
[Three] has been added to the list. There is now 1 item in the list.

Please select from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
6) Count the instances of an item in the list.
s) Save data.
l) Load data.
E) Exit.
Option: 1
Please enter the item: Four
[Four] has been added to the list. There are now 2 items in the list.

Please select from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
6) Count the instances of an item in the list.
s) Save data.
l) Load data.
E) Exit.
Option: 4
Item 1: Three
Item 2: Four

Please select from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
6) Count the instances of an item in the list.
s) Save data.
l) Load data.
E) Exit.
Option: L
Data already exists in the list, overwrite? (Y/N): y
Data has been loaded.

Please select from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
6) Count the instances of an item in the list.
s) Save data.
l) Load data.
E) Exit.
Option: 4
Item 1: One
Item 2: Two

Please select from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
6) Count the instances of an item in the list.
s) Save data.
l) Load data.
E) Exit.
Option: E
Bye.

Data in the list is being not overwritten by a request to load data from the file.

Please select from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
6) Count the instances of an item in the list.
s) Save data.
l) Load data.
E) Exit.
Option: 1
Please enter the item: One
[One] has been added to the list. There is now 1 item in the list.

Please select from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
6) Count the instances of an item in the list.
s) Save data.
l) Load data.
E) Exit.
Option: 1
Please enter the item: Two
[Two] has been added to the list. There are now 2 items in the list.

Please select from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
6) Count the instances of an item in the list.
s) Save data.
l) Load data.
E) Exit.
Option: S
Data has been saved.

Please select from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
6) Count the instances of an item in the list.
s) Save data.
l) Load data.
E) Exit.
Option: L
Data already exists in the list, overwrite? (Y/N): n
Data was not loaded.

Please select from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
6) Count the instances of an item in the list.
s) Save data.
l) Load data.
E) Exit.
Option: E
Bye.

Enter data, save to file, empty the list, load data from the file.

Please select from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
6) Count the instances of an item in the list.
s) Save data.
l) Load data.
E) Exit.
Option: 1
Please enter the item: One
[One] has been added to the list. There is now 1 item in the list.

Please select from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
6) Count the instances of an item in the list.
s) Save data.
l) Load data.
E) Exit.
Option: 1
Please enter the item: Two
[Two] has been added to the list. There are now 2 items in the list.

Please select from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
6) Count the instances of an item in the list.
s) Save data.
l) Load data.
E) Exit.
Option: 1
Please enter the item: One
[One] is already in the list, please confirm that want to add another [Y/N]: y
[One] has been added to the list. There are now 3 items in the list.

Please select from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
6) Count the instances of an item in the list.
s) Save data.
l) Load data.
E) Exit.
Option: 4
Item 1: One
Item 2: Two
Item 3: One

Please select from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
6) Count the instances of an item in the list.
s) Save data.
l) Load data.
E) Exit.
Option: s
Data has been saved.

Please select from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
6) Count the instances of an item in the list.
s) Save data.
l) Load data.
E) Exit.
Option: 4
Item 1: One
Item 2: Two
Item 3: One

Please select from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
6) Count the instances of an item in the list.
s) Save data.
l) Load data.
E) Exit.
Option: 5
All the items have been removed from the list.

Please select from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
6) Count the instances of an item in the list.
s) Save data.
l) Load data.
E) Exit.
Option: 4
Sorry, the list is empty.

Please select from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
6) Count the instances of an item in the list.
s) Save data.
l) Load data.
E) Exit.
Option: l
Data has been loaded.

Please select from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
6) Count the instances of an item in the list.
s) Save data.
l) Load data.
E) Exit.
Option: 3
There are 3 items in the list.

Please select from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
6) Count the instances of an item in the list.
s) Save data.
l) Load data.
E) Exit.
Option: 4
Item 1: One
Item 2: Two
Item 3: One

Please select from one of the following options.
1) Enter an item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
6) Count the instances of an item in the list.
s) Save data.
l) Load data.
E) Exit.
Option: E
Bye.
"""
"""
Terminal Menu #9-2-2
=============
Written on: May 20-21 2018
Developed by: Michael Devenport
Email: croxleyway@gmail.com

Implement save / load data

"""
import os
import re

# Main assignments
valid_selection = range(1, 7)
exit_selection = 'E'
selection = ""
data_file = "data.txt"

# Menu prompt/input assignments
blank_line = " "
selection_prompt = "Please select from one of the following options."
item_prompt = "1) Enter an item."
remove_one_item_prompt = "2) Remove an item by its element number."
count_items_prompt = "3) Display the number of items in the list."
display_items_prompt = "4) Display a list of the items."
remove_all_items_prompt = "5) Remove all items from the list."
instance_count_prompt = "6) Count the instances of an item in the list."
save_data_prompt = "s) Save data."
load_data_prompt = "l) Load data."
exit_prompt = "9) Exit.".replace('9', 'E')

option_prompt = "Option: "

# Option input/function & return statement assignments
enter_item_prompt = "Please enter the item: "                                 # option 1 input field prompt
append_confirmation_prompt = "[{}] is already in the list," \
                             " please confirm that you" \
                             " want to add another [Y/N]: "                   # option 1 confirmation prompt
append_true = 'y'                                                             # option 1 confirm & proceed

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

overwrite_confirmation_prompt = "The file exists, overwrite? (Y/N): "         # option 7 prompt for overwrite file
write_confirmation = "Data has been saved."                                   # write confirm for overwrite
write_opt_out = "Data was not saved."                                         # write opt out

items_deletion_confirmation_prompt = "Data already exists in the list, overwrite? (Y/N): "
load_confirmation = "Data has been loaded."
load_opt_out = "Data was not loaded."

exit_statement = "Bye."  # exit option 9

# Create a list of menu options
menu_options = [
    item_prompt,
    remove_one_item_prompt,
    count_items_prompt,
    display_items_prompt,
    remove_all_items_prompt,
    instance_count_prompt,
    save_data_prompt,
    load_data_prompt,
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
        # print(str(items)) debugging save/load options 7/8
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
    # option 7( 's' save data ) evaluation
    elif any([selection == 's', selection == 'S']):
        if items:
            cdl = os.listdir(os.getcwd())
            if re.search(data_file, str(cdl)):
                overwrite_confirm = input(overwrite_confirmation_prompt)
                if any([overwrite_confirm == 'y', overwrite_confirm == 'Y']):
                    df = open(data_file, "w")
                    for item in items:
                        df.write(item + '\n')
                    df.close()
                    print(write_confirmation)
                else:
                    print(write_opt_out)
            else:
                df = open(data_file, "w")
                for item in items:
                    df.write(item + '\n')
                df.close()
                print(write_confirmation)
        else:
            continue
    # option 8 ( load saved data into list[items] ) evaluation
    elif any([selection == 'l', selection == 'L']):
        cdl = os.listdir(os.getcwd())
        if re.search(data_file, str(cdl)):
            if items:
                items_deletion_confirm = input(items_deletion_confirmation_prompt)
                if any([items_deletion_confirm == "y", items_deletion_confirm == "Y"]):
                    items.clear()
                    df = open(data_file, "r")
                    for entry in df:
                        items.append(entry.replace('\n', ''))
                    df.close()
                    print(load_confirmation)
                else:
                    print(load_opt_out)
            else:
                items.clear()
                df = open(data_file, "r")
                for entry in df:
                    items.append(entry.replace('\n', ''))
                df.close()
                print(load_confirmation)
        else:
            continue
    # exit evaluation
    elif selection == exit_selection:
        print(exit_statement)
    else:
        continue
