"""
Create a suitably named list and add the following items to it:
Apple
Banana
Plum

Display the list as follows:
Item 1: Apple
Item 2: Banana
Item 3: Plum

Ask the user to enter the item number where the fruit will be added by displaying a blank line followed by the message:

Please enter the item number where the fruit will be added:

If the item number is between first and the last number then ask the user to enter the name of a fruit by displaying the following message:

Please enter the name of a fruit:

Remove any leading or trailing spaces from the fruit name.

Capitalise the name of the fruit.

Add the value they entered before the item they specified then print a blank line followed by the items in the list as per the example below.

*Just for Moodle*, a "blank line" needs to be generated using print(" ")

Example
Item 1: Apple
Item 2: Banana
Item 3: Plum

Please enter the item number where the fruit will be added: 1
Please enter the name of a fruit: pear

Item 1: Pear
Item 2: Apple
Item 3: Banana
Item 4: Plum

Example
Item 1: Apple
Item 2: Banana
Item 3: Plum

Please enter the item number where the fruit will be added: 2
Please enter the name of a fruit: pear

Item 1: Apple
Item 2: Pear
Item 3: Banana
Item 4: Plum


"""

# Auth: Michael Devenport.
# croxleyway@gmail.com

# In the interest of keeping it DRY I've written this with a while loop, I realise it could be done with
# 2 for loops. ;-).

index_position_prompt = "Please enter the item number where the fruit will be added: "
enter_item_prompt = "Please enter the name of a fruit: "
output_str = "Item {}: {}"

fruit_basket = ['Apple', 'Banana', 'Plum']

nothing_added = True
while nothing_added:
    item_count = 0
    if len(fruit_basket) > 3:
        print(" ")

    for item in fruit_basket:
        item_count += 1
        print(output_str.format(item_count, item))

    if len(fruit_basket) <= 3:
        print(" ")
        index_position = int(input(index_position_prompt))
        new_item = input(enter_item_prompt).strip().capitalize()

        fruit_basket.insert(index_position-1, new_item)
    else:
        nothing_added = False

