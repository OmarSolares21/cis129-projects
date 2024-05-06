# Module 11: Class Average Exercises
# By Omar Solares

import csv

students = []
print("Enter student info (type 'done' when finished):")
while True:
    first_name = input("First Name: ")
    if first_name.lower() == 'done':
        break
    last_name = input("Last Name: ")
    grades = input("Enter the three exam grades separated by space: ")
    grades = list(map(int, grades.split()))
    students.append([first_name, last_name] + grades)

with open('grades.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3'])
    for student in students:
        writer.writerow(student)