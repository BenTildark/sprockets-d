import turtle

def draw_square():
    for i in range(500):
        crawl = turtle.Turtle()
        crawl.forward(i)
        crawl.left(91)
        popup = turtle.Screen()
        popup.bgcolor("orange")

        popup.exitonclick()

        draw_square()

