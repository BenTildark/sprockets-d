"""
Take the code you wrote for Lab9-2-2 and create a function called display_menu which generates the following
output:

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

As per previous requirements there is a blank line above "Please select from one of the following options.".
*Just for Moodle*, use print(" ") to generate a blank line.

The display_menu function displays the output shown above.

The display_menu function returns the default None.

Example output


display_menu()

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

"""


def display_menu():

    """display menu options / return None"""

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

    print(blank_line)
    print(selection_prompt)

    # Iterate our aggregate( menu_options )
    for option in menu_options:
        print(option)

    return False


# print(type(display_menu()))
