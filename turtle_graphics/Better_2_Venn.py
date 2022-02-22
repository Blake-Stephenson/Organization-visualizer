import turtle
t = turtle.Turtle()
h = 100
g = 70
b = 50
a = 0.5
r = 100
t.color("#20EEEA" , "#BBFAF9")
t.begin_fill()
t.circle(r); # t.color('blue');
t.end_fill()
k = turtle.Turtle()
k.penup(); k.forward(100); k.pendown()
k.color("#E53497" , "#FFEDF7")
k.begin_fill()
k.circle(r)

k.end_fill()
k.penup(); k.backward(50); k.left(90); k.forward(100); k.right(90); k.pendown()
k.shape("circle")
k.color("#A960DC" ,"#E3C2FA")
k.shapesize(9, 5, 1)
turtle.done()