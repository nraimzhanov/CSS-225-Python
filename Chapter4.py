def competeInMatch():
    print("Chapter 4: National U-17 Match...")
    print("The big match is coming up. You are in the locker room, getting ready to face a tough team.")

    gameReady = input("Are you ready to play in the match? (y/n): ").lower()
    if gameReady == 'y':
        print("You step onto the field, the crowd cheers, and the match begins!")
        action = input("Make your move: pass, shoot, or defend: ").lower()
        if action == 'shoot':
            print("You take the shot and SCORE! Goal!")
            return True  # Success
        else:
            print("You missed the opportunity to score.")
            return False  # Failure
    else:
        print("You feel nervous, but your teammates encourage you. The match begins!")
        return False  # Failure
