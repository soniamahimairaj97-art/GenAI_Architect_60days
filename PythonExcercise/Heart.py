import turtle

# Set up the window
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Heart Drawing")

# Create turtle
pen = turtle.Turtle()
pen.color("red")
pen.pensize(3)
pen.speed(1)

# Move to starting position
pen.begin_fill()
pen.left(50)
pen.forward(133)
pen.circle(50, 200)
pen.right(140)
pen.circle(50, 200)
pen.forward(133)
pen.end_fill()

# Keep window open
turtle.done()

