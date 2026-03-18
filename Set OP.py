# Set data
a = {1, 2, 3, 4, 5}
b = {2, 4, 6, 7, 8}

print("Set A: ", a)
print("Set B: ", b)

# Union
print("Union: ", a.union(b))

# Intersection
print("Intersection:", a.intersection(b))

# Difference (A - B)
print("Difference (A - B):", a - b)

# Difference (B - A)
print("Difference (B - A):", b - a)

# Symmetric Difference
print("Symmetric Difference:", a ^ b)