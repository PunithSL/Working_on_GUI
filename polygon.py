from turtle import Turtle, Screen,Pen
import random
timmy_turtle = Turtle()
colours = ['aquamarine','beige','blue','brown','cadetBlue','chartreuse','chocolate','coral','gray','orange','red',
           'green','pink','khaki','lightBlue']\

timmy_turtle.speed(10)
timmy_turtle.pensize(10)
timmy_turtle.shape("turtle")
timmy_turtle.color("red")


for i in range(3,11):
    angle = 360/i
    timmy_turtle.pencolor(random.choice(colours))
    for j in range(i):
        timmy_turtle.forward(100)
        timmy_turtle.right(angle)

