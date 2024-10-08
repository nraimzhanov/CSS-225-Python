#Nurtilek Raimzhanov
#10/8/2024

#Problem 1. The program simply outputs the text "Hello World" to the screen

greeting = "Hello World!"
print(greeting)
#Problem 2.This program takes name from user and greets with inputed name
name = input("What is your name?")
print("Greetings", name)
#Problem 3.This program checks is my and my professor's name wrote in input and if it is it will say welcome if not it will not works
if name == "Nurtilek" or name == "Antonio":
    print("Welcome!", name)
else:
    print("Unfortunately, you can not enter!",name)
#Problem 4. This program takes a number from user and finding an area of circle
radius = int(input("Enter your radius:"))
areaOfCircle = 3.14 * radius ** 2
print("The area of circle is ", areaOfCircle)
#Problem 5. This rogram takes a two inputs both are numbers and it calculates the MPG of the car
milesDriven = int(input("How many miles you driven?"))
gallonsUsed = int(input("How many gallons your car consumed?"))
findingMpg = milesDriven/gallonsUsed
print("Your car's MPG is", findingMpg)
#Problem 6. This program takes an input from user to convert a Fahrenheit to Celsius
fahrenheit = int(input("Write a Fahrenheit that you want to convert to Celsius:"))
convertToCelsius = (fahrenheit - 32) * 5/9
print("The result is", convertToCelsius)
#Problem 7.The program takes a starting day number (0-6, where 0 is Sunday) and the length of stay in nights. It calculates the return day by adding the length of stay to the starting day and using modulo 7 to find the day of the week.
leavingDay = int(input("Write your leaving day(0 = Sunday, 6 = Saturday):"))
lengthOfStay = int(input("How many days you were traveling:"))
calculation = (leavingDay + lengthOfStay) % 7
print("You will return at the day number ",calculation)