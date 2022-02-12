import turtle
import Diagram as Diag

class Venn3():

    boxes = [[]]
    labels = []

    def __init__(self, D: Diag):
        self.boxes = D.getBoxes()
        self.labels = D.getGroups()

    def printD(self):
        # close any old turtle
        turtle.bye()
        canvas = turtle.Screen()
        turtle.TurtleScreen._RUNNING = True
        t = turtle.Turtle()
        t.speed(20)
        r = 100
        t.circle(r); t.color('blue');
        t.penup(); t.forward(100); t.pendown()
        t.circle(r)
        t.penup(); t.back(50); t.left(90); t.back(90); t.right(90); t.pendown()
        t.circle(r)
        t.penup()
        t.goto(0, -20)
        t.write(self.labels)
        t.goto(0, -40)
        t.write(self.boxes)
        canvas.exitonclick()