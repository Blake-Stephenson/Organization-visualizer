import turtle
import Diagram as Diag


class Venn2():
    boxes = [[]]
    labels = []

    def __init__(self, d: Diag):
        self.boxes = d.getBoxes()
        self.labels = d.getGroups()

    def printD(self):
        # close any old turtle
        turtle.bye()
        canvas = turtle.Screen()
        turtle.TurtleScreen._RUNNING = True
        t = turtle.Turtle()
        t.speed(20)
        r = 100
        t.circle(r)
        t.color('blue')
        t.penup();
        t.forward(100);
        t.pendown()
        t.circle(r)
        t.penup()
        t.goto(0, -20)
        t.write(self.labels)
        t.goto(0, -40)
        t.write(self.boxes)
        canvas.exitonclick()
