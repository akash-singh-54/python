# MINI PROJECT — STUDENT MANAGEMENT SYSTEM
# Create a dictionary containing 3 students.
# Each student should have:
# name
# age
# course
# marks
# city


students = {

    "student1": {
        "name": "Rahul",
        "age": 21,
        "course": "Python",
        "marks": 85,
        "city": "Jaipur"
    },

    "student2": {
        "name": "Aman",
        "age": 22,
        "course": "Java",
        "marks": 78,
        "city": "Jaipur"
    },

    "student3": {
        "name": "Priya",
        "age": 20,
        "course": "Django",
        "marks": 92,
        "city": "Ajmer"
    },

    "student4": {
        "name": "Rohit",
        "age": 23,
        "course": "C++",
        "marks": 89,
        "city": "Jaipur"
    },

    "student5": {
        "name": "Sneha",
        "age": 21,
        "course": "JavaScript",
        "marks": 95,
        "city": "Udaipur"
    },

    "student6": {
        "name": "Ankit",
        "age": 22,
        "course": "Python",
        "marks": 88,
        "city": "Ajmer"
    },

    "student7": {
        "name": "Neha",
        "age": 20,
        "course": "Django",
        "marks": 92,
        "city": "Ajmer"
    }

}


# Tasks
# 1.	Display all students.

print("All students:")
for student_id, student_info in students.items():
    print("{student_id}: {student_info}".format(student_id=student_id, student_info=student_info))
print("\n")



# 2.	Display all student names.
print("Student Names:")
for student_info in students.values():
    print(student_info["name"])
print("\n") 



# 3.	Display all courses.
print("Courses:")
for student_info in students.values():
    print(student_info["course"])
print("\n")
 

# 4.	Display all marks.
print("Marks:")
for student_info in students.values():
    print(student_info["marks"])
print("\n")



# 5.	Find the highest marks.
highest_marks = max(student["marks"] for student in students.values())
print("Highest Marks:", {highest_marks})
print("\n")



# 6.	Find the lowest marks.
lowest_marks = min(student["marks"] for student in students.values())
print("Lowest Marks:", {lowest_marks})
print("\n")



# 7.	Display the complete information of a specific student.
print("Complete Information of a Specific Student:")
student_id = input("Enter student ID (e.g., student1): ")
if student_id in students:
    print(students[student_id])
else:
    print("Student not found.")
print("\n")



# 8.	Count the total number of students.
total_students = len(students)
print("Total Number of Students:", {total_students})
print("\n")



# 9.	Display students whose marks are greater than 80.
print("Students with Marks greater than 80:")
for student_info in students.values():
    if student_info["marks"] > 80:
        print(student_info["name"])
print("\n") 



# 10.	Display students who are from Jaipur.
print("Students from Jaipur:")
for student_info in students.values():
    if student_info["city"] == "Jaipur":
        print(student_info["name"])


# ______________
# 