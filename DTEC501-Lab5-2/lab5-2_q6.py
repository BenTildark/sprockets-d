"""
Write a program to draw the following.  Your code from Q5 will help here as it is a slight variation of that question.
You can choose the length of the lines.

"""

# Auth: Michael Devenport


import turtle

x = 0
y = 0

line = 100


def forty_five_deg_angles():
    pan = turtle.Turtle()
    for start_point in range(8):
        pan.setposition(x, y)
        pan.forward(line)
        pan.right(45)


forty_five_deg_angles()


def ui():
    popup = turtle.Screen()
    popup.exitonclick()


ui()


