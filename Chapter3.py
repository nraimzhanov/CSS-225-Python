def overcomeObstacles():
    print("Chapter 3: Overcoming Obstacles in Training...")
    obstacles = ["Larger opponents", "Stamina issues", "Pressure to succeed"]

    for obstacle in obstacles:
        print(f"Facing challenge: {obstacle}...")
        response = input(f"How will you overcome {obstacle}? (Type your action): ")
        print(f"Your response to {obstacle}: {response}. Keep pushing!")

    print("You overcame the obstacles and improved your game!")
    return True  # Success
