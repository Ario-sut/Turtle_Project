import turtle

t = turtle.Turtle()
t.color("Red")
#t._color("White")
t.width(3)
t.speed(40)
n = 180
a = 0

for i in range(360*3):
    t.forward(a)
    t.left(1)
    if i % 180 ==0:
        a+=0.5