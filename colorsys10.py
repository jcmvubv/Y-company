from turtle import *
import colorsys
pensize (2)
bgcolor("black")
tracer (10)
hue=0.0
for i in range(150):
    c=colorsys. hsv_to_rgb (hue,1,1)
    color (c)
    hue+=0.003
    goto (0,0)
    circle (150-1, 90)
    up()
    fd(30)
    down ()
    begin_fill()
    circle (150-1, 90)
    end_fill()
    lt(1)
done()
