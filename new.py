import turtle
from turtle import Turtle

# Create an instance of Turtle
alex = Turtle()

# Get user inputs
shapeLength = float(input("What length do you want? "))
userRange = int(input("How many lines do you want? "))
fillColor = input("What color fill do you want? ")
justColor = input("What color do you want? ")

# Set the fill color and pen color
alex.fillcolor(fillColor)
alex.color(justColor)

# Start filling
alex.begin_fill()

# Draw the lines
for i in range(userRange):
    alex.forward(shapeLength)
    alex.right(360 / userRange)  # Adjust the angle for a better shape

# End filling
alex.end_fill()

# Complete drawing
turtle.done()

for i in range(100):
    print("Hello world")
# -------------------------------------------
listOfNum = 12,10,32,3,66,17,42,99,20
for num in listOfNum:
    print(num)
    print("Squared numbers:", num ** 2)
# -------------------------------------------



