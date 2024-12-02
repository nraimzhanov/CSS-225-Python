class Chapter2:
    def trainingDrills(self):
        print("\nChapter 2: Youth Tournament Training...")
        print("You are at a training camp and you're about to take a drill to test your soccer knowledge.")

        # Math Problem
        print("\nTo prepare for the tournament, you need to calculate the total time spent on drills.")
        print("You spent 45 minutes on dribbling, 40 minutes on passing, and 35 minutes on shooting.")
        print("What is the total time spent on drills in minutes?")

        while True:
            answer = input("Enter the total time in Hours: ")
            try:
                if int(answer) == 2:
                    print("\nCorrect! You spent 120 minutes on drills.")
                    return True  # Success, move to next chapter
                else:
                    print("\nThat’s not right. Try again!")
            except ValueError:
                print("\nPlease enter a valid number.")
