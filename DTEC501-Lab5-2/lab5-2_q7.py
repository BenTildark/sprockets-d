"""
Write a program to draw the following.  This is made up of 10 squares.
The lines are 100 pixels in length but feel free to choose something different.

"""

# Auth: Michael Devenport.

import turtle

line_length = 100

line_color = 'Red'


def protractor_boxes():
    pan = turtle.Turtle()
    pan.color(line_color)
    for each_start_point in range(10):  # 1 Draw 10 boxes.
        pan.right(10)  # 2 Off-set each box by 10DEG right.
        for sides in range(4):  # 3 Draw each box.
            pan.forward(line_length)
            pan.right(90)


protractor_boxes()


def ui():
    popup = turtle.Screen()
    popup.exitonclick()


ui()

