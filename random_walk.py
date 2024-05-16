import turtle
from turtle import Turtle, Screen
import random

timmy_turtle = Turtle()
turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color= (r,g,b)
    return color


timmy_turtle.speed(10)
timmy_turtle.pensize(10)

random_direction = [0,90,180,270]

timmy_turtle.setheading(random.choice(random_direction))

for i in range(200):
    timmy_turtle.pencolor(random_color())
    timmy_turtle.forward(30)
    timmy_turtle.setheading(random.choice(random_direction))

screen = Screen()
screen.exitonclick()

