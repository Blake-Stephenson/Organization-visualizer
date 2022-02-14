import turtle
from diagram import DData as Diag


class Venn2:
    boxes = [[]]
    labels = []

    def __init__(self, d: Diag):
        self.boxes = d.getBoxes()
        self.labels = d.getLabels()
        self.data = d.getData()

    def printDiag(self):
        lens = [len(i) for i in self.boxes]
        x = max(lens)
        r = 50+5*x
        # close any old turtle
        turtle.bye()
        canvas = turtle.Screen()
        turtle.TurtleScreen._RUNNING = True
        t = turtle.Turtle(visible=False)
        t.speed(20)
        t.circle(r)
        t.color('blue')
        t.penup()
        t.forward(r)
        t.pendown()
        t.circle(r)
        t.penup()
        self.printTextLeft(r)
        self.printTextRight(r)
        self.printTextMid(r)
        self.printOther(r)
        canvas.exitonclick()

    def printTextLeft(self, r: int):
        nums = self.boxes[0][:]
        for i in self.boxes[1]:
            if i in nums:
                nums.remove(i)
        turtle.TurtleScreen._RUNNING = True
        t = turtle.Turtle(visible=False)
        t.setheading(270)
        t.penup()
        t.speed(10)
        # Print label
        t.goto(0,2 * r + 5)
        t.write(self.labels[0])
        # Print nums
        t.goto(-r / 3, r+(5 * len(nums)))
        for i in nums:
            t.write(i)
            t.fd(10)

    def printTextRight(self, r: int):
        nums = self.boxes[1][:]
        for i in self.boxes[0]:
            if i in nums:
                nums.remove(i)
        turtle.TurtleScreen._RUNNING = True
        t = turtle.Turtle(visible=False)
        t.right(90)
        t.penup()
        t.speed(10)
        # Print label
        t.goto(r, 2 * r + 5)
        t.write(self.labels[1])
        # Print nums
        t.goto(r*5/4, r + (5*len(nums)))
        for i in nums:
            t.write(i)
            t.fd(10)

    def printTextMid(self, r: int):
        nums = []
        for i in self.boxes[0]:
            for j in self.boxes[1]:
                if i == j:
                    nums.append(i)
        turtle.TurtleScreen._RUNNING = True
        t = turtle.Turtle(visible=False)
        t.right(90)
        t.penup()
        t.speed(10)
        # Print nums
        t.goto(r / 2, r + (5 * len(nums)))
        for i in nums:
            t.write(i)
            t.fd(10)

    def printOther(self, r: int):
        nums = self.data[:]
        print(nums)
        for i in self.boxes[0]:
            if i in nums:
                nums.remove(i)
        for i in self.boxes[1]:
            if i in nums:
                nums.remove(i)
        turtle.TurtleScreen._RUNNING = True
        t = turtle.Turtle(visible=False)
        t.right(90)
        t.penup()
        t.speed(10)
        # Print nums
        t.goto(0, -20)
        print(nums)
        t.write("Other: %s" % nums)
