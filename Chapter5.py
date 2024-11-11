def makeKeyDecisionsDuringMatch():
    print("Chapter 5: The World Stage - FIFA World Cup...")
    print("This is it—the final match in the World Cup. You need to make key decisions.")

    action = input("You are in a critical position. Do you: 1. Pass the ball 2. Shoot for goal 3. Wait for support: ")
    if action == '1':
        print("You pass the ball to a teammate who scores! Great team effort!")
        return True  # Success
    elif action == '2':
        print("You shoot and score! The crowd erupts in cheers!")
        return True  # Success
    else:
        print("You decide to wait. The support comes and the team scores a great goal!")
        return True  # Success
