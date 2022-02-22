import turtle
import math

myturtle = turtle.Turtle()
myturtle.hideturtle()
myturtle.speed(20)
myturtle.pendown()


def drawOval(w: int, l: int, x: int, y: int, right: bool):
    myturtle.penup()
    myturtle.goto(x, y)
    myturtle.pendown()

    # right
    if right:
        for i in range(2):
            # two arcs
            myturtle.circle(w, 60)
            myturtle.circle(l, 120)
    else:
        for i in range(2):
            # two arcs
            myturtle.circle(l, 120)
            myturtle.circle(w, 60)

width = 260
length = int(width / 4)

xoff =int(width * 0.35)
yoff = int(width * 0.12)

# draw x
myturtle.color("blue")
drawOval(width, length, xoff, 0, False)
myturtle.color("black")
drawOval(width, length, -xoff, 0, True)
# draw v
drawOval(width, length, 0, -yoff, False)
drawOval(width, length, 0, -yoff, True)

turtle.exitonclick()
