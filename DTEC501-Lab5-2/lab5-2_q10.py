"""
Write a program to draw the image below.

Suggestions.

Start drawing at the -200,200 by using the following statement:

set position(-200,200)

Use variables to represent the x and y coordinate values.

You need to consider how to move to the position specified above without drawing a line.

Consider the sequence of steps needed to draw the image, there is no repetition in this task.

The lines are 50 pixels long.

"""
# Auth: Michael Devenport

# from turtle import * # THIS DOES NOT WORK IN MY SYSTEM. !!!! if time Look into it' ;-)
import turtle

x = -200
y = 200

for i in range(1):
    pan = turtle.Turtle()
    pan.penup()
    pan.setposition(x, y)
    pan.pendown()
    pan.forward(50)
    pan.left(90)
    pan.forward(50)
    pan.right(90)
    pan.forward(50)
    pan.right(90)
    pan.forward(50)
    pan.left(90)


def ui():
    popup = turtle.Screen()
    popup.exitonclick()


ui()
