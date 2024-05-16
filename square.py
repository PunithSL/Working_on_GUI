from turtle import Turtle,Screen

timmy_turtle = Turtle()
timmy_turtle.shape("turtle")
timmy_turtle.shapesize(1)
timmy_turtle.color("red")

# Draw a square so, we need to use forward and right attribute from the turtle module

# TODO :Brute force way
# timmy_turtle.forward(100)
# timmy_turtle.right(90)
# timmy_turtle.forward(100)
# timmy_turtle.right(90)
# timmy_turtle.forward(100)
# timmy_turtle.right(90)
# timmy_turtle.forward(100)
# timmy_turtle.right(90)

#TODO :loop way
for i in range(0,4):
    timmy_turtle.forward(100)
    timmy_turtle.right(90)


screen = Screen()
screen.exitonclick()