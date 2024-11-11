import random


def interactWithLocals():
    # Ask the player for their name
    playerName = input("What is your name, young player? ")

    # Greet the player with their name
    print(f"Hello {playerName}, welcome to Chapter 1: Interacting with locals...")

    # Randomly select a villager to interact with
    npcNameChoice = ["Dexter", "Ryan", "Dawn", "Andie"]
    random.shuffle(npcNameChoice)
    npcName = npcNameChoice[0]

    print(f"{npcName}: Hello, I am {npcName}. Would you like to talk to me, {playerName}?")

    answer = input("Press 'y' to talk to the villager or 'n' to leave: ").lower()
    if answer == 'y':
        print(f"{npcName}: It's good to see you pursuing soccer here, {playerName}!")
        return True  # Success
    else:
        print(f"{npcName}: Alright, maybe next time, {playerName}!")
        return False  # Failure
