"""
Create a suitably named list and add the following items to it.
Apple
Banana
Plum


Display the values in the list as per the example below.

Example

Item 1: Apple
Item 2: Banana
Item 3: Plum


"""

# Auth: Michael Devenport.
# croxleyway@gmail.com

output_str = "Item {}: {}"

fruit_basket = ['Apple', 'Banana', 'Plum']

item_count = 0
for item in fruit_basket:
    item_count += 1
    print(output_str.format(item_count, item))