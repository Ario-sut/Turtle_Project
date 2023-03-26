import turtle
import time

t = turtle.Turtle()
t.color("purple")
t._color("White")
t.width(3)


t.penup()
t.left(180)
t.forward(500)
t.right(180)
t.pendown()
for i in range(5):
    for j in range(6):
        t.forward(100)
        t.left(60)
    t.penup()
    t.forward(200)
    t.pendown()

time.sleep(5)