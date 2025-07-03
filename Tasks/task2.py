import turtle

screen = turtle.Screen()
t = turtle.Turtle()

c = turtle.textinput("Колір", "Введи колір пера:")

t.pensize(4)
t.shape("turtle")
t.pencolor(c)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)

turtle.done()