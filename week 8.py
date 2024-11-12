# def checkRange(r):
#     if r in range(1,10):
#             print(f"The {r} is in range")
#     else:
#             print(f"The {r} is not in range")
#
# def main():
#     num = int(input("Enter number:  "))
#     checkRange(num)
#
# if __name__ == "__main__":
#     main()


list = [3,4,3,3,5]

newList = []

for i in list:
    if i in newList:
        pass
    else:
        newList.append(i)