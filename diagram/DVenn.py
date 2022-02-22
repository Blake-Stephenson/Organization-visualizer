import turtle
from diagram import DData as Diag


class DVenn:
    size = 0

    def __init__(self, d: Diag):
        self.size = len(d.getLabels())
        if self.size == 2:
            self.venn = Venn2(d)
        elif self.size == 3:
            self.venn = Venn3(d)
        elif self.size == 4:
            self.venn = Venn4(d)

    def show(self):
        self.venn.printDiag()


class Venn2:
    boxes = [[]]
    labels = []
    data = []

    def __init__(self, d: Diag):
        self.boxes = d.getBoxes()
        self.labels = d.getLabels()
        self.data = d.getData()
        self.t = d.getT()

    def printDiag(self):
        lens = [len(i) for i in self.boxes]
        x = max(lens)
        r = 40 + 3 * x
        hx = -r / 2
        hy = -r / 2

        t = self.t
        t.penup()
        t.goto(hx, hy)
        t.pendown()
        t.color('black')
        t.speed(20)
        t.circle(r)
        t.color('blue')
        t.penup()
        t.forward(r)
        t.pendown()
        t.circle(r)
        t.penup()
        self.printTextLeft(r, (hx, hy))
        self.printTextRight(r, (hx, hy))
        self.printTextMid(r, (hx, hy))
        self.printOther(r, (hx, hy))

    def printTextLeft(self, r: int, home: (int, int)):
        nums = self.boxes[0][:]
        for i in self.boxes[1]:
            if i in nums:
                nums.remove(i)
        turtle.TurtleScreen._RUNNING = True
        t = self.t
        t.setheading(270)
        t.penup()
        # Print label
        t.goto(home[0], home[1] + 2 * r + 5)
        t.write(self.labels[0])
        # Print nums
        t.goto(home[0] - r / 3, home[1] + r + (5 * len(nums)))
        for i in nums:
            t.write(i)
            t.fd(10)

    def printTextRight(self, r: int, home: (int, int)):
        nums = self.boxes[1][:]
        for i in self.boxes[0]:
            if i in nums:
                nums.remove(i)
        t = self.t
        t.setheading(270)
        t.penup()
        # Print label
        t.goto(home[0] + r, home[1] + 2 * r + 5)
        t.write(self.labels[1])
        # Print nums
        t.goto(home[0] + r * 5 / 4, home[1] + r + (5 * len(nums)))
        for i in nums:
            t.write(i)
            t.fd(10)

    def printTextMid(self, r: int, home: (int, int)):
        nums = []
        for i in self.boxes[0]:
            for j in self.boxes[1]:
                if i == j:
                    nums.append(i)
        t = self.t
        t.setheading(270)
        t.penup()
        # Print nums
        t.goto(home[0] + r / 2 - 5, home[1] + r + (5 * (len(nums)-1)))
        for i in nums:
            t.write(i)
            t.fd(10)

    def printOther(self, r: int, home: (int, int)):
        nums = self.data[:]
        for i in self.boxes[0]:
            if i in nums:
                nums.remove(i)
        for i in self.boxes[1]:
            if i in nums:
                nums.remove(i)
        t = self.t
        t.right(90)
        t.penup()
        t.speed(10)
        # Print nums
        t.goto(home[0], home[1] - 20)
        t.write("Other: %s" % nums)


class Venn3:
    boxes = [[]]
    labels = []
    data = []

    def __init__(self, d: Diag):
        self.boxes = d.getBoxes()
        self.labels = d.getLabels()
        self.data = d.getData()
        self.t = d.getT()

    def printDiag(self):
        lens = [len(i) for i in self.boxes]
        x = max(lens)
        r = 40 + 4 * x
        hx = -r / 2
        hy = -r / 2

        t = self.t
        t.penup()
        t.goto(hx, hy)
        t.pendown()
        t.color('black')
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
        self.printA(r, (hx, hy))
        self.printB(r, (hx, hy))
        self.printC(r, (hx, hy))
        self.printAB(r, (hx, hy))
        self.printAC(r, (hx, hy))
        self.printBC(r, (hx, hy))
        self.printABC(r, (hx, hy))
        self.printOther(r, (hx, hy))

    def printA(self, r: int, home: (int, int)):
        nums = self.boxes[0][:]
        for i in self.boxes[1]:
            if i in nums:
                nums.remove(i)
        for i in self.boxes[2]:
            if i in nums:
                nums.remove(i)

        t = self.t
        t.setheading(270)
        t.penup()
        # Print label
        t.goto(home[0], home[1] + 2 * r + 5)
        t.write(self.labels[0])
        # Print nums
        t.goto(home[0] - r / 3, home[1] + r * 1.2 + (5 * len(nums)))
        for i in nums:
            t.write(i)
            t.fd(10)

    def printB(self, r: int, home: (int, int)):
        nums = self.boxes[1][:]
        for i in self.boxes[0]:
            if i in nums:
                nums.remove(i)
        for i in self.boxes[2]:
            if i in nums:
                nums.remove(i)

        t = self.t
        t.setheading(270)
        t.penup()
        # Print label
        t.goto(home[0] + r, home[1] + 2 * r + 5)
        t.write(self.labels[1])
        # Print nums
        t.goto(home[0] + r * 4 / 3, home[1] + r * 1.2 + (5 * len(nums)))
        for i in nums:
            t.write(i)
            t.fd(10)

    def printC(self, r: int, home: (int, int)):
        nums = self.boxes[2][:]
        for i in self.boxes[0]:
            if i in nums:
                nums.remove(i)
        for i in self.boxes[1]:
            if i in nums:
                nums.remove(i)

        t = self.t
        t.setheading(270)
        t.penup()
        # Print label
        t.goto(home[0] + r / 2, home[1] - r - 10)
        t.write(self.labels[2])
        # Print nums
        t.goto(home[0] + r / 2, home[1] - r * 0.6 + (5 * len(nums)))
        for i in nums:
            t.write(i)
            t.fd(10)

    def printAB(self, r: int, home: (int, int)):
        nums = []
        for i in self.boxes[0]:
            for j in self.boxes[1]:
                if i == j:
                    nums.append(i)
        for i in self.boxes[2]:
            if i in nums:
                nums.remove(i)

        t = self.t
        t.setheading(270)
        t.penup()
        # Print nums
        t.goto(home[0] + r / 2, home[1] + r * 1.38 + (5 * len(nums)))
        for i in nums:
            t.write(i)
            t.fd(10)

    def printAC(self, r: int, home: (int, int)):
        nums = []
        for i in self.boxes[0]:
            for j in self.boxes[2]:
                if i == j:
                    nums.append(i)
        for i in self.boxes[1]:
            if i in nums:
                nums.remove(i)

        t = self.t
        t.setheading(270)
        t.penup()
        t.speed(10)
        # Print nums
        t.goto(home[0] - r / 5, home[1] + r * 0.25 + (5 * len(nums)))
        for i in nums:
            t.write(i)
            t.fd(10)

    def printBC(self, r: int, home: (int, int)):
        nums = []
        for i in self.boxes[1]:
            for j in self.boxes[2]:
                if i == j:
                    nums.append(i)
        for i in self.boxes[0]:
            if i in nums:
                nums.remove(i)

        t = self.t
        t.setheading(270)
        t.penup()
        # Print nums
        t.goto(home[0] + r * 1.05, home[1] + r * 0.25 + (5 * len(nums)))
        for i in nums:
            t.write(i)
            t.fd(10)

    def printABC(self, r: int, home: (int, int)):
        nums = []
        for i in self.boxes[0]:
            for j in self.boxes[1]:
                for k in self.boxes[2]:
                    if i == j and i == k:
                        nums.append(i)

        t = self.t
        t.setheading(270)
        t.penup()
        # Print nums
        t.goto(home[0] + r / 2 - 5, home[1] + r * 0.5 + (5 * len(nums)))
        for i in nums:
            t.write(i)
            t.fd(10)

    def printOther(self, r: int, home: (int, int)):
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
        t = self.t
        t.right(90)
        t.penup()
        # Print nums
        t.goto(home[0], home[1] - r - 30)
        t.write("Other: %s" % nums)

class Venn4:
    boxes = [[]]
    labels = []
    data = []

    def __init__(self, d: Diag):
        self.boxes = d.getBoxes()
        self.labels = d.getLabels()
        self.data = d.getData()
        self.t = d.getT()

    def printDiag(self):
        width = 300
        length = int(width / 4)

        #home coords
        hx = 0
        hy = -50

        t = self.t
        t.penup()
        t.speed(20)

        # draw diagram ovals
        xoff = int(width * 0.35)
        yoff = int(width * 0.12)
        # draw x
        t.color("black")
        self.drawOval(width, length, hx+xoff, hy, False)
        self.drawOval(width, length, hx+-xoff, hy, True)
        # draw v
        self.drawOval(width, length, hx, hy-yoff, False)
        self.drawOval(width, length, hx, hy-yoff, True)
        self.printA(width, (hx, hy))
        self.printB(width, (hx, hy))
        self.printC(width, (hx, hy))
        self.printD(width, (hx, hy))
        self.printAB(width, (hx, hy))
        self.printAC(width, (hx, hy))
        self.printAD(width, (hx, hy))
        self.printBC(width, (hx, hy))
        self.printBD(width, (hx, hy))
        self.printCD(width, (hx, hy))
        self.printABC(width, (hx, hy))
        self.printABD(width, (hx, hy))
        self.printACD(width, (hx, hy))
        self.printBCD(width, (hx, hy))
        self.printABCD(width, (hx, hy))
        self.printOther(width, (hx, hy))

    def printA(self, r: int, home: (int, int)):
        #left oval
        nums = self.boxes[0][:]
        for i in self.boxes[1]:
            if i in nums:
                nums.remove(i)
        for i in self.boxes[2]:
            if i in nums:
                nums.remove(i)
        for i in self.boxes[3]:
            if i in nums:
                nums.remove(i)

        t = self.t
        t.setheading(270)
        t.penup()
        # Print label
        t.goto(home[0] - r * 0.7, home[1] + r * 0.8)
        t.write(self.labels[0])
        # Print nums
        t.goto(home[0] - r * 0.7, home[1] + r * 0.45 + (5 * len(nums)))
        for i in nums:
            t.write(i)
            t.fd(10)

    def printB(self, r: int, home: (int, int)):
        # right oval
        nums = self.boxes[1][:]
        for i in self.boxes[0]:
            if i in nums:
                nums.remove(i)
        for i in self.boxes[2]:
            if i in nums:
                nums.remove(i)
        for i in self.boxes[3]:
            if i in nums:
                nums.remove(i)

        t = self.t
        t.setheading(270)
        t.penup()
        # Print label
        t.goto(home[0] + r * 0.7, home[1] + r * 0.8)
        t.write(self.labels[1])
        # Print nums
        t.goto(home[0] + r * 0.7, home[1] + r * 0.45 + (5 * len(nums)))
        for i in nums:
            t.write(i)
            t.fd(10)

    def printC(self, r: int, home: (int, int)):
        # mid left oval
        nums = self.boxes[2][:]
        for i in self.boxes[0]:
            if i in nums:
                nums.remove(i)
        for i in self.boxes[1]:
            if i in nums:
                nums.remove(i)
        for i in self.boxes[3]:
            if i in nums:
                nums.remove(i)

        t = self.t
        t.setheading(270)
        t.penup()
        # Print label
        t.goto(home[0] - r * 0.3, home[1] + r * 0.9)
        t.write(self.labels[2])
        # Print nums
        t.goto(home[0] - r * 0.3, home[1] + r * 0.75 + (5 * len(nums)))
        for i in nums:
            t.write(i)
            t.fd(10)

    def printD(self, r: int, home: (int, int)):
        # mid right oval
        nums = self.boxes[3][:]
        for i in self.boxes[0]:
            if i in nums:
                nums.remove(i)
        for i in self.boxes[1]:
            if i in nums:
                nums.remove(i)
        for i in self.boxes[2]:
            if i in nums:
                nums.remove(i)

        t = self.t
        t.setheading(270)
        t.penup()
        # Print label
        t.goto(home[0] + r * 0.3, home[1] + r * 0.9)
        t.write(self.labels[3])
        # Print nums
        t.goto(home[0] + r * 0.3, home[1] + r * 0.75 + (5 * len(nums)))
        for i in nums:
            t.write(i)
            t.fd(10)

    def printAB(self, r: int, home: (int, int)):
        nums = []
        for i in self.boxes[0]:
            for j in self.boxes[1]:
                if i == j:
                    nums.append(i)
        for i in self.boxes[2]:
            if i in nums:
                nums.remove(i)
        for i in self.boxes[3]:
            if i in nums:
                nums.remove(i)

        t = self.t
        t.setheading(270)
        t.penup()
        # Print nums
        t.goto(home[0] - 5, home[1] - r * 0.08 + (5 * len(nums)))
        for i in nums:
            t.write(i)
            t.fd(10)

    def printAC(self, r: int, home: (int, int)):
        nums = []
        for i in self.boxes[0]:
            for j in self.boxes[2]:
                if i == j:
                    nums.append(i)
        for i in self.boxes[1]:
            if i in nums:
                nums.remove(i)
        for i in self.boxes[3]:
            if i in nums:
                nums.remove(i)

        t = self.t
        t.setheading(270)
        t.penup()
        # Print nums
        t.goto(home[0] - r * 0.5, home[1] + r * 0.6 + (5 * len(nums)))
        for i in nums:
            t.write(i)
            t.fd(10)

    def printAD(self, r: int, home: (int, int)):
        nums = []
        for i in self.boxes[0]:
            for j in self.boxes[3]:
                if i == j:
                    nums.append(i)
        for i in self.boxes[1]:
            if i in nums:
                nums.remove(i)
        for i in self.boxes[2]:
            if i in nums:
                nums.remove(i)

        t = self.t
        t.setheading(270)
        t.penup()
        # Print nums
        t.goto(home[0] - r * 0.48, home[1] + r * 0.18 + (5 * len(nums)))
        for i in nums:
            t.write(i)
            t.fd(10)

    def printBC(self, r: int, home: (int, int)):

        nums = []
        for i in self.boxes[1]:
            for j in self.boxes[2]:
                if i == j:
                    nums.append(i)
        for i in self.boxes[0]:
            if i in nums:
                nums.remove(i)
        for i in self.boxes[3]:
            if i in nums:
                nums.remove(i)

        t = self.t
        t.setheading(270)
        t.penup()
        # Print nums
        t.goto(home[0] + r * 0.48, home[1] + r * 0.18 + (5 * len(nums)))
        for i in nums:
            t.write(i)
            t.fd(10)

    def printBD(self, r: int, home: (int, int)):
        nums = []
        for i in self.boxes[1]:
            for j in self.boxes[3]:
                if i == j:
                    nums.append(i)
        for i in self.boxes[2]:
            if i in nums:
                nums.remove(i)
        for i in self.boxes[0]:
            if i in nums:
                nums.remove(i)

        t = self.t
        t.setheading(270)
        t.penup()
        # Print nums
        t.goto(home[0] + r * 0.45, home[1] + r * 0.6 + (5 * len(nums)))
        for i in nums:
            t.write(i)
            t.fd(10)

    def printCD(self, r: int, home: (int, int)):
        nums = []
        for i in self.boxes[2]:
            for j in self.boxes[3]:
                if i == j:
                    nums.append(i)
        for i in self.boxes[0]:
            if i in nums:
                nums.remove(i)
        for i in self.boxes[1]:
            if i in nums:
                nums.remove(i)

        t = self.t
        t.setheading(270)
        t.penup()
        # Print nums
        t.goto(home[0] - 5, home[1] + r * 0.65 + (5 * len(nums)))
        for i in nums:
            t.write(i)
            t.fd(10)

    def printABC(self, r: int, home: (int, int)):
        nums = []
        for i in self.boxes[0]:
            for j in self.boxes[1]:
                for k in self.boxes[2]:
                    if i == j and i == k:
                        nums.append(i)
        for i in self.boxes[3]:
            if i in nums:
                nums.remove(i)

        t = self.t
        t.setheading(270)
        t.penup()
        # Print nums
        t.goto(home[0] + r * 0.17, home[1] + r * 0.05 + (5 * len(nums)))
        for i in nums:
            t.write(i)
            t.fd(10)

    def printABD(self, r: int, home: (int, int)):
        nums = []
        for i in self.boxes[0]:
            for j in self.boxes[1]:
                for k in self.boxes[3]:
                    if i == j and i == k:
                        nums.append(i)
        for i in self.boxes[2]:
            if i in nums:
                nums.remove(i)

        t = self.t
        t.setheading(270)
        t.penup()
        # Print nums
        t.goto(home[0] - r * 0.19, home[1] + r * 0.05 + (5 * len(nums)))
        for i in nums:
            t.write(i)
            t.fd(10)

    def printACD(self, r: int, home: (int, int)):
        nums = []
        for i in self.boxes[0]:
            for j in self.boxes[2]:
                for k in self.boxes[3]:
                    if i == j and i == k:
                        nums.append(i)
        for i in self.boxes[1]:
            if i in nums:
                nums.remove(i)

        t = self.t
        t.setheading(270)
        t.penup()
        # Print nums
        t.goto(home[0] - r * 0.3, home[1] + r * 0.45 + (5 * len(nums)))
        for i in nums:
            t.write(i)
            t.fd(10)

    def printBCD(self, r: int, home: (int, int)):
        nums = []
        for i in self.boxes[1]:
            for j in self.boxes[2]:
                for k in self.boxes[3]:
                    if i == j and i == k:
                        nums.append(i)
        for i in self.boxes[0]:
            if i in nums:
                nums.remove(i)

        t = self.t
        t.setheading(270)
        t.penup()
        # Print nums
        t.goto(home[0] + r * 0.3, home[1] + r * 0.45 + (5 * len(nums)))
        for i in nums:
            t.write(i)
            t.fd(10)

    def printABCD(self, r: int, home: (int, int)):
        nums = []
        for i in self.boxes[0]:
            for j in self.boxes[1]:
                for k in self.boxes[2]:
                    for p in self.boxes[3]:
                        if i == j and i == k and i == p:
                            nums.append(i)
        t = self.t
        t.setheading(270)
        t.penup()
        # Print nums
        t.goto(home[0] - 5, home[1] + r * 0.25 + (5 * len(nums)))
        for i in nums:
            t.write(i)
            t.fd(10)

    def printOther(self, r: int, home: (int, int)):
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
        for i in self.boxes[3]:
            if i in nums:
                nums.remove(i)

        t = self.t
        t.right(90)
        t.penup()
        # Print nums
        t.goto(home[0] - 40, home[1] - r * 0.2 - 10)
        t.write("Other: %s" % nums)

    def drawOval(self, w: int, l: int, x: int, y: int, right: bool):
        t = self.t
        t.penup()
        t.goto(x, y)
        t.pendown()

        # right
        if right:
            for i in range(2):
                # two arcs
                t.circle(w, 60)
                t.circle(l, 120)
        else:
            for i in range(2):
                # two arcs
                t.circle(l, 120)
                t.circle(w, 60)