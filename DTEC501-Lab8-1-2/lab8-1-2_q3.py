"""
Modify the code for Q3 to allow the user to enter a new item when they select option 1.

Remove the line of code which displays the

Enter an item.

message.

Modify the code at that point changing it to an input() to do the following:

Ask the user to enter the new item by displaying the message:

Please enter new item:

Once the user enters the item, display the message

[<Item>] has been added to the list. There is/are now <Total> item(s) in the list.
where <Item> is the item they just entered and <Total> is the total number of items now in the list.

The above must be grammatically correct e.g.

[Apple] has been added to the list. There is now 1 item in the list.
[Banana] has been added to the list. There are now 2 items in the list.

All other options must generate their output as per Q3.

Do not capitalise the item that is entered.

Hints.

Remember to remove all leading and trailing spaces from the entered item.
Displaying the "[Item] has been added to the list..." message is 1 conditional statement totaling 4 lines of code.

Add two items to the list and exit.

Please select the number from one of the following options.
1) Enter a new item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
9) Exit.
Option: 1
Please enter new item: Apple
[Apple] has been added to the list. There is now 1 item in the list.

Please select the number from one of the following options.
1) Enter a new item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
9) Exit.
Option: 1
Please enter new item: Banana
[Banana] has been added to the list. There are now 2 items in the list.

Please select the number from one of the following options.
1) Enter a new item.
2) Remove an item by its element number.
3) Display the number of items in the list.
4) Display a list of the items.
5) Remove all items from the list.
9) Exit.
Option: 9
Bye.
"""

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

    print(" ")
    print(selection_prompt)

    # Iterate our aggregate( menu_options )
    for constituent in menu_options:
        print(constituent)

    # Call to input function
    selection = int(input(option_prompt))

    # Assign options to var's
    enter_item = "Please enter new item: "          # option 1 input field prompt
    remove_one_item = "Remove an item."             # option 2
    count_items = "Display the number of items."    # option 3
    display_list = "Display a list of items."       # option 4
    remove_all_items = "Remove all items."          # option 5
    exit_statement = "Bye."                         # exit option 9

    if selection == 1:
        items.append(input(enter_item).strip())
    elif selection == 2:
        print(remove_one_item)
    elif selection == 3:
        print(count_items)
    elif selection == 4:
        print(display_list)
    elif selection == 5:
        print(remove_all_items)
    elif selection == 9:
        print(exit_statement)
    else:
        continue

    items_count = len(items)
    if all([items_count > 0, selection == 1]):
        if items_count == 1:
            print(singular_list_evaluation.format(items[-1], items_count))
        else:
            print(plural_list_evaluation.format(items[-1], items_count))
