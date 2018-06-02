# Auth: Michael Devenport
# Email: croxleyway@gmail.com


# This code is q2 version 1. Q 2 is the revised code.

valid_selection = range(1, 6)
exit_selection = 9

valid_selection_constituent = True  # this is not required.

blank_line = " "
selection_prompt = "Please select the number from one of the following options."
new_item_prompt = "1) Enter a new item."
remove_one_item_prompt = "2) Remove an item by its element number."
count_items_prompt = "3) Display the number of items in the list."
display_items_prompt = "4) Display a list of the items."
remove_all_items_prompt = "5) Remove all items from the list."
exit_prompt = "9) Exit."

option_prompt = "Option: "

# Create a list of menu options
menu_options = [new_item_prompt, remove_one_item_prompt, count_items_prompt,
                display_items_prompt, remove_all_items_prompt, exit_prompt]

while valid_selection_constituent:
    print(" ")
    print(selection_prompt)

    # Iterate our aggregate( menu_options )
    for constituent in menu_options:
        print(constituent)

    # Call to input function
    selection = int(input(option_prompt))

    # Assign options to var's
    enter_item = "Enter an item."
    remove_one_item = "Remove an item."
    count_items = "Display the number of items."
    display_list = "Display a list of items."
    remove_all_items = "Remove all items."
    exit_statement = "Bye."

    # Create options key value pair hash
    options = {1: enter_item, 2: remove_one_item, 3: count_items,
               4: display_list, 5: remove_all_items, 9: exit_statement}

    # Print selection if valid else loop back to menu options
    if selection in valid_selection:                # not required
        print(options[selection])                   # I'm required!! ;-)
    elif selection == exit_selection:               # not required
        print(options[selection])                   # not required
        valid_selection_constituent = False         # not required
    else:                                           # not required
        continue                                    # not required
