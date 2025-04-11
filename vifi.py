import turtle

wn = turtle.Screen()
wn.title("Cookie Clicker by @TokyoEdtech")
wn.bgcolor("black")

wn.register_shape("__pycache__/ihvih/ihgi.gif")

cookie = turtle.Turtle()
cookie.shape("__pycache__/ihvih/ihgi.gif")
cookie.speed(0)

clicks = 0

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 400)
pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))

def clicked(x, y):
    global clicks
    clicks += 1
    pen.clear()
    pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))
    
cookie.onclick(clicked)

wn.mainloop()