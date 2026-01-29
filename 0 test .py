import math

def hexagonarea(side):
    area = (3 * math.sqrt(3) * (side ** 2)) / 2
    return area
def octagonarea(side_length):
    """
    Calculates the area of a regular octagon given its side length.
    Formula: Area = 2 * side^2 * (1 + sqrt(2))
    """
    if side_length <= 0:
        return "Side length must be positive"
    area = 2 * (side_length ** 2) * (1 + math.sqrt(2))
    return area

def squareArea(side):
    area = side * side 
    return area
def circleArea(Radius):
    area = 3.15169 * Radius ** 2
    return area

print("Area calculator")
print("Choose a shape: ")
print("1.Hexagon")
print("2.Octagon")
print("3.Square")
print("4.Circle")

choice = int(input("Enter your choice from 1/2/3/4: "))
if choice ==1:

    s = float(input("Enter the side of Hexagon: "))
    print("The area of Rectangle is: ", hexagonarea(s))
elif choice ==2:

    s = float(input("Enter the side of Octagon: "))
    print("The area of Octagon  is: ", octagonarea(s))

elif choice ==3:

    s = float(input("Enter the side of square: "))
    print("The area of square  is: ", squareArea(s))

elif choice ==4:

    r = float(input("Enter the radius of circle: "))
    print("The area of circle  is: ", circleArea(r))

else:
    print("Invalid input!")