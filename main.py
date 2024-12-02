import Chapter1
import Chapter2
import Chapter3
import Chapter4
import Chapter5


def restart_game(chapter):
    print("\nGame Over. You failed! Restarting the game...")
    if chapter == 2:
        Chapter1.Chapter1().interactWithLocals()  # Go back to Chapter 1
    elif chapter == 3:
        Chapter2.Chapter2().trainingDrills()  # Go back to Chapter 2
    elif chapter == 4:
        Chapter3.Chapter3().overcomeObstacles()  # Go back to Chapter 3
    elif chapter == 5:
        Chapter4.Chapter4().competeInMatch()  # Go back to Chapter 4


def draw_victory():
    print("\nCongratulations! You've completed all the chapters and won the game!")


def main():
    print("Welcome to the Soccer Adventure Game!\n")

    # The game starts at Chapter 1
    chapter = 1

    # Start with Chapter 1 and proceed based on the player's answers
    while chapter <= 5:
        print(f"\n--- Starting Chapter {chapter} ---")
        if chapter == 1:
            if not Chapter1.Chapter1().interactWithLocals():
                restart_game(chapter)  # Restart if the player fails Chapter 1
            else:
                chapter += 1  # Proceed to next chapter
        elif chapter == 2:
            if not Chapter2.Chapter2().trainingDrills():
                restart_game(chapter)  # Restart if the player fails Chapter 2
            else:
                chapter += 1  # Proceed to next chapter
        elif chapter == 3:
            if not Chapter3.Chapter3().overcomeObstacles():
                restart_game(chapter)  # Restart if the player fails Chapter 3
            else:
                chapter += 1  # Proceed to next chapter
        elif chapter == 4:
            if not Chapter4.Chapter4().competeInMatch():
                restart_game(chapter)  # Restart if the player fails Chapter 4
            else:
                chapter += 1  # Proceed to next chapter
        elif chapter == 5:
            if not Chapter5.Chapter5().makeKeyDecisionsDuringMatch():
                restart_game(chapter)  # Restart if the player fails Chapter 5
            else:
                draw_victory()  # Show victory message
                break  # End the game
import turtle

def draw_victory():
    screen = turtle.Screen()
    screen.bgcolor("black")  # Set the background color

    # Create a turtle for drawing
    victory_turtle = turtle.Turtle()
    victory_turtle.color("yellow")
    victory_turtle.pensize(5)
    victory_turtle.speed(5)

    # Draw a star
    for _ in range(5):
        victory_turtle.forward(100)
        victory_turtle.right(144)

    # Draw the "Passed" text
    victory_turtle.penup()
    victory_turtle.goto(0, -150)
    victory_turtle.pendown()
    victory_turtle.color("white")
    victory_turtle.write("YOU PASSED THE GAME!!!", align="center", font=("Arial", 24, "bold"))

    turtle.done()  # Finish drawing

if __name__ == "__main__":
    main()  # Start the game
