"""
Write a program to do the following.

Ask the user to specify the length (in pixels) of a side of a square. You can choose the appropriate wording to use.

Using Python's turtle graphics, draw a square of the size specified.

"""

# Auth: Michael Devenport.

import turtle

instance_error = "\nPlease only use integers"
primary_input_prompt = "\nWelcome to drawing geometric shapes in python with turtle." \
                       " To get started please enter a size between 10 - 100 pixels inclusively & click enter: "
secondary_input_prompt = "\nInvalid input, enter a size between 10 - 100 pixels inclusively & click enter: "

square_size_in_px = ''  # Require assignment var for input outside of validation loops. !important.

# Validation loop
try:
    square_size_in_px = int(input(primary_input_prompt))  # Primary input prompt with initial welcome, only runs once.
except ValueError:  # Catch class error( if <input> not 'int' ) run next line & continue
    print(instance_error)
while square_size_in_px not in range(10, 101):  # Check if <input> value is outside our range params,
    # run if while condition was True.
    try:
        square_size_in_px = int(input(secondary_input_prompt))  # Execute if any above validation returned True( which
        # would be an invalid input )
    except ValueError:  # Catch any Value error,
        if not isinstance(secondary_input_prompt, int):  # Checking for explicit class error instance
            print(instance_error)  # Only run if class error & loop back to while else
            # skip & loop back to while condition
        else:
            continue  # Loop back to while condition


def draw_square():
    crawl = turtle.Turtle()
    crawl.forward(square_size_in_px)
    crawl.right(90)
    crawl.forward(square_size_in_px)
    crawl.right(90)
    crawl.forward(square_size_in_px)
    crawl.right(90)
    crawl.forward(square_size_in_px)
    crawl.right(90)


draw_square()

popup = turtle.Screen()
popup.bgcolor("orange")
popup.exitonclick()

