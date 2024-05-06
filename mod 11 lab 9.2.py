# Module 11: Class Average Exercises
# By Omar Solares

# Reading grades from a plain text file
with open('grades.txt', 'r') as file:
    grades = file.readlines()

grades = [int(grade.strip()) for grade in grades]
total = sum(grades)
count = len(grades)
average = total / count

print("Grades:", grades)
print(f"Total: {total}, Count: {count}, Average: {average:.2f}")