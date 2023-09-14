#scientific calculator
import math

while True:
    print("\n\t\t\tChoose the Math Operation\n\n1 ->Addition\n2 ->Subtraction\n3 ->Multiplication\n4 -> Division\n5 ->Modulus\n6 ->Integer Division\n7->raising to a power\n8 -> Square Root of a number\n9 -> Logarithm\n10 -> Sine\n11 -> cosine\n12 -> tangent\n")

    #prompt the user for an application
    operation = int(input("Enter your option from the menu"))

    #check users choice /opration
    #Addition
    if operation == 1:
        print ("\t\t\t Addition")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"The sum of {num1} and {num2} is {num1 + num2}")

        #Go back to the menu or exit program
        back = input("\nGo back to the main menu ? (y/n): ")

        if back.lower() == "y":
            continue
        else:
            break
    #subtration
    elif operation == 2:
        print ("\t\t\t Substraction")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"The sum of {num1} and {num2} is {num1 - num2}")

        #Go back to the menu or exit program
        back = input("\nGo back to the main menu ? (y/n): ")

        if back.lower() == "y":
            continue
        else:
            break
    #Multiplication
    elif operation == 3:
        print ("\t\t\t Multiplication")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"The sum of {num1} and {num2} is {num1 * num2}")

        #Go back to the menu or exit program
        back = input("\nGo back to the main menu ? (y/n): ")

        if back.lower() == "y":
            continue
        else:
            break

    # DIVISON
    elif operation == 4:
        print ("\t\t\t Divison")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"The sum of {num1} and {num2} is {num1 / num2}")

        #Go back to the menu or exit program
        back = input("\nGo back to the main menu ? (y/n): ")

        if back.lower() == "y":
            continue
        else:
            break

    #modulus
    elif operation == 5:
        print ("\t\t\t Modulus")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"The sum of {num1} and {num2} is {num1 % num2}")

        #Go back to the menu or exit program
        back = input("\nGo back to the main menu ? (y/n): ")

        if back.lower() == "y":
            continue
        else:
            break

    #integer divison 
    elif operation == 6:
        print("\t\t\t integer Divison")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"The sum of {num1} and {num2} is {num1 // num2}")

        #Go back to the menu or exit program
        back = input("\nGo back to the main menu ? (y/n): ")

        if back.lower() == "y":
            continue
        else:
            break
        
    #raising power
    elif operation == 7:
        print ("\t\t\t Addition")
        base = float(input("Enter the base: "))
        power = float(input("Enter the exponent: "))
        print(f"The power of {base} raised to {power} is {pow(base, power)}")
     
        #Go back to the menu or exit program
        back = input("\nGo back to the main menu ? (y/n): ")

        if back.lower() == "y":
            continue
        else:
            break

    #square root of a number 
    
    elif operation == 8:
        print("\t\t\t Square root")
        num = float(input("Enter a number to get its square root: "))
        print(f"The square root of {num} is {round(math.sqrt(num),4)}")

         #Go back to the menu or exit program
        back = input("\nGo back to the main menu ? (y/n): ")

        if back.lower() == "y":
            continue
        else:
            break

    #logarithm
    elif operation == 9:
        print("\t\t\t Logarithm")
        num = float(input("Enter a number to calculate the logarithm to base 2: "))
        print(f"The log of {num} is {round(math.log(num,2),4)}")

        # Go back to the menu or exit program
        back = input("\nGo back to the main menu ? (y/n): ")

        if back.lower() == "y":
            continue
        else:
            break

    #sine
    elif operation == 10:
        print("\t\t\t Sine")
        num = float(input("Enter an angle in degrees to get its sine: "))
        print(f"The sine of {num} is {round(math.sin(math.radians(num)),4)}")

        #Go back to the menu or exit program
        back = input("\nGo back to the main menu ? (y/n): ")

        if back.lower() == "y":
            continue
        else:
            break

    #cos
    elif operation == 11:
        print("\t\t\t cos")
        num = float(input("Enter an angle to get its cos: "))
        print(f"The cos of {num} is {round(math.cos(math.radians(num)),4)}")

        #Go back to the menu or exit program
        back = input("\nGo back to the main menu ? (y/n): ")

        if back.lower() == "y":
            continue
        else:
            break

    #tangent
    elif operation == 12:
        print("\t\t\t Tangent")
        num = float(input("Enter an angle to get its tan: "))
        print(f"The tan of {num} is {round(math.tan(math.radians(num)),4)}")

        #Go back to the menu or exit program
        back = input("\nGo back to the main menu ? (y/n): ")

        if back.lower() == "y":
            continue
        else:
            break
    
    else:
        print("\nInvalid Choice Try Again!!!")
