class Chapter4:
    def competeInMatch(self):
        print("\nChapter 4: National U-17 Match...")
        print("You’re about to play in a big match, but first, you need to solve a math problem to ensure you’re focused.")

        # Math Problem
        print("\nThe coach needs your help with some math to calculate the total distance run in the first half of the match.")
        print("You ran 2.5 kilometers in the first 10 minutes, 1.8 kilometers in the next 15 minutes, and 3.2 kilometers in the last 20 minutes.")
        print("What is the total distance run in the first half of the match (in kilometers)?")

        while True:
            answer = input("Enter the total distance in Meters: ")
            try:
                if float(answer) == 7500:
                    print("\nCorrect! You ran 7.5 kilometers in the first half.")
                    return True  # Success, move to next chapter
                else:
                    print("\nThat’s not correct. Try again!")
            except ValueError:
                print("\nPlease enter a valid number.")
