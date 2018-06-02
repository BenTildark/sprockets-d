"""
Ask the user to enter how many items they would like to enter into the list by displaying the message:

Please enter the number of items you would like to enter into the list:

There is a space immediately after the : on the input line.

Using a loop, ask the user to enter each item in turn by displaying the message:
Please enter item #x
where x is the number of the current item.

Remove any leading or trailing spaces from the entered data.

Correctly capitalise the entered data.

Once all the items have been entered, display the list as follows:
Item #1: <Item1>
Item #2: <Item2>
Item #3: <Item3>

Hint.
A for loop is suggested.

Example

Please enter the number of items you would like to enter into the list: 4
Please enter item #1 first item
Please enter item #2 Second item
Please enter item #3  third item
Please enter item #4  fourth item
Item 1: First item
Item 2: Second item
Item 3: Third item
Item 4: Fourth item


"""
# Auth: Michael Devenport.
# croxleyway@gmail.com

quantity_prompt = "Please enter the number of items you would like to enter into the list: "
add_item_prompt = "Please enter item #{} "
output_items = "Item {}: {}"

aggregate = []

element_quantity = int(input(quantity_prompt))

element_count = 0

still_to_add = True
while still_to_add:
    element_count += 1
    if element_count <= element_quantity:
        constituent = input(add_item_prompt.format(element_count)).strip().capitalize()
        aggregate.append(constituent)
        if element_count == element_quantity:
            still_to_add = False
        else:
            continue
    else:
        continue
items_count = 0
for item in aggregate:
    items_count += 1
    print(output_items.format(items_count, item))