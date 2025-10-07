name = input("Enter student's name: ")
roll_no = input("Enter roll number: ")

num_subjects = int(input("Enter number of subjects: "))
marks = []
total_marks = 0

for i in range(num_subjects):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)
    total_marks += mark

percentage = total_marks / num_subjects

if percentage >= 90:
    grade = 'A+'
elif percentage >= 80:
    grade = 'A'
elif percentage >= 70:
    grade = 'B+'
elif percentage >= 60:
    grade = 'B'
elif percentage >= 50:
    grade = 'C'
elif percentage >= 40:
    grade = 'D'
else:
    grade = 'F'

print("\n----- Student Report -----")
print(f"Name      : {name}")
print(f"Roll No   : {roll_no}")
print(f"Subjects  : {num_subjects}")
print(f"Marks     : {marks}")
print(f"Total     : {total_marks}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade     : {grade}")
print("--------------------------")
