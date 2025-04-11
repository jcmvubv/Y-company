import turtle
from random import randint

# setup the turtle screen
screen = turtle.Screen()
screen.bgcolor('black')

#create a turtle instance
t = turtle.Turtle()
t.speed(0)

#define the colors
colors = ['red','orange','yellow','indigo','purple','green']

#draw the spiral
for i in range(360):
    #set the pen color randomly
    color = colors[randint(0, len(colors)-1)]
    t.pencolor(color)

    #move the turtle forward and turn it
    t.forward(i)
    t.left(59)

#hide the turtle
t.hideturtle()

#exit the turtle graphics
screen.exitonclick()