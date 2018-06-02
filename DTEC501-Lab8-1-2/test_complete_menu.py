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

items = []  # aggregate assignment list object, required outside of loop for compiling.

while any([not selection == exit_selection, selection in valid_selection]):

    items_count = len(items)  # preliminary item count

    print(" ")
    print(selection_prompt)

    # Iterate our aggregate( menu_options )
    for constituent in menu_options:
        print(constituent)

    # Call to input function
    selection = int(input(option_prompt))

    # Assign options to var's
    enter_item = "Please enter new item: "              # option 1 input field prompt
    remove_one_item = "Item {} removed from list."      # option 2
    count_items = "{}."                                 # option 3
                                                        # option 4 Display a list of items
    remove_all_items = "All items removed."             # option 5
    exit_statement = "Bye."                             # exit option 9

    if selection == 1:
        items.append(input(enter_item).strip())         # append new item/input
    elif all([selection == 2, items_count >= 1]):
        print(remove_one_item.format(items.pop(int(input("Please enter element number: ")))))
    elif all([selection == 2, items_count == 0]):
        print("Sorry you can not remove items from an empty list.")
    elif selection == 3:
        print(count_items.format(len(items)))
    elif selection == 4:
        for i in items:
            print(i)
    elif selection == 5:
        items.clear()
        print(remove_all_items)
    elif selection == 9:
        print(exit_statement)
    else:
        continue

    items_count = len(items)  # secondary items count( required after call to addend to list[ above ])
    if items_count > 0:
        if items_count == 1:
            print(singular_list_evaluation.format(items[-1], items_count))
        else:
            print(plural_list_evaluation.format(items[-1], items_count))
