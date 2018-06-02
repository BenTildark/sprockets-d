"""
Write a program to draw the following.

Notes.

How many lines are there in a hexagon?

What is the angle of turn at each point?

https://www.mathsisfun.com/geometry/exterior-angles-polygons.html

The line length in the image below is 100 (pixels).

"""

# Auth: Michael Devenport.

import turtle

line_length = 100
angle = 60
line_color = 'Red'


def hexagon():
    pan = turtle.Turtle()
    pan.color(line_color)
    for sides in range(6):
        pan.forward(line_length)
        pan.right(angle)


hexagon()


def ui():
    popup = turtle.Screen()
    popup.exitonclick()


ui()

