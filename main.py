import Chapter1  # Import Chapter1.py
import Chapter2  # Import Chapter2.py
import Chapter3  # Import Chapter3.py
import Chapter4  # Import Chapter4.py
import Chapter5  # Import Chapter5.py
import turtle  # For drawing the "Passed" message and star


def restart_game():
    print("Game Over. You failed! Restarting the game...")
    main()  # Restart the game if the player fails


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
    victory_turtle.write("Passed!", align="center", font=("Arial", 24, "bold"))

    turtle.done()  # Finish drawing


def main():
    print("Welcome to the Soccer Adventure Game!")

    # Chapter 1: Interact with locals
    if not Chapter1.interactWithLocals():
        restart_game()  # Restart the game if the player fails in Chapter 1

    # Chapter 2: Training drills
    if not Chapter2.trainingDrills():
        restart_game()  # Restart the game if the player fails in Chapter 2

    # Chapter 3: Overcoming obstacles
    if not Chapter3.overcomeObstacles():
        restart_game()  # Restart the game if the player fails in Chapter 3

    # Chapter 4: Competing in a match
    if not Chapter4.competeInMatch():
        restart_game()  # Restart the game if the player fails in Chapter 4

    # Chapter 5: Key decisions in the World Cup
    if not Chapter5.makeKeyDecisionsDuringMatch():
        restart_game()  # Restart the game if the player fails in Chapter 5

    # If all chapters are completed successfully, show the victory message and draw a star
    draw_victory()


if __name__ == "__main__":
    main()  # Start the game
