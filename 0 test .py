student = {
    "name": "Wrik",
    "Age": "10",
    "roll": "07",
    "Adress": "Mirpur 11",
    "Class": "STD-3",
    "city": "Dhaka"
}

print("---Original Dictionary---")
print(student)

print("Name: ", student["name"])
print("Age: ", student["Age"])
print(student)

student["school"] = "Heed International School"
print("\nAfter Adding New Field:")
print(student)

student["roll"] = "01"
print("\nAfter Updating Age:")
print(student)

removed = student.pop("Adress")
print("\nRemoved city:", removed)
print("After pop: ", student)

print("\nkeys:", student.keys())
print("\nvalues:", student.values())
print("\nitems:", student.items())

copy_student = student.copy()
print("\nCopy of student", copy_student)

student.update({"Class": "4"})
print("\nAfter update:", student)

val = student.setdefault("hobby", "Reading books")
print("\nAfter setdefault():", student)