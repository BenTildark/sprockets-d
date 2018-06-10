
def display_menu():

    """display menu options / return None"""

    blank_line = " "
    selection_prompt = "Please select the number from one of the following options."
    new_item_prompt = "1) Enter a new item."
    remove_one_item_prompt = "2) Remove an item by its element number."
    count_items_prompt = "3) Display the number of items in the list."
    display_items_prompt = "4) Display a list of the items."
    remove_all_items_prompt = "5) Remove all items from the list."
    exit_prompt = "9) Exit."

    # Create a list of menu options
    menu_options = [
        new_item_prompt,
        remove_one_item_prompt,
        count_items_prompt,
        display_items_prompt,
        remove_all_items_prompt,
        exit_prompt
    ]

    print(blank_line)
    print(selection_prompt)

    # Iterate our aggregate( menu_options )
    for option in menu_options:
        print(option)

    return None
