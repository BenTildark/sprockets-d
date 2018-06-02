"""
Write a program to draw the following.

Notes.

How many lines are there in an octagon?

What is the angle of turn at each point?

https://www.mathsisfun.com/geometry/exterior-angles-polygons.html

The line length in the image below is 100 (pixels).

"""

# Auth: Michael Devenport.

import turtle

line_length = 100
angle = 45
line_color = 'Red'


def octagon():
    pan = turtle.Turtle()
    pan.color(line_color)
    for sides in range(8):
        pan.forward(line_length)
        pan.right(angle)


octagon()


def ui():
    popup = turtle.Screen()
    popup.exitonclick()


ui()

