import turtle

# Create a turtle object
my_turtle = turtle.Turtle()

# Set the turtle's speed to fast
my_turtle.speed(10)

# Set the turtle's pen color to red
my_turtle.pencolor("red")

# Move the turtle to the starting position
my_turtle.penup()
my_turtle.goto(-150, 0)
my_turtle.pendown()

# Write the word "Happy"
my_turtle.write("Happy", font=("Arial", 36, "bold"))

# Move the turtle to the next position
my_turtle.penup()
my_turtle.forward(200)

# Write the word "Birthday"
my_turtle.write("Birthday", font=("Arial", 36, "bold"))

# Hide the turtle when done
my_turtle.hideturtle()

# Keep the turtle window open
turtle.done()