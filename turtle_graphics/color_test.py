import turtle

def draw2circle(t: turtle, r: int, home: (int, int)):
    #move to start
    t.penup()
    t.goto(home)
    # draw circle one
    t.color("#20EEEA", "#BBFAF9")
    t.pendown()
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    #move to next
    t.penup()
    t.forward(r)
    # draw circle two
    t.pendown()
    t.color("#E53497", "#FFEDF7")
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    #move to middle
    t.penup()
    t.color("#A960DC", "#E3C2FA")
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
    t.color("#20EEEA", "#BBFAF9")
    t.pendown()
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    #move to next
    t.penup()
    t.forward(r)
    # draw circle two
    t.pendown()
    t.color("#E53497", "#FFEDF7")
    t.begin_fill()
    t.circle(r)
    t.end_fill()

    #draw bottom circle
    t.penup()
    t.goto(home[0]+r/2,home[1]-r*0.866)
    t.color("#10B827", "#15C644")
    t.pendown()
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    t.penup()

    t.circle(r, 90)
    t.setheading(90)
    t.color("#80B827", "#75C644")
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
    t.color("#802827", "#75C604")
    t.pendown()
    t.begin_fill()
    t.circle(r, 120)
    t.setheading(330)
    t.circle(r, 120)
    t.end_fill()

    #over lap two pieces
    t.penup()
    t.color("#A960DC", "#E3C2FA")
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
    t.color("#2960DC", "#63C28A")
    t.setheading(30)
    t.pendown()
    t.begin_fill()
    t.circle(r, 60)
    t.setheading(150)
    t.circle(r, 60)
    t.setheading(270)
    t.circle(r, 60)
    t.end_fill()

r =100
x = 0
y = 0

t = turtle.Turtle()
t.speed(20)
draw3circle(t,r,(x,y))

turtle.done()
