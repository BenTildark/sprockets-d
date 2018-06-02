"""
Using the code you wrote for Q2, modify it to set the title of the graphics window to

A <SelectedColour> square drawn for <EnteredFirstName>



The full specification is:

Write a program to do the following.

Ask the user to enter their first name. You can choose the appropriate wording to use.

Ask the user to enter the length (in pixels) of a side of a square.  You can choose the appropriate wording to use.

If the length the user specifies is greater than 50 (inclusively) and less than 350 (inclusively), then ask the user to enter the colour that should be used for drawing the square.  The colours that are available are Red, Yellow and Blue. You can choose the appropriate wording to use. Only ask the user to enter a colour if the length was valid.

If the colour they specified is either Red, Yellow or Blue then using Python's turtle graphics, draw a square of the size and colour specified and set the window title.

If the colour they entered was something other than Red, Yellow or Blue then loop back and ask the user to enter a colour to use.

If the length the user specifies was outside the range of 50 and 350 then display the message:

Sorry, the length of the side of the square needs to be between 50 and 350. Please re-run the program.

"""

# Auth: Michael Devenport.

import turtle

user_name = ''

user_name_prompt = "\nPlease enter your first name: "

name_error_prompt = "\nName invalid, please try again. First name can not be blank,"

len_input_prompt = "\nWelcome to drawing geometric shapes in python with turtle {}." \
                       " To get started please enter a size between 50 - 350 pixels inclusively & click enter: "
validation_error = "\nSorry, the length of the side of the square needs to be between 50 and 350." \
                         " Please re-run the program. "
color_input_prompt = "\nPlease enter a color the square shall be drawn in, you can choose only Red, Yellow or Blue." \
                     " Input is required & is case sensitive. Type color & click enter: "
screen_title = "A {} square drawn for {}"

try:
    user_name = input(user_name_prompt).capitalize()
except ValueError:
    print(name_error_prompt)

# Primary validation loop:

square_size_in_px = int(input(len_input_prompt.format(user_name)))
if square_size_in_px not in range(50, 351):  # Check if <input> value is outside our range params,
    # run if while condition was True.
    print(validation_error)
    exit()

valid_colors = ['Red', 'Yellow', 'Blue']

# Secondary Validation loop:

line_color = input(color_input_prompt)
while line_color not in valid_colors:
    line_color = input(color_input_prompt)


def draw_square():
    crawl = turtle.Turtle()
    crawl.color(line_color)
    for sides in range(1, 5):
        crawl.forward(square_size_in_px)
        crawl.right(90)


draw_square()


def init_ui():
    popup = turtle.Screen()
    popup.title(screen_title.format(line_color, user_name))
    popup.bgcolor("Grey")
    popup.exitonclick()


init_ui()



