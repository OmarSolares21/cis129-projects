# Module 11: Class Average Exercises
# By Omar Solares

# Writing grades to a plain text file
grades = []
print("Enter grades (type 'done' to finish):")
while True:
    grade = input()
    if grade.lower() == 'done':
        break
    grades.append(grade)

with open('grades.txt', 'w') as file:
    for grade in grades:
        file.write(f"{grade}\n")