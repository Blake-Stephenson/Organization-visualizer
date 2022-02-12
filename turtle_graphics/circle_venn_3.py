import turtle
import Diagram as Diag

class Venn3():

    boxes = [[]]
    labels = []

    def __init__(self, D: Diag):
        self.boxes = D.getBoxes()
        self.labels = D.getGroups()

    def printD(self):
        t = turtle.Turtle()
        r = 100
        t.circle(r); t.color('blue');
        t.penup(); t.forward(100); t.pendown()
        t.circle(r)
        t.penup(); t.back(50); t.left(90); t.back(90); t.right(90); t.pendown()
        t.circle(r)