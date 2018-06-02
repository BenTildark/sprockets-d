"""
Write a program to draw the following.  Using setposition(0,0) will help.
"""

# Auth: Michael Devenport


import turtle

x = 0
y = 0

line = 100


def draw_x_y_planes():
    pan = turtle.Turtle()
    for start_point in range(4):
        pan.setposition(x, y)
        pan.forward(line)
        pan.right(90)


draw_x_y_planes()


def ui():
    popup = turtle.Screen()
    popup.exitonclick()


ui()
