"""
Write a program to draw the following chequered squares image

Notes.

The code for determining if a value is odd or even will be of use here.

The window must have a title as shown below.

The pointer must be hidden.

"""

# Auth: Michael Devenport.

# This one I just could not figure out following you instructions so I've hacked up an approximation of output.

import turtle


title = 'Chequered squares'

x = 0
y = 0

col_1 = 'red'
col_2 = 'Yellow'


def chequered_square():
    pan = turtle.Turtle()
    pan.penup()
    pan.setposition(x, y)
    pan.pendown()
    pan.begin_fill()
    pan.left(45)
    for i in range(4):
        pan.color(col_2)
        pan.forward(200)
        pan.left(90)
    pan.end_fill()
    pan.begin_fill()
    for e in range(4):
        pan.color(col_1)
        pan.forward(100)
        pan.left(90)
    pan.end_fill()
    pan.setposition(0, 142)
    pan.begin_fill()
    for e in range(4):
        pan.color(col_1)
        pan.forward(100)
        pan.left(90)
    pan.end_fill()
    pan.hideturtle()


chequered_square()


def ui():
    popup = turtle.Screen()
    popup.title(title)
    popup.exitonclick()


ui()

