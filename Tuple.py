marks = (10, 20, 30, 40, 50)
fruits = ("apple", "banana", "cherry", "banana")

print("1. Accessing an Element:", marks[2])
print("2. Slicing:", marks[1:4])
print("3. Length:", len(fruits))
print("4. Count:", fruits.count("banana"))
print("5. Index:", fruits.index("cherry"))

t3 = marks + fruits
print("6. Concatenation:", t3)

t4 = marks * 2
print("7. Repitition:", t4)
print("8. Membership cheak:", 30 in marks)
lst = list(marks)
print("9. Tuple to list:", lst)