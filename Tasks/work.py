import turtle


shape = input("Введи форму черепашки (turtle, arrow, circle, square, triangle): ")
color = input("Введи колір черепашки (red, blue, green, yellow, purple, black): ")


t = turtle.Turtle()
t.shape()
t.color()


t.forward(100)

turtle.done()