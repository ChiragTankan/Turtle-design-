import turtle
a=turtle.Turtle()
a.speed(500)
a.shape("turtle")
for i in range (50000):
    a.forward(i)
    a.color("red")
    a.left(91)
    a.color("green")
    a.backward(i)
    a.color("gray")
    a.right(i)
    a.left(1)
    a.circle(i)
