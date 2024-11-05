def printnnumber(num):
    print("This is the calling program: ", __name__)
    for i in num:
        print("This is number", i)

def main():
    i = "Antonio"
    print("This is item: ", i)
    printnnumber([10])
    print("This is item: ", i)

if __name__ == "__main__":
    main()
