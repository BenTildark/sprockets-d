# from ok_cancel import *
# from ok_cancel import protocolhandler
# from retrying import retry
# Auth: Michael Devenport
# Email: croxleyway@gmail.com

# Q: 13 1 q2

# Option assignments
enter_item = 1
remove_item_by_id = 2
num_of_items = 3
list_items = 4
remove_all_items = 5
exit_menu = 9

# aggregate assignment list object, required outside of loop for compiling.
items = []

selection = ''  # required to hop into loop
while selection:
    print("1 hop load_menu func")

    # Create a list of menu options
    menu_options = [
        "1) Enter a new item.",
        "2) Remove an item by its element number.",
        "3) Display the number of items in the list.",
        "4) Display a list of the items.",
        "5) Remove all items from the list.",
        "9) Exit."
    ]

    print(" ")
    print("Please select the number from one of the following options.")

    # Iterate our aggregate( menu_options )
    for option in menu_options:
        print(option)

    # Call to input function
    selection = input("Option: ")

    # check if selection value is numeric
    if selection.isnumeric():
        selection = int(selection)

    # option 1 evaluation
    if selection == enter_item:
        item_new = input("Please enter new item: ").replace(' ', '_').strip()
        items.append(item_new)
        if len(items) == 1:
            print("[{}] has been added to the list. There is now {} item in the list.".format(item_new, len(items)))
        else:
            print("[{}] has been added to the list. There are now {} items in the list.".format(item_new, len(items)))

    elif selection == remove_item_by_id:
        print("Remove an item.")

    elif selection == num_of_items:
        print("Display the number of items.")

    elif selection == list_items:
        print("Display a list of items.")

    elif selection == remove_all_items:
        print("Remove all items.")

    elif selection == exit_menu:
        # protocolhandler()
        print("error location")

    else:
        continue
        # print("Sorry that option does not exist, please try again.")




