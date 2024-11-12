


class Character:
    def __init__(self, playerName,favWeapon): #Constructor
        self.playerName = playerName
        self.favWeapon = favWeapon

    def printFav(self):
        print(f"The player is: {self.playerName}, likes {self.favWeapon}")


def main():
    myPlayer = Character("Antonio", "wand")
    myPlayer2 = Character("Alikhan", "sword")

    print(f"This is player 1: {myPlayer.playerName}, {myPlayer.favWeapon}")
    print(f"This is player 2: {myPlayer2.playerName}, {myPlayer2.favWeapon}")

    myPlayer.printFav()





if __name__ == "__main__":
    main()