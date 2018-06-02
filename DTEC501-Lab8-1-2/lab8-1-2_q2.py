"""
Modify your code from Q1 to display the menu below and accept input from the user.

Please select the number from one of the following options.
1) Enter a new item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
9) Exit.
Option:

If the user enters a valid option then perform the appropriate task below and in the case of options 1 to 5, then display the menu again.

If the user enters 1, display
Enter an item.

If the user enters 2, display
Remove an item.

If the user enters 3, display
Display the number of items.

If the user enters 4, display
Display a list of items.

If the user enters 5, display
Remove all items.

If the user enters 9, display
Bye.
and then exit from the program.



As there is no error handling, assume the user will always enter an integer for the option.


If the user enters an invalid option which is something other than 1, 2, 3, 4, 5 or 9 then display the menu again.


"""

# Auth: Michael Devenport
# Email: croxleyway@gmail.com

valid_selection = range(1, 6)
exit_selection = 9
selection = ''


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

while any([not selection == exit_selection, selection in valid_selection]):

    print(" ")
    print(selection_prompt)

    # Iterate our aggregate( menu_options )
    for constituent in menu_options:
        print(constituent)

    # Call to input function
    selection = int(input(option_prompt))

    # Assign options to var's
    enter_item = "Enter an item."                   # option 1
    remove_one_item = "Remove an item."             # option 2
    count_items = "Display the number of items."    # option 3
    display_list = "Display a list of items."       # option 4
    remove_all_items = "Remove all items."          # option 5

    exit_statement = "Bye."                         # exit option 9

    # Create options key value pair dictionary( hash )
    options = {1: enter_item, 2: remove_one_item, 3: count_items,
               4: display_list, 5: remove_all_items, 9: exit_statement}

    print(options[selection])
