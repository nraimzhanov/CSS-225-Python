direction = input("Which way would you like to go [left]  [right]:")
print(direction)
if direction.casefold() == "left":
    print("Going left")
elif direction.casefold() == "right":
    print("Going right")
else:
    print("invalid direction!")