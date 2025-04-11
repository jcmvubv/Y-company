import turtle
from vpython import *

screen = turtle.Screen()
screen.bgcolor('black')

canvas = canvas(width=800, height = 600)

#create the 3d cube
cube = box(pos = vector(0,0,0), size = vector(4,4,4), color = color.red)

#Animate the rotation of the cube
while True:
    rate(60)
    cube.rotate(angle = radians(1), axis = vector(0,1,0))

#exit on click
turtle.done()