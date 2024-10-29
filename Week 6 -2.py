# def adding(num1, num2):
#     if num1 == num2:
#         result = num1 + num2
#         return result
#     return 0
# def multiply(num1, num2):
#     result = num1 * num2
#     return result
# def division(num1, num2):
#     result = num1 / num2
#     return result

# def askUser(message):
#     answer = input(message)
#     return answer

# userHeight = float(input("Enter height of triangle: "))
# userBase = float(input("Enter base of triangle: "))
# def areaOfTriangle(height, base):
#     result = 1/2*height*base
#     return resul

userInput = float(input("Enter your height in feet: "))
userInput2 = float(input("Enter your height in inch: "))
def convertHeightToCm(feet, inch):

    result1 = (feet * 12) + inch
    result2 = result1 * 2.54
    return result2


def main ():
    #print(areaOfTriangle(userHeight,userBase))
    print(convertHeightToCm(userInput,userInput2),"cm")
    # print("Hello")
    # print(adding(2,3))
    # print(multiply(9,87))
    # print(division(193043,907))
    # print(askUser("What do you want to do next?  "))
    # print(askUser("What is your favorite color?  "))

if __name__ == "__main__":
    main()

