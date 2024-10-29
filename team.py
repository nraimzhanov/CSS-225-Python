#Nurtilek Raimzhanov
#10/29/2024
# This program prompts the user to guess a number between 1 and 10
# It provides feedback on whether the guess is too high or too low,
# and allows the user to continue playing or exit.

answer = 6 #The right answer
# Using While Loop to continue the game
while True:
    # Prompt the user for their guess
    guessingUser = int(input("Guess a number from 1-10: "))
    # Provide feedback based on the user's guess
    if guessingUser < answer:
        print("Guess a higher number!")
    elif guessingUser > answer:
        print("Guess a lower number!")
    elif guessingUser == answer:
        print("Congratulations! You've guessed the correct number!")
    else:
        print("Please,use only numbers")
    # Ask if the user wants to continue playing
    yesOrNo = input("Do you want to continue playing? (Yes or No): ")
    if yesOrNo.casefold( )== "no":
        print("Thanks for playing!")

