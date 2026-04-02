student = ["Wrik", "Kashif", "Mazin", "Tahmid"]
marks = (70, 67, 56, 24)

if len(student) != len(marks):
    print("Data mismatch deleted. Exiting system.")
    exit()

bonus_marks = list(map(lambda x: x + 5, marks))

def get_grade(mark):
    if mark >= 70:
        return "A"
    elif mark >= 60:
        return "B"
    elif mark >= 40:
        return "C"
    else:
        return "F"
    
grades = list(map(get_grade, bonus_marks))

def performance_label(grade):
    if grade == "A":
        return "Excellent"
    elif grade == "B":
        return "Good"
    elif grade == "C":
        return "Average"
    else:
        return "Fail"
    
labels = list(map(performance_label, grades))

student_data = list(zip(student, marks, bonus_marks, grades, labels))

print("-" * 40)
print("Student Performance Report")



total = 0
fail_count = 0

for name, original, updated, grade, label in student_data:
    total += updated

    print("Name:", name)
    print("Original marks:", marks)
    print("After Bonus:", updated)
    print("Performance:", label)
    print("-" * 40)


    if grade == "F":
        fail_count += 1