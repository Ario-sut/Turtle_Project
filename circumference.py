import turtle

t = turtle.Turtle()
t.color("Red")
t._color("White")
t.width(3)

a = 100
b = 100

for x in range(4):
    for i in range(360):
        t.right(1)
        t.forward(2)
    t.penup()
    t.left(a)
    a+=100
    t.forward(b)
    b+=100
    t.pendown()