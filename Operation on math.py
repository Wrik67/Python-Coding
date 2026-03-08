import math

def power_and_root():
    num = float(input("Enter number: "))
    power = float(input("Enter power:"))
    print("Power:", math.pow(num, power))

def factorial_calculation():
    num = int(input("Enter integer: "))
    print("Factorial:", math.factorial(num))

def circle_calculation():
    r = float(input("Enter radius:"))
    area = math.pi * r * r
    print("Area of circle:", area)

while True:
    print("\n------Math Operation------")
    print("1. Power ")
    print("2. Factorial ")
    print("3. Circle ")
    print("4. Exit ")

    choice = input("Select option: ")

    if choice == "1":
        power_and_root() 
    elif choice == "2":
        factorial_calculation() 
    elif choice == "3":
        circle_calculation()
    elif choice == "4":
        print("Program Ended")
        break
    else:
        print("Invalid option")