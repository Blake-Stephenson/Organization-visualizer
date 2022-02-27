import turtle
from diagram import DData as Diag


class Venn3:
    boxes = [[]]
    labels = []
    data = []

    def __init__(self, d: Diag):
        self.boxes = d.getBoxes()
        self.labels = d.getLabels()
        self.data = d.getData()

    def printDiag(self):
        lens = [len(i) for i in self.boxes]
        x = max(lens)
        r = 50 + 5 * x
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
        t.back(r / 2)
        t.left(90)
        t.back(0.87 * r)
        t.right(90)
        t.pendown()
        t.circle(r)
        t.penup()
        self.printA(r)
        self.printB(r)
        self.printC(r)
        self.printAB(r)
        self.printAC(r)
        self.printBC(r)
        self.printABC(r)

        self.printOther(r)
        canvas.exitonclick()

    def printA(self, r: int):
        nums = self.boxes[0][:]
        for i in self.boxes[1]:
            if i in nums:
                nums.remove(i)
        for i in self.boxes[2]:
            if i in nums:
                nums.remove(i)

        turtle.TurtleScreen._RUNNING = True
        t = turtle.Turtle(visible=False)
        t.setheading(270)
        t.penup()
        t.speed(10)
        # Print label
        t.goto(0, 2 * r + 5)
        t.write(self.labels[0])
        # Print nums
        t.goto(-r / 3, r * 1.2 + (5 * len(nums)))
        for i in nums:
            t.write(i)
            t.fd(10)

    def printB(self, r: int):
        nums = self.boxes[1][:]
        for i in self.boxes[0]:
            if i in nums:
                nums.remove(i)
        for i in self.boxes[2]:
            if i in nums:
                nums.remove(i)

        turtle.TurtleScreen._RUNNING = True
        t = turtle.Turtle(visible=False)
        t.setheading(270)
        t.penup()
        t.speed(10)
        # Print label
        t.goto(r, 2 * r + 5)
        t.write(self.labels[1])
        # Print nums
        t.goto(r * 4 / 3, r * 1.2 + (5 * len(nums)))
        for i in nums:
            t.write(i)
            t.fd(10)

    def printC(self, r: int):
        nums = self.boxes[2][:]
        for i in self.boxes[0]:
            if i in nums:
                nums.remove(i)
        for i in self.boxes[1]:
            if i in nums:
                nums.remove(i)

        turtle.TurtleScreen._RUNNING = True
        t = turtle.Turtle(visible=False)
        t.setheading(270)
        t.penup()
        t.speed(10)
        # Print label
        t.goto(r / 2, -r - 10)
        t.write(self.labels[2])
        # Print nums
        t.goto(r / 2, -r * 0.6 + (5 * len(nums)))
        for i in nums:
            t.write(i)
            t.fd(10)

    def printAB(self, r: int):
        nums = []
        for i in self.boxes[0]:
            for j in self.boxes[1]:
                if i == j:
                    nums.append(i)
        for i in self.boxes[2]:
            if i in nums:
                nums.remove(i)

        turtle.TurtleScreen._RUNNING = True
        t = turtle.Turtle(visible=False)
        t.setheading(270)
        t.penup()
        t.speed(10)
        # Print nums
        t.goto(r/2, r * 1.3 + (5 * len(nums)))
        for i in nums:
            t.write(i)
            t.fd(10)

    def printAC(self, r: int):
        nums = []
        for i in self.boxes[0]:
            for j in self.boxes[2]:
                if i == j:
                    nums.append(i)
        for i in self.boxes[1]:
            if i in nums:
                nums.remove(i)

        turtle.TurtleScreen._RUNNING = True
        t = turtle.Turtle(visible=False)
        t.setheading(270)
        t.penup()
        t.speed(10)
        # Print nums
        t.goto(-r / 5, r * 0.25 + (5 * len(nums)))
        for i in nums:
            t.write(i)
            t.fd(10)

    def printBC(self, r: int):
        nums = []
        for i in self.boxes[1]:
            for j in self.boxes[2]:
                if i == j:
                    nums.append(i)
        for i in self.boxes[0]:
            if i in nums:
                nums.remove(i)

        turtle.TurtleScreen._RUNNING = True
        t = turtle.Turtle(visible=False)
        t.setheading(270)
        t.penup()
        t.speed(10)
        # Print nums
        t.goto(r*1.05, r * 0.25 + (5 * len(nums)))
        for i in nums:
            t.write(i)
            t.fd(10)

    def printABC(self, r: int):
        nums = []
        for i in self.boxes[0]:
            for j in self.boxes[1]:
                for k in self.boxes[2]:
                    if i == j and i == k:
                        nums.append(i)

        turtle.TurtleScreen._RUNNING = True
        t = turtle.Turtle(visible=False)
        t.setheading(270)
        t.penup()
        t.speed(10)
        # Print nums
        t.goto(r / 2 - 5, r * 0.5 + (5 * len(nums)) )
        for i in nums:
            t.write(i)
            t.fd(10)

    def printOther(self, r: int):
        nums = self.data[:]
        for i in self.boxes[0]:
            if i in nums:
                nums.remove(i)
        for i in self.boxes[1]:
            if i in nums:
                nums.remove(i)
        for i in self.boxes[2]:
            if i in nums:
                nums.remove(i)
        turtle.TurtleScreen._RUNNING = True
        t = turtle.Turtle(visible=False)
        t.right(90)
        t.penup()
        t.speed(10)
        # Print nums
        t.goto(0, -r - 30)
        t.write("Other: %s" % nums)
