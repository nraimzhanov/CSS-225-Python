
#Nurtilek Raimzhanov

#10/22/2024






#Problem 1 – Consider a program that prints “Hello World” to the screen 100 times.
# Use draw.io to draw the flow of execution.
# Then write the program. Submit both the flowchart and the code.
greetings = "Hello World!"
print((greetings + "\n") * 100)




#Problem 2 – Assume you have a list of numbers 12, 10, 32, 3, 66, 17, 42, 99, 20.

#Write a loop that prints each of the numbers on a new line.
numbers = (12, 10, 32, 3, 66, 17, 42, 99, 20)
for number in numbers:
    print(number)

#Write a loop that prints each number and its square on a new line.
for newNumber in numbers:
    print(newNumber ** 2)




#Problem 3 – Write a program that asks the user for the number of sides, the length of the side, the color of the line, and the fill color of a regular polygon.
# The program should draw the polygon and then fill it in.
import turtle

# Ask the user for inputs
sides = int(input("Enter the number of sides: "))  # Number of sides
length = int(input("Enter the length of each side: "))  # Length of each side
line_color = input("Enter the line color: ")  # Line color
fill_color = input("Enter the fill color: ")  # Fill color

# Set the line and fill colors
turtle.pencolor(line_color)
turtle.fillcolor(fill_color)

# Start filling the shape
turtle.begin_fill()

# Draw the polygon
for i in range(sides):
    turtle.forward(length)  # Move forward by 'length' units
    turtle.left(360 / sides)  # Turn left by the angle for the polygon

# End filling the shape
turtle.end_fill()  # Fill the shape with the fill color

turtle.done()  # Finish the drawing





#Problem 4 – Consider a program that iterates the integers from 1 to 50. For multiples of three print “Divisible by three” instead of the number and for the multiples of five print “Divisible by five”. For numbers which are multiples of both three and five print “Divisible by both”. Use draw.io to draw the flow of execution. Then write the program. Submit both the flowchart and the code.
for i in range(50):
    print("The number is: ", i)
    if i % 3 == 0 and i % 5 == 0:
        print( i, "Divisible by both")
    elif i % 3 == 0:
        print( i, "Divisible by three")
    elif i % 5 == 0:
        print(i, "Divisible by five")

#Problem 5 – Write a program to draw some kind of picture. Be creative and experiment with the turtle methods provided in Summary of Turtle Methods.
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

