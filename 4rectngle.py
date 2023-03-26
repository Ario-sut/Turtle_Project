import turtle

t = turtle.Turtle()
t.color("green")
t._color("White")
t.width(3)

t.penup()
t.left(180)
t.forward(110)
t.pendown()
for i in range(4):
    for j in range(4):
        t.forward(100)
        t.left(90)
    t.penup()
    t.forward(110)
    t.pendown()