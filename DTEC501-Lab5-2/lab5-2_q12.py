"""
Write a program to draw the following.

Notes.

Use your answer from q11 as the basis for this question.

"""

# Auth: Michael Devenport

import turtle

x = -200
y = 200


def sq_wave_polygon():
    pan = turtle.Turtle()
    pan.penup()
    pan.setposition(x, y)
    pan.pendown()
    # Loop through nested 'square_wave' ( * 4 ) Once for each side of our polygon shape.
    for each_side in range(4):
        # Loop through 'square_wave' dimensions ( * 4 ) to create each side majority ;-).
        for square_wave in range(4):
            pan.forward(50)
            pan.left(90)
            pan.forward(50)
            pan.right(90)
            pan.forward(50)
            pan.right(90)
            pan.forward(50)
            pan.left(90)
            # Following code indentation is important. They are not in the 'square_wave' loop
            # 'square_wave' & below 2 lines run in chronological order,
            # ie: run after each side completes( to hack end of a given side: tack on 50px line & rotate turtle right)
        pan.forward(50)
        pan.right(90)
        # With our hack run, side is completed & turtles facing the way we want the program loops back up to 'each_side'


sq_wave_polygon()


def ui():
    popup = turtle.Screen()
    popup.exitonclick()


ui()
