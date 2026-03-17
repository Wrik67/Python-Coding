data = [120, 20, 25, 40, 200, 57, 150, 160, 90, 150, 85, 190, 20, 30, 205, 20]
fruits = ["Mango", "Banana", "Apple"]

print("Original list:", data)
print("Original list:", fruits)

# Append
data.append(200)
print("After append:", data)

fruits.append("Pineapple")
print("After append:", fruits)

# Extend
data.extend([300, 400, 255, 625])
print("After extand:", data)

fruits.extend(["Cherry", "Guava", "Watermelon"])
print("After extand:", fruits)

# Insert
data.insert(2, 150)
print("After insert at index 2:", data)

# Count
countdata = data.count(20)
print("Count of 20:", countdata)

# Sort
data.sort()
print("After sort:", data)

# Reverse
data.reverse()
print("After reverse:", data)