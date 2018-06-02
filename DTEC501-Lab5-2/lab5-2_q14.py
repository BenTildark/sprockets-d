"""
Write a program to draw the following.

Notes.

Start drawing at the -50,-100 by using the following statement:

setposition(-50,-100)

Use variables to represent the x and y coordinate values.

This is a sequence of lines, not squares that have been coloured in.

Use a loop to replicate the sequence of steps.

The length of a side is 100 pixels.

"""
# Auth: Michael Devenport.

import turtle

x = -50
y = -100

col = 'red'


def red_cross():
    pan = turtle.Turtle()
    pan.penup()
    pan.setposition(x, y)
    pan.pendown()
    pan.begin_fill()
    pan.color(col)
    for each_side in range(2):
        pan.forward(100)
        pan.left(90)
        pan.forward(100)
        pan.right(90)
        pan.forward(100)
        pan.left(90)
        pan.forward(100)
        pan.left(90)
        pan.forward(100)
        pan.right(90)
        pan.forward(100)
        pan.left(90)
    pan.end_fill()


red_cross()


def ui():
    popup = turtle.Screen()
    popup.exitonclick()


ui()


