import turtle

t = turtle.Turtle()
t.speed(2)


t.penup()


t.goto(0, 0)


t.pendown()


for _ in range(4):
    t.forward(100)
    t.right(90)


t.penup()
t.goto(150, 0) 

turtle.done()
