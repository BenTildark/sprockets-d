"""
Write a program to draw the following.

Notes.

Use your code for q's 13&14 as the basis for this.

The window must have a title as shown below.

The pointer must be hidden.


"""

# Auth: Michael Devenport.

import turtle

x_1 = -300
y_1 = 350

x_2 = -50
y_2 = -100

cross = 'White'
background = 'Red'
title = 'The Swiss flag'


def flag_background():
    pan = turtle.Turtle()
    pan.penup()
    pan.setposition(x_1, y_1)
    pan.pendown()
    pan.begin_fill()
    pan.color(background)
    for i in range(4):
        pan.forward(600)
        pan.right(90)
    pan.end_fill()
    pan.hideturtle()


flag_background()


def flag_cross():
    pan = turtle.Turtle()
    pan.penup()
    pan.setposition(x_2, y_2)
    pan.pendown()
    pan.begin_fill()
    pan.color(cross)
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
    pan.hideturtle()


flag_cross()


def ui():
    popup = turtle.Screen()
    popup.title(title)
    popup.exitonclick()


ui()
