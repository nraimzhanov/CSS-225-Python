# Nurtilek Raimzhanov
# 10/29/2024
# Problem 1: Generate and print 10 random integers between 25 and 35.

import random  # Import the random module to use its random number

# Loop to generate and print 10 random integers
for i in range(10):
    # Random integer between 25 and 35
    print(random.randrange(25, 36))

# Problem 2: Generate and print a random odd integer between 0 and 100.

import random  # Import the random module for random number

# Generate a random odd integer between 0 and 100
odd_integer = random.randrange(1, 100, 2)  # Start at 1, end at 100, step by 2 to ensure it's odd
print(odd_integer)  # Print the generated odd integer

# Problem 3: Randomly select a day from a list of weekdays.

import random  # Import the random module

# List of weekdays
listOfTheWeekDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Randomly select a day from the list
day = random.choice(listOfTheWeekDays)  #  call random.choice with the list
print(day)  # Print the selected day

# Problem 4:
import math


def approximate_pi(n_terms):
    """
    Calculate an approximation of π using the Gregory-Leibniz series.

    The Gregory-Leibniz series states that:
    π ≈ 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - ...)

    Parameters:
    n_terms (int): The number of terms to sum in the series for the approximation.

    Returns:
    float: The approximated value of π.
    """
    pi_approximation = 0  # Initialize the variable to store the approximation
    for i in range(n_terms):
        # Calculate the i-th term in the series and add/subtract it from the total
        pi_approximation += ((-1) ** i) / (2 * i + 1)

    pi_approximation *= 4  # Multiply the sum by 4 to obtain the approximation of π
    return pi_approximation


# Number of terms to use in the approximation
n_terms = 1000000  # Using one million terms for a more accurate approximation

# Calculate the approximation of π using the specified number of terms
pi_approx = approximate_pi(n_terms)

# Print the approximated value of π
print("Approximated π: ", pi_approx)

# Print the actual value of π from the math module for comparison
print("Actual π from math module: ", math.pi)

# Problem 5
import math

def radians_to_degrees(radians):
    """
    Convert radians to degrees.

    The conversion formula is:
    degrees = radians * (180 / π)

    Parameters:
    radians (float): The value in radians to convert.

    Returns:
    float: The equivalent value in degrees.
    """
    return radians * (180 / math.pi)
# Get user input
radians_input = float(input("Enter a value in radians: "))

# Calculate the conversion using the custom function
degrees_manual = radians_to_degrees(radians_input)

# Calculate the conversion using the math module
degrees_math = math.degrees(radians_input)

# Print both results
print(f"Converted value (manual calculation): {degrees_manual:.2f} degrees")
print(f"Converted value (math module): {degrees_math:.2f} degrees")

# Problem 6: This program calculates the factorial of a user-defined integer
# using both a manual method and the math.factorial() function for comparison.
import math

# Get user input
userNumber = int(input("Enter your number to find a factorial: "))

# Initialize variable to hold the factorial result
factorial_manual = 1

# Calculate the factorial using a for loop
for i in range(1, userNumber + 1):
    factorial_manual *= i  # Multiply the current value of factorial_manual by i

# Calculate the factorial using the math module
factorial_math = math.factorial(userNumber)

# Print both results
print("Manually calculated factorial of",userNumber, "is",factorial_manual)
print("Factorial calculated using math.factorial", "is",factorial_math)
