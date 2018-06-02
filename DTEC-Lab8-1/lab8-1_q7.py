"""
Ask the user to enter their first name.
Ask the user to enter how many items they would like to enter into the list by displaying the message:
FirstName, please enter the number of items you would like to enter:
where FirstName is correctly capitalised.  There is a space immediately after the : on the input line.

Using a loop, ask the user to enter each item in turn by displaying the message:
Please enter item #x or STOP! if you want to finish early:
where x is the number of the current item.
If the user enters STOP! then stop asking for any more items and display the items as per below. The STOP! instruction is case sensitive.

User entered items other than the instruction to stop must have any extra spaces removed and be correctly capitalised.  See the examples  below.
If the user entered all the items then display the list as follows:

Item #1: <Item1>
Item #2: <Item2>
Item #3: <Item3>
etc

Hint.

Loop while there are more items to enter or the user has not said to stop.


Example
Please enter your first/given name: dave
Dave, please enter the number of items you would like to enter: 3
Please enter item #1 or STOP! if you want to finish early: oNe
Please enter item #2 or STOP! if you want to finish early:  two
Please enter item #3 or STOP! if you want to finish early: Three

Item 1: One
Item 2: Two
Item 3: Three

Example
Please enter your first/given name: dave
Dave, please enter the number of items you would like to enter: 10
Please enter item #1 or STOP! if you want to finish early: one
Please enter item #2 or STOP! if you want to finish early: tWo
Please enter item #3 or STOP! if you want to finish early: three
Please enter item #4 or STOP! if you want to finish early: Four
Please enter item #5 or STOP! if you want to finish early: stop!
Please enter item #6 or STOP! if you want to finish early: fIVe
Please enter item #7 or STOP! if you want to finish early: STOP!

Item 1: One
Item 2: Two
Item 3: Three
Item 4: Four
Item 5: Stop!
Item 6: Five


"""


# "Item {}: {}"

# Auth: Michael Devenport.
# croxleyway@gmail.com


name_prompt = "Please enter your first/given name: "
quantity_prompt = "{}, please enter the number of items you would like to enter: "
add_item_prompt = "Please enter item #{} or STOP! if you want to finish early: "
output_items = "Item {}: {}"

aggregate = []

first_name = input(name_prompt).strip().capitalize()

element_quantity = int(input(quantity_prompt.format(first_name)))

element_count = 0

still_to_add = True
while still_to_add:
    element_count += 1
    if element_count <= element_quantity:
        constituent = input(add_item_prompt.format(element_count))
        if not constituent == 'STOP!':
            aggregate.append(constituent.strip().capitalize())

        if any([element_count == element_quantity, constituent == 'STOP!']):
            still_to_add = False
        else:
            continue
    else:
        continue
print(" ")
items_count = 0
for item in aggregate:
    items_count += 1
    print(output_items.format(items_count, item))