import turtle
import Diagram as Diag

class Venn2():

    boxes = [[]]
    labels = []



    def __init__(self, D: Diag):
        self.boxes = D.getBoxes()
        self.labels = D.getGroups()

    def printD(self):
        t = turtle.Turtle()
        r = 100
        t.circle(r);
        t.color('blue')
        t.penup();
        t.forward(100);
        t.pendown()
        t.circle(r)