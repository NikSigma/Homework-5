import turtle

screen = turtle.Screen()
t = turtle.Turtle()

t.speed(1)
t.shape("turtle")

t.pensize(2)
t.color("red") 
t.forward(100)
t.right(90)

t.pensize(5)
t.shape("arrow")
t.color("purple") 
t.speed(2)
t.forward(100)
t.right(90)

t.pensize(7)
t.shape("circle")
t.color("blue") 
t.speed(3)
t.forward(100)
t.right(90)

t.pensize(10)
t.shape("triangle")
t.color("green") 
t.speed(4)
t.forward(100)
t.right(90)

turtle.done()