# Nurtilek Raimzhanov
# 11/5/2024
# Problem 1: Write a function areaOfCircle(r) which returns the area of a circle of radius r.
# Make sure you use the math module in your solution.
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