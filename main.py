import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create turtle object
pen = turtle.Turtle()
pen.color("red")
pen.pensize(3)
pen.speed(1)

# Draw heart shape
pen.begin_fill()
pen.left(140)
pen.forward(180)
pen.circle(-90, 200)
pen.left(120)
pen.circle(-90, 200)
pen.forward(180)
pen.end_fill()

# Hide the turtle and keep the window open
pen.hideturtle()
screen.mainloop()
