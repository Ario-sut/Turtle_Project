import turtle

t = turtle.Turtle()
t.color("Red")
#t._color("White")
t.width(3)
t.speed(5)
n = 3
for i in range(1,101):
    t.forward(n+i)
    t.left(15)