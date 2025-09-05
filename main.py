# main.py
import addition
import subtraction
import multiplication
import division
import modulusDivision
import power
import squares

operations = {
    1: "Addition",
    2: "Subtraction",
    3: "Multiplication",
    4: "Division",
    5: "Modulus Division",
    6: "power",
    7: "squares"
}

# main function
if __name__ == "__main__":
        print("Welcome to simple calculator, It will do two number operations")
        
        while True:
            for i in sorted(operations.keys()):
                print(f"{i}. {operations[i]}")
            choice = int(input("Please select your operation(1-8): "))
            if choice == 1:
                num1 = int(input("Enter number 1: "))
                num2 = int(input("Enter number 2: "))
                print(addition.add(a = num1, b = num2))
            elif choice == 2:
                num1 = int(input("Enter number 1: "))
                num2 = int(input("Enter number 2: "))
                print(subtraction.sub(a = num1, b = num2))
            elif choice == 3:
                num1 = int(input("Enter number 1: "))
                num2 = int(input("Enter number 2: "))
                print(multiplication.mul(a = num1, b = num2))
            elif choice == 4:
                num1 = int(input("Enter number 1: "))
                num2 = int(input("Enter number 2: "))
                print(division.div(a = num1, b = num2))
            elif choice == 5:
                num1 = int(input("Enter number 1: "))
                num2 = int(input("Enter number 2: "))
                print(modulusDivision.modDiv(a = num1, b = num2))
            elif choice == 6:
                num1 = int(input("Enter number 1: "))
                num2 = int(input("Enter number 2: "))
                print(power.pow(a = num1, b = num2))
            elif choice == 7:
                num1 = int(input("Enter number 1: "))
                print(squares.square(a = num1))
                
            elif choice == 8:
                print("exiting from calculator")
                exit()
            else:
                print("Please select the operation between 1-8")
                
                
            