student = {
    "name": "Wrik",
    "age": "10",
    "grade": "3",
    "city": "Dhaka"
}

print("Original Dictionary:")
print(student)

print("\nName:", student["name"])
print("Age using get():", student["age"])

student["school"] = "Heed International School"
print("\nAfter Adding New Field: ")
print(student)

student["age"] = 12
print("\nAfter Updating Age:")
print(student)

removed = student.pop("city")
print("\nRemoved City:", removed)
print("After pop():", student)

print("\nKeys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

copy_student = student.copy()
print("\nCopy of student:", copy_student)

student.update({"grade": "4"})
print("\nAfter update:", student)

val = student.setdefault("hobby", "Reading books")
print("\nAfter setdefault():", student)