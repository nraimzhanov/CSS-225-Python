# number = 0
# while number <= 10: #infinite loop
#     print("This is the number", number)
#     number = number + 1


#
# import turtle
#
# # Ask the user for inputs
# sides = int(input("Enter the number of sides: "))  # Number of sides
# length = int(input("Enter the length of each side: "))  # Length of each side
# line_color = input("Enter the line color: ")  # Line color
# fill_color = input("Enter the fill color: ")  # Fill color
#
# # Set the line and fill colors
# turtle.pencolor(line_color)
# turtle.fillcolor(fill_color)
#
# # Start filling the shape
# turtle.begin_fill()
#
# # Draw the polygon
# for i in range(sides):
#     turtle.forward(length)  # Move forward by 'length' units
#     turtle.left(360 / sides)  # Turn left by the angle for the polygon
#
# # End filling the shape
# turtle.end_fill()  # Fill the shape with the fill color
#
# turtle.done()  # Finish the drawing
#

import turtle
import random

# Function to draw a petal
def draw_petal():
    turtle.circle(100, 60)  # Draw the first curve of the petal
    turtle.left(120)         # Turn to draw the other side
    turtle.circle(100, 60)   # Draw the second curve of the petal
    turtle.left(120)         # Reposition for the next petal

# Function to draw the flower
def draw_flower():
    for _ in range(6):  # Draw 6 petals
        draw_petal()
        turtle.left(60)  # Position for the next petal

# Function to draw the stem
def draw_stem():
    turtle.right(90)    # Point downwards
    turtle.forward(300) # Draw the stem

# Set up the turtle
turtle.speed(3)          # Set the drawing speed
turtle.bgcolor("lightblue")  # Background color

# Draw the flower
turtle.color("magenta")  # Petal color
draw_flower()

# Draw the stem
turtle.color("green")     # Stem color
draw_stem()

# Draw leaves
turtle.penup()
turtle.goto(-50, -150)   # Position for the left leaf
turtle.pendown()
turtle.color("darkgreen")
turtle.begin_fill()
turtle.circle(50, 90)    # Draw left leaf
turtle.left(90)
turtle.circle(50, 90)
turtle.end_fill()

turtle.penup()
turtle.goto(50, -150)    # Position for the right leaf
turtle.pendown()
turtle.begin_fill()
turtle.circle(-50, 90)   # Draw right leaf
turtle.left(90)
turtle.circle(-50, 90)
turtle.end_fill()

# Finish up
turtle.hideturtle()       # Hide the turtle
turtle.done()             # Finish the drawing


