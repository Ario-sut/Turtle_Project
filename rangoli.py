import turtle

t = turtle.Turtle()
t.color("Red")
t.width(3)
t.speed(5)
for i in range(80):
    for j in ["Green", "Blue", "Indigo", "Purple"]:
        t.forward(100)
        t.left(122)
        t.color(j)