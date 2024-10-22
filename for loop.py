#
# listOfArray = [0,1,2,3,4,5,6,7,8,9]
#
# for i in listOfArray:
#     print("This is a i:", i)
#
# for i in range(6):
#     print("This is a i:", i)

# weapons = ["sword", "stone", "shield"]
# weaponsTwo = ["sword", "stone", "hammer"]
#
# for weapon in weapons:
#     print("Your weapons are: ", weapon)
#     if weapon in weaponsTwo:
#         print("You already have that weapon!")
#     else:
#         print("Weapon: ", weapon, "has been added to your bag")

# import turtle
#
# alex = turtle.Turtle()  # Corrected initialization of the turtle
# for i in range(4):
#     alex.forward(150)
#     alex.left(90)
#
# turtle.done()  # Correct usage to finish the drawing
#
# for i in range(10,17, ):
#     print("i is now", i)

import turtle

# Function to draw a petal
def draw_petal():
    turtle.circle(50, 60)  # Draw one side of the petal
    turtle.left(120)        # Turn to draw the other side
    turtle.circle(50, 60)   # Draw the other side of the petal
    turtle.left(120)        # Reposition for the next petal

# Set up the turtle
turtle.speed(5)              # Set the drawing speed
turtle.color("red")          # Petal color

# Draw the flower
for i in range(6):  # Draw 6 petals
    draw_petal()
    turtle.left(60)  # Position for the next petal


# Finish up
turtle.hideturtle()  # Hide the turtle
turtle.done()        # Finish the drawing
