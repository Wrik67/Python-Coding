def TriangleArea(Base,Hight):
    area = (Base*Hight)/2
    return area
def squareArea(side):
    area = side ** 2
    return area
def rectangleArea(Lenth,Width):
    area = Lenth * Width
    return area
def circleArea(Radius):
    area = 3.15169 * Radius ** 2
    return area

print("Area calculator")
print("Choose a shape: ")
print("1.Rectangle")
print("2.Triangle")
print("3.Square")
print("4.Circle")

choice = int(input("Enter your choice from 1/2/3/4: "))
if choice ==1:

    l = float(input("Enter the lenth of rectangle: "))
    w = float(input("Enter the width of rectangle: "))
    print("The area of Rectangle is: ", rectangleArea(l,w))
elif choice ==2:

    b = float(input("Enter the base of triangle: "))
    h = float(input("Enter the hight of triangle: "))
    print("The area of triangle  is: ", TriangleArea(b,h))

elif choice ==3:

    s = float(input("Enter the side of square: "))
    print("The area of square  is: ", squareArea(s))

elif choice ==4:

    r = float(input("Enter the radius of circle: "))
    print("The area of circle  is: ", circleArea(r))

else:
    print("Invalid input!")