"""
Create a suitably named list and add the following items to it:
Apple
Banana
Plum


Ask the user to enter the name of a fruit by displaying the following message:

Please enter the name of a fruit:

There is a space immediately after the : on the input line.

Remove any leading or trailing spaces from the fruit the user enters.

Capitalise the name of the fruit.

Add the value they entered between the elements containing Banana and Plum.



Example
Please enter the name of a fruit: peach
Item 1: Apple
Item 2: Banana
Item 3: Peach
Item 4: Plum


"""

# Auth: Michael Devenport.
# croxleyway@gmail.com

enter_item = "Please enter the name of a fruit: "
output_str = "Item {}: {}"

fruit_basket = ['Apple', 'Banana', 'Plum']

new_item = input(enter_item).strip().capitalize()

fruit_basket.insert(2, new_item)

item_count = 0
for item in fruit_basket:
    item_count += 1
    print(output_str.format(item_count, item))