import turtle
t = turtle.Turtle()
r = 100
x = 100
a = 7
t.circle(r); t.color('blue');
t.penup(); t.forward(100); t.pendown()
t.circle(r)
t.penup(); t.right(90); t.back(100); t.right(90); t.pendown(); t.color('red')
t.circle(r)
t.penup(); t.forward(100); t.pendown(); t.color('green')
t.circle(r);
turtle.penup(); turtle.goto(x, r); turtle.pendown(); turtle.write(a)
turtle.done()
print("hello")