import turtle
from turtle import Turtle,Screen
import random

timmy_turtle = Turtle()
timmy_turtle.speed(0)
timmy_turtle.pensize(2)
turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color= (r,g,b)
    return color


def draw_spiragoph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        timmy_turtle.pencolor(random_color())
        timmy_turtle.circle(100)
        timmy_turtle.setheading(timmy_turtle.heading() + size_of_gap)


draw_spiragoph(10)

screen = Screen()
screen.exitonclick()