# Question No 1 with specific subjects

subjects = ["English", "Urdu", "Maths", "Physics", "Chemistry"]
marks = []

# Loop to enter marks with subject names
for subject in subjects:
    m = int(input(f"Enter marks of {subject}: "))
    marks.append(m)

total = sum(marks)
percentage = (total / 500) * 100  # 5 subjects x 100 = 500

# Grade logic
if percentage >= 80:
    grade = "A+"
elif percentage >= 70:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"

# Pass/Fail
if percentage >= 40 and all(m >= 40 for m in marks):
    result = "Pass"
else:
    result = "Fail"

print("\n--- Result ---")
for i in range(5):
    print(f"{subjects[i]}: {marks[i]}")

print(f"\nTotal Marks: {total} / 500")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
print(f"Result: {result}")
