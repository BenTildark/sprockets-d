"""
Write a program to draw the following.

Start drawing at the -250,-200 by using the following statement:

set position(-250,-200)

Use variables to represent the x and y coordinate values.

The length of a side is 500 pixels.

"""
# Auth: Michael Devenport.

import turtle

x = -250
y = -200

paint = 'Red'


def paint_it_red():
    pan = turtle.Turtle()
    pan.penup()
    pan.setposition(x, y)
    pan.color(paint)
    pan.pendown()
    # Initialize fill outside of 'sides' loop
    pan.begin_fill()
    for sides in range(4):
        pan.forward(500)
        pan.left(90)
        pan.color(paint)
    # Kill fill not Bill ( Awesome movie that - have u seen it Dave? )
    pan.end_fill()


paint_it_red()


def ui():
    popup = turtle.Screen()
    popup.exitonclick()


ui()
