#Simple Calculator

#Init
#Function
#Adds num1 and num2 and prints the result
def add(num1, num2):
    result = num1 + num2
    print("The result is " + str(result))

def subtract(num1, num2):
    result = num1 - num2
    print("The result is " + str(result))

def multiply(num1, num2):
    result = num1 * num2
    print("The result is " + str(result))

def divide(num1, num2):
    result = num1 / num2
    print("The result is " + str(result))

def simpleCalculator():
    print("Welcome Preschoolers to Simple Calculator!")
    while True:
        print("Enter an operation: ")
        print("""1.Addition
        2.Subtraction
        3.Divison
        4.Multiplication
        5.Quit""")
        operation = int(input("(1-5)Operation :"))
        if operation == 1: #Keep the data types the same
            int1 = int(input("Enter your first number: "))
            int2 = int(input("Enter your second number: "))
            add(int1, int2)
        if operation == 2:
            int1 = int(input("Enter your first number: "))
            int2 = int(input("Enter your second number: "))
            subtract(int1, int2)
        if operation == 3:
            int1 = int(input("Enter your first number: "))
            int2 = int(input("Enter your second number: "))
            multiply(int1, int2)
        if operation == 4:
            int1 = int(input("Enter your first number: "))
            int2 = int(input("Enter your second number: "))
            divide(int1, int2)
        if operation == 5:
            break
#Main
simpleCalculator()
