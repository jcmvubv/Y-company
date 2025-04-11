from turtle import *
import colorsys
bgcolor("black")
pensize(3)
speed(0)
sm=0.6
for i in range(55):
    vj=colorsys.hsv_to_rgb(sm,0.2,0.9)
    color(vj)
    left(90)
    forward(200)
    left(135)
    forward(200)
    right(45)
    forward(200)
    right(135)
    forward(200)
    left(90)
    circle(i)
done()