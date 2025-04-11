from turtle import *
pensize(20)
color("#9fa0a2")
right(45)
for x in range(2):
    circle(170,90)
    circle(85,90)
    up()
    goto (15,85)
    down()
    for x in range(2):
        
        circle (150,90)
        circle (25,90)
        up()
        goto (110,150)
        down()
        right(90)
    for x in range(2):
        circle (125,90)
        circle(21,90)
done()