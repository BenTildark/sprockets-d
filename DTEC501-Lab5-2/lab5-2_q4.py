"""
Using nested loops, write a program to draw the following.  You choose the size.

It's actually 4 squares all started from the same point.
"""

import turtle

inner_sq = 100  # Side length of square.

# We need 4 overall squares which start from same location, hence 4 cycles. (see: # 1 )
# Each cycle pans right 90 degree then heads into the nested loop 'sides' loops 4 times drawing a square. (see: # 2 )
# After the inner loops (360DEG)4 cycle completes we have 1 square with our turtle back at the start origin. (see: # 3 )
# As the inner loop 'sides' ends with a right 90 degree turn our turtle is currently facing East.
# If we went forward East we would just repeat our already drawn path! Considering the over all box/square needs to be
# positioned center to UI & the turtle needs to finish UI/box center East, we need to turn 180DEG after a square is
# complete & repeat our square again ( * 4 ).
# Hence the outer loop 'each_start_point' is run each time a square is completed, (on sq completion turtle turns 90DEG)
# we need 180DEG, as we already have 90 of our required 180 we can just turn another 90DEG right = 180DEG.
# Now turtle is facing South & heads into our 'sides' loop, draws an adjacent square.
# The process runs until the outer loop completes ( 4 squares in this case )


def draw_four_squares():
    pan = turtle.Turtle()
    for each_start_point in range(4):  # 1
        pan.right(90)  # 2
        for sides in range(4):  # 3
            pan.forward(inner_sq)
            pan.right(90)


draw_four_squares()


def ui():
    popup = turtle.Screen()
    popup.exitonclick()


ui()



