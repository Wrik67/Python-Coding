n = int(input("Enter the number in rows: "))

for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print()