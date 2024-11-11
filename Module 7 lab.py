# Nurtilek Raimzhanov
# 11/5/2024
# Problem 1: AreaOfCircle
# Area = π * r^2, where r is the radius.
import math
# Function to calculate the area of a circle given a radius
def areaOfCircle(r):
    calculation = math.pi * math.pow(r,2) # Area formula: π * r^2
    print("The area of circle is: ", calculation)
# Main function where we ask for input and call areaOfCircle
def main():
    radius = float(input("Enter your radius: "))# User input for radius
    areaOfCircle(radius) # Pass the input radius to the function

if __name__ == "__main__":
    main()# Call main function

# Problem 2: CheckRange
# Description: This program defines a function that checks if a given number is in the range from 1 to 9.
# The function prints whether the number is in the range or not, and it is called from the main function
# based on user input.
def checkNumberInRange(number):
    """
    This function checks if a given number is in the range of 1 to 9 (inclusive).

    Parameters:
    number (int): The number to be checked.

    Prints:
    - A message indicating if the number is in the range or not.
    """
    # Check if the number is in the range from 1 to 9 (inclusive)
    if number in range(1, 10):
        print("Yes,", number, "is in range")  # Number is within the range
    else:
        print("No,", number, "is not in range")  # Number is outside the range


def main():
    """
    The main function that gets user input and calls the checkNumberInRange function to check if the number
    is in the specified range.
    """
    # Prompt the user to enter a number
    rangeNum = int(input("Enter a number: "))  # Convert user input to an integer
    # Call the function to check if the entered number is in the range
    checkNumberInRange(rangeNum)

if __name__ == "__main__":
    # Call the main function to start the program
    main()

# Problem 3: MulitplyList
# Description: This program defines a function that multiplies all the numbers in a given list.
# The function prints the result of the multiplication.

def multiplyList(numbers):
    """
    This function multiplies all the numbers in a given list.

    Parameters:
    numbers (list): A list of numbers to be multiplied.

    Prints:
    - The result of multiplying all the numbers in the list.
    """
    # Initialize the result as 1 since multiplying by 1 does not affect the result
    result = 1

    # Iterate through each number in the list and multiply it with the result
    for number in numbers:
        result *= number

    # Print the result after multiplying all numbers
    print("The result of multiplying all the numbers in the list is:", result)


def main():
    """
    The main function that defines a list of numbers and calls the multiplyList function
    to multiply all the numbers in the list.
    """
    # List of numbers to multiply
    numbers = [5, 2, 7, -1]

    # Call the function to multiply the numbers in the list
    multiplyList(numbers)


if __name__ == "__main__":
    # Call the main function to start the program
    main()

# Problem 4: Unique
# Description: This function takes a list of numbers and returns a new list with unique elements.
# The list is processed to remove duplicates, and only the first occurrence of each element is kept.

def getUniqueElements(numbers):
    """
    This function returns a new list containing only the unique elements from the given list of numbers.

    Parameters:
    numbers (list): A list of numbers with possible duplicates.

    Returns:
    list: A list with unique elements from the original list.
    """
    uniqueNumbers = []  # Initialize an empty list to store unique numbers

    # Iterate through the original list
    for number in numbers:
        # If the number is not already in the uniqueNumbers list, append it
        if number not in uniqueNumbers:
            uniqueNumbers.append(number)

    # Return the list containing only unique elements
    return uniqueNumbers


def main():
    """
    The main function that defines a list with duplicate elements and calls the getUniqueElements function
    to filter out duplicates and return a list of unique numbers.
    """
    # List of numbers with duplicates
    numbers = [1, 3, 3, 3, 6, 2, 3, 5]

    # Call the function to get the list of unique elements
    uniqueNumbers = getUniqueElements(numbers)

    # Print the result
    print("The unique elements in the list are:", uniqueNumbers)


if __name__ == "__main__":
    # Call the main function to start the program
    main()

# Problem 5: Squares
#Draw multiple squares inside each other, where each square is smaller
# than the previous one. Each square should be centered within the previous square.
import turtle

# Create a turtle object named 'myTurtle'
myTurtle = turtle.Turtle()

def drawSquares(myTurtle, sideLength, x, y, nSquares, distanceApart):
    """
    This function recursively draws squares inside each other, starting from the largest square.

    Parameters:
    myTurtle (Turtle): The turtle object used for drawing the squares.
    sideLength (int): The side length of the current square to be drawn.
    x (int): The x-coordinate for the starting position of the square.
    y (int): The y-coordinate for the starting position of the square.
    nSquares (int): The total number of squares to be drawn.
    distanceApart (int): The distance by which each square is smaller than the previous one.

    Recursively:
    - Draws a square at the given (x, y) position.
    - Shrinks the square size for the next recursive call by `distanceApart * 2`.
    - Moves the position slightly for the next square (by adjusting x and y).
    - Stops drawing when `nSquares` reaches 0.
    """

    if nSquares > 0:  # If there are squares to draw
        myTurtle.color("blue")  # Set the turtle's color to blue
        myTurtle.pu()  # Pick up the pen to move the turtle without drawing
        myTurtle.setx(x)  # Move the turtle to the x position
        myTurtle.sety(y)  # Move the turtle to the y position
        myTurtle.pd()  # Put the pen down to start drawing

        # Loop to draw the four sides of the square
        for i in range(4):
            myTurtle.forward(sideLength)  # Move forward by 'sideLength' units
            myTurtle.right(90)  # Turn right by 90 degrees to form the square

        # Recursively call drawSquares to draw the next square inside this one
        drawSquares(myTurtle, sideLength - distanceApart * 2, x + 10, y - 10, nSquares - 1, distanceApart)


# Call the function to start drawing squares: initial size 100, starting at (60, 60), 4 squares, 10 units apart
drawSquares(myTurtle, 100, 60, 60, 4, 10)

# Problem 6: ClassCar
class Car:
    def __init__(self, model, year, color, type, manufacturer):
        """
        Constructor to initialize the car attributes.

        Parameters:
        model (str): The model of the car.
        year (int): The manufacturing year of the car.
        color (str): The color of the car.
        type (str): The type of the car (e.g., sedan, sports, etc.).
        manufacturer (str): The manufacturer of the car.
        """
        self.model = model
        self.year = year
        self.color = color
        self.type = type
        self.manufacturer = manufacturer

    # Getter methods for existing attributes
    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color

    # Getter methods for new attributes
    def get_type(self):
        return self.type

    def get_manufacturer(self):
        return self.manufacturer

    # Method to return full specifications
    def fullspecs(self):
        """
        This method returns the full specifications of the car as a string.

        Returns:
        str: A string containing all the car specifications including model,
             year, color, type, and manufacturer.
        """
        return f'{self.model} {self.year} {self.color} {self.type} {self.manufacturer}'


# Creating instances of the Car class
car1 = Car("Sports", 2012, "Blue", "Coupe", "Toyota")
car2 = Car("Sedan", 2020, "Black", "Sedan", "Honda")

# Printing out individual attributes using getter methods
print(car1.get_color())  # Blue
print(car1.get_model())  # Sports
print(car2.get_color())  # Black

# Printing full specifications using the fullspecs method
print(car1.fullspecs())  # Sports 2012 Blue Coupe Toyota
print(car2.fullspecs())  # Sedan 2020 Black Sedan Honda


