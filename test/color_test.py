import turtle

def draw2circle(t: turtle, r: int, home: (int, int)):
    #move to start
    t.penup()
    t.goto(home)
    # draw circle one
    t.color("#EB3431", "#EB5670")
    t.pendown()
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    #move to next
    t.penup()
    t.forward(r)
    # draw circle two
    t.pendown()
    t.color("#253BEB", "#636EEB")
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    #move to middle
    t.penup()
    t.color("#C114F0", "#D254F0")
    t.goto(home)
    t.circle(r,30)
    t.pendown()
    t.begin_fill()
    t.circle(r, 120)
    t.setheading(210)
    t.circle(r, 120)
    t.end_fill()

def draw3circle(t: turtle, r: int, home: (int, int)):
    #move to start
    t.penup()
    t.goto(home)
    # draw circle one
    t.color("#EB3431", "#EB5670")
    t.pendown()
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    #move to next
    t.penup()
    t.forward(r)
    # draw circle two
    t.pendown()
    t.color("#253BEB", "#636EEB")
    t.begin_fill()
    t.circle(r)
    t.end_fill()

    #draw bottom circle
    t.penup()
    t.goto(home[0]+r/2,home[1]-r*0.866)
    t.color("#E0D910", "#FFFA16")
    t.pendown()
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    t.penup()

    t.circle(r, 90)
    t.setheading(90)
    t.color("#02FA00", "#4DFA58")
    t.pendown()
    t.begin_fill()
    t.circle(r, 120)
    t.setheading(270)
    t.circle(r, 120)
    t.end_fill()
    t.penup()

    t.goto(home[0] + r / 2, home[1] - r * 0.866)
    t.setheading(0)
    t.circle(r, 150)
    t.setheading(150)
    t.color("#FF8A00", "#FF9A2D")
    t.pendown()
    t.begin_fill()
    t.circle(r, 120)
    t.setheading(330)
    t.circle(r, 120)
    t.end_fill()

    #over lap two pieces
    t.penup()
    t.color("#C114F0", "#D254F0")
    t.goto(home)
    t.setheading(0)
    t.circle(r,30)
    t.pendown()
    t.begin_fill()
    t.circle(r, 120)
    t.setheading(210)
    t.circle(r, 120)
    t.end_fill()

    t.penup()
    t.color("#A6B3AB", "#C0CFC6")
    t.setheading(30)
    t.pendown()
    t.begin_fill()
    t.circle(r, 60)
    t.setheading(150)
    t.circle(r, 60)
    t.setheading(270)
    t.circle(r, 60)
    t.end_fill()

r =50
x = 100
y = 200

t = turtle.Turtle()
t.ht()
t.speed(20)
draw2circle(t,r,(x,y))

turtle.done()
