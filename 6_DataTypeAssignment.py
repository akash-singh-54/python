# Python Data Types Practice Questions

# 1. Student Information
#Create variables for:
name = "Rahul"
age = 21
percentage = 82.5
is_student = True
# Print every value along with its data type.

print("Name:", name, "Type:", type(name))
print("Age:", age, "Type:", type(age))
print("Percentage:", percentage, "Type:", type(percentage))
print("Is Student:", is_student, "Type:", type(is_student))
print("\n")


# _____________________________________________________________________________________________________________________
# ____________________________________________________________________________________________________________________
# 2. Employee Information
# Create:
name = "Amit"
salary = 35000
experience = 2.5
is_active = True
# Print all values and their data types.

print("Name:", name, "Type:", type(name))
print("Salary:", salary, "Type:", type(salary))
print("Experience:", experience, "Type:", type(experience))
print("Is Active:", is_active, "Type:", type(is_active))
print("\n")


# _____________________________________________________________________________________________________________________
# _____________________________________________________________________________________________________________________
# 3. String Indexing
# Given:
text = "Python"
# Print:
# •	First character
# •	Second character
# •	Third character
# •	Last character

print("First character:", text[0])
print("Second character:", text[1])
print("Third character:", text[2])
print("Last character:", text[-1])
print("\n")


# _____________________________________________________________________________________________________________________
# _____________________________________________________________________________________________________________________
# 4. Negative Indexing
# Given:
text = "Programming"
# Print:
# •	Last character
# •	Second-last character
# •	Third-last character
# •	Fifth-last character
# Use negative indexing.

print("Last character:", text[-1])
print("Second-last character:", text[-2])
print("Third-last character:", text[-3])
print("Fifth-last character:", text[-5])
print("\n")

# _____________________________________________________________________________________________________________________
# _____________________________________________________________________________________________________________________
# 5. len() 
# Given:
# name = "CodeDesk"
# Print:
# •	Total length

name = "CodeDesk"
print("Total length of the string:", len(name))
print("\n")

#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

# 6. Mobile Number
# Given:
mobile = "9876543210"
# Print:
# •	First digit
# •	Third digit
# •	Last digit
# •	Second-last digit
# •	Total number of digits

    
print("First digit:", mobile[0])
print("Third digit:", mobile[2])
print("Last digit:", mobile[-1])
print("Second-last digit:", mobile[-2])
print("Total number of digits:", len(mobile))
print("\n")

# _____________________________________________________________________________________________________________________
# _____________________________________________________________________________________________________________________