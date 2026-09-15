# Coding Task:
import json

class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks

    def display(self):
        print("ID:", self.student_id)
        print("Name:", self.name)
        print("Marks:", self.marks)

student = Student(101, "Hemanth", 85)

# Save student to JSON
student_data = {
    "student_id": student.student_id,
    "name": student.name,
    "marks": student.marks
}

with open("student.json", "w") as file:
    json.dump(student_data, file, indent=4)

print("Student data saved successfully.")

# Read student from JSON
with open("student.json", "r") as file:
    data = json.load(file)

print("\nStudent details:")
print("ID:", data["student_id"])
print("Name:", data["name"])
print("Marks:", data["marks"])

# Assignment:

import json
students = [
    {
        "student_id": 101,
        "name": "Hemanth",
        "marks": 85
    },
    {
        "student_id": 102,
        "name": "Rahul",
        "marks": 78
    },
    {
        "student_id": 103,
        "name": "Suresh",
        "marks": 92
    }
]
with open("student.json","w") as file:
    json.dump(students,file,indent=4)
print("data saved")

with open("student.json","r") as file:
    data = json.load(file)
print("\nStudent Details:")

for student in data:
    print(
        "ID:", student["student_id"],
        "| Name:", student["name"],
        "| Marks:", student["marks"]
    )
