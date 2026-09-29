# PRACTICAL PRACTICE QUESTIONS
# LEVEL 1 — LIST BASICS
# Q1
# Create a list containing:
# 10, 20, 30, 40, 50
# Print the list and its type.

l1 =[10,20,30,40,50]
print(l1, type(l1))
print("\n")


# Q2
# Create a list of 5 student names and print the first and last student.

students = ["ankit","raj","lokesh","lalit","aniket"]
print("First student is :", students[0], "\nLast student is :", students[-1])
print("\n")

# Q3
# Given:
# numbers = [10, 20, 30, 40, 50]
# Print:
# •	First element
# •	Third element
# •	Last element
# •	Second-last element


l1 =[10,20,30,40,50]

print("First element is :", l1[0], "\nThird element is :", l1[2], "\nLast element is :", l1[-1],"\nsecond last element is :", l1[-2])

print("\n")



# Q4
# Given:
# numbers = [10, 20, 30, 40, 50, 60]
# Print:
# [20, 30, 40]
# using slicing.


l1 =[10,20,30,40,50]
print(l1[1:4])
print("\n")


# Q5
# Print every element of this list using a for loop:
# courses = ["Python", "Java", "Django", "React", "Node"]
# ______________


courses = ["Python", "Java", "Django", "React", "Node"]
for i in courses:
    print(i)


print("\n")


# LEVEL 2 — LIST METHODS


# Q6
# Create:
# numbers = [10, 20, 30, 40]
# Add 50 at the end using append().

numbers = [10, 20, 30, 40]
numbers.append(50)
print(numbers)

# Q7
# Insert 5 at index 0.
numbers = [10, 20, 30, 40]
numbers.insert(0,5)
print(numbers)
print("\n")


# Q8
# Remove 30 using remove().

numbers = [10, 20, 30, 40]
numbers.remove(30)
print(numbers)
print("\n")

# Q9
# Remove the last element using pop().
numbers = [10, 20, 30, 40]
numbers.pop()
print(numbers)
print("\n")

# Q10
# Delete the element at index 1 using del.
numbers = [10, 20, 30, 40]
del numbers[0]
print(numbers)
print("\n")


# Q11
# Create:
# a = [1, 2, 3]
# b = [4, 5, 6]
# Combine them using extend().

a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)
print("\n")




# ______________
# LEVEL 3 — PRACTICAL PROBLEMS
# Q12 — Student Marks
# Given:
# marks = [78, 89, 56, 92, 67, 45]
# Find:
# 1.	Maximum marks
# 2.	Minimum marks
# 3.	Total marks
# 4.	Number of students

marks = [78, 89, 56, 92, 67, 45]
print("Maximum marks :", max(marks))
print("Minimum marks :", min(marks))
print("Total marks :", sum(marks))
print("Number of students :", len(marks))
print("\n")

# ______________
# Q13 — Even Numbers
# Given:
# numbers = [10, 15, 20, 25, 30, 35, 40]
# Create a new list containing only even numbers.
# Expected output:
# [10, 20, 30, 40]


numbers = [10, 15, 20, 25, 30, 35, 40]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)
print("\n")

# ______________
# Q14 — Square Numbers
# Given:
# numbers = [1, 2, 3, 4, 5]
# Create:
# [1, 4, 9, 16, 25]
# using list comprehension.


numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)
print("\n")


# ______________
# Q15 — Names and Marks
# Use zip() with:
# names = ["Rahul", "Aman", "Priya", "Neha"]

# marks = [80, 75, 90, 85]
# Expected output:
# Rahul 80
# Aman 75
# Priya 90
# Neha 85


names = ["Rahul", "Aman", "Priya", "Neha"]
marks = [80, 75, 90, 85]

for name, mark in zip(names, marks):
    print(name, mark)

print("\n")


# ______________
# LEVEL 4 — NESTED LIST
# Q16
# Given:
# data = [10, 20, [30, 40, 50]]
# Print:
# 50


data = [10, 20, [30, 40, 50]]
print(data[2][2])
print("\n")


# ______________
# Q17
# Given:
# data = [10, [20, 30], [40, [50, 60]]]
# Print:
# 60

data = [10, [20, 30], [40, [50, 60]]]
print(data[2][1][1])
print("\n")


# ______________
# Q18
# Create a nested list containing:
# Student Name
# Course
# Marks
# Access each value individually.

 


# ______________
# LEVEL 5 — DICTIONARY
# Q19
# Create a dictionary containing:
# name
# age
# course
# city
# Print all values.

student = {
    "name": "Raaj",
    "age": 31,
    "course": "C++",
    "marks": 89
}
print(student)
print("\n")



# ______________
# Q20
# Given:
student = {
    "name": "Rahul",
    "age": 21,
    "course": "Python",
    "marks": 85
}
# Print:
# 1.	Student name
# 2.	Course
# 3.	Marks

print("Student name:", student["name"])
print("Course:", student["course"]) 
print("Marks:", student["marks"])

# ______________
# Q21
# Use keys() to print all keys.

print(student.keys())
print("\n")


# ______________
# Q22
# Use values() to print all values.

print(student.values())
print("\n")



# ______________
# Q23
# Use items() to print:
# name Rahul
# age 21
# course Python
# marks 85

print(student.items())
print("\n")


# ______________
# LEVEL 6 — NESTED DICTIONARY
# Q24
# Create:
students = {
    "student1": {
        "name": "Rahul",
        "course": "Python",
        "marks": 85
    },

    "student2": {
        "name": "Aman",
        "course": "Java",
        "marks": 78
    }
}
# Print:
# •	Rahul
# •	Python
# •	85
# •	Aman
# •	Java
# •	78

print("Name of the first student is :",students["student1"]["name"])
print("First student's course is :",students["student1"]["course"])   
print("First student's marks is :",students["student1"]["marks"])
print("Name of the second student is :",students["student2"]["name"])
print("Second student's course is :",students["student2"]["course"])   
print("Second student's marks is :",students["student2"]["marks"])