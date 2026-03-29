a = {1, 2, 3, 4, 5}
b = {2, 4, 6, 7, 8}

print("Set A: ", a)
print("Set B: ", b)

print("Union: ", a.union(b))

print("Intersection:", a.intersection(b))

print("Difference (A - B):", a - b)

print("Difference (B - A):", b - a)

print("Symmetric Difference:", a ^ b)