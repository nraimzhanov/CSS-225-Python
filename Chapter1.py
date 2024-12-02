import random


class Chapter1:
    def __init__(self):
        self.player_name = ""

    def interactWithLocals(self):
        print("\nChapter 1: Interacting with Locals...")
        self.player_name = input("What is your name, young player? ")
        print(f"Hello {self.player_name}, welcome to the village!")

        # Randomly select a villager to interact with
        npc_names = ["Dexter", "Ryan", "Dawn", "Andie"]
        random.shuffle(npc_names)
        npc_name = npc_names[0]

        print(f"{npc_name}: Hello, I am {npc_name}. Would you like to talk to me, {self.player_name}?")

        # Multiple Choice Question
        print("\nWhat is the most important skill for a soccer player?")
        print("1. Dribbling")
        print("2. Passing")
        print("3. Shooting")
        print("4. Defending")

        while True:
            answer = input("Choose the correct option (1-4): ")
            if answer == "2":
                print(f"\n{npc_name}: Correct! Passing is key to maintaining possession.")
                return True  # Success, move to next chapter
            elif answer == "2":
                print(f"\n{npc_name}: Not quite. Dribbling is important, but not the most crucial.")
            elif answer == "3":
                print(f"\n{npc_name}: Shooting is important, but not the first thing you need to focus on.")
            elif answer == "4":
                print(f"\n{npc_name}: Defending is important, but not the most crucial for a young player.")
            else:
                print("\nInvalid input. Please choose a number between 1 and 4.")
