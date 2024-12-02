class Chapter3:
    def overcomeObstacles(self):
        print("\nChapter 3: Overcoming Obstacles in Training...")
        print("You've faced some tough obstacles, and now you need to show your knowledge of overcoming challenges.")

        # Multiple Choice Question
        print("\nCoach asks: What is the best way to overcome fatigue during a match?")
        print("1. Drink water and take a break")
        print("2. Push through and keep running")
        print("3. Focus on defense only")
        print("4. Wait for the game to end")

        while True:
            answer = input("Choose the correct option (1-4): ")
            if answer == "1":
                print("\nCoach: Correct! Hydration and rest are crucial to recovery.")
                return True  # Success, move to next chapter
            elif answer == "2":
                print("\nCoach: Pushing through is good, but it’s better to hydrate and take short breaks.")
            elif answer == "3":
                print("\nCoach: Focusing on defense isn’t enough. You need energy to play all aspects of the game.")
            elif answer == "4":
                print("\nCoach: Waiting for the game to end won't help you win. You need to take action.")
            else:
                print("\nInvalid input. Please choose a number between 1 and 4.")
