"""
Write a program to draw the following.

Notes.

Use your answer from q10 as the basis for this question.

4 pulses (or peaks) need to be drawn.

"""

# Auth: Michael Devenport


import turtle

x = -200
y = 200


def sq_wave():
    pan = turtle.Turtle()
    pan.penup()
    pan.setposition(x, y)
    pan.pendown()
    for square_wave in range(4):
        pan.forward(50)
        pan.left(90)
        pan.forward(50)
        pan.right(90)
        pan.forward(50)
        pan.right(90)
        pan.forward(50)
        pan.left(90)


sq_wave()


def ui():
    popup = turtle.Screen()
    popup.exitonclick()


ui()
