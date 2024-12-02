class Chapter5:
    def makeKeyDecisionsDuringMatch(self):
        print("\nChapter 5: The World Stage - FIFA World Cup...")
        print("The final match is about to begin. You’re in a crucial position on the field and must make a decision.")

        # Multiple Choice Question
        print("\nYou have the ball in front of the goal. What do you do?")
        print("1. Pass to a teammate who is in a better position")
        print("2. Shoot for the goal and take the risk")
        print("3. Wait for the goalkeeper to come closer and then shoot")
        print("4. Dribble around the defense")

        while True:
            answer = input("Choose the correct option (1-4): ")
            if answer == "1":
                print("\nGreat decision! The teammate scores a beautiful goal!")
                return True  # Success, game over
            elif answer == "2":
                print("\nYou shoot, but the goalkeeper saves it. It wasn’t the best choice.")
            elif answer == "3":
                print("\nYou waited too long, and the chance is lost. The goalkeeper caught up.")
            elif answer == "4":
                print("\nYou try to dribble but lose possession. The defense takes control.")
            else:
                print("\nInvalid input. Please choose a number between 1 and 4.")
