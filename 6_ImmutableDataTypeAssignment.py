
# PRACTICAL PRACTICE QUESTIONS (string, tuples, set)


# Question 1 — String Iteration
# Given:
# text = "CodeDesk Python Course"
# Use a for loop to print every character on a separate line.

text = "CodeDesk Python Course"

for i in text:
    print(i)
print("\n")

# _____________________________________________________________________________________________________________________
# _____________________________________________________________________________________________________________________
# ______________

# Question 2 — Case Conversion
# Given:
# text = "welcome to codedesk"
# Print:
# WELCOME TO CODEDESK
# welcome to codedesk
# Welcome to codedesk
# using the appropriate string methods.

text = "welcome to codedesk"
print("Upper:",text.upper())
print("Lower:",text.lower())
print("Capitalize:",text.capitalize())
print("\n")


# _____________________________________________________________________________________________________________________
# _____________________________________________________________________________________________________________________
# ______________


# Question 3 — Find Character
# Given:
# text = "python programming"
# Find the position of:
# p
# g
# z
# Use the find() method.

text = "python programming"
print(text.find('p'))
print(text.find('g'))
print(text.find('z'))
print("\n")

# _____________________________________________________________________________________________________________________
# _____________________________________________________________________________________________________________________
# ______________


# Question 4 — Find vs Index
# Given:
# text = "hello python"
# Try to find "z" using:
# find()
# index()
# Observe what happens in each case.

# text = "hello python"

# print(text.find('z'))
# print(text.index('z'))
print("\n")


# _____________________________________________________________________________________________________________________
# _____________________________________________________________________________________________________________________
# ______________

# Question 5 — Dynamic String
# Create these variables:
# name = "Rahul"
# course = "Python"
# institute = "CodeDesk"
# Using format(), create this output:
# My name is Rahul. I am learning Python at CodeDesk.

str = "My name is {name}. I am learning {course} at {institute}".format(name="Rahul", course = "Python", institute ="CodeDesk"  )
print(str)
print("\n")

# _____________________________________________________________________________________________________________________
# _____________________________________________________________________________________________________________________
# ______________

# Question 6 — Tuple Indexing and Slicing
# Given:
# courses = (
#     "Python",
#     "Java",
#     "React",
#     "Django",
#     "Data Science"
# )
# Print:
# 1.	First course
# 2.	Last course
# 3.	Second and third courses
# 4.	First three courses

courses = ("Python","Java","React","Django","Data Science")
print("First Course is:",courses[0])
print("Last Course is:",courses[-1])
print("Second Course is:",courses[1],"and Third Course is:",courses[2])
print("first three cources are:", courses[0:3])
print("\n")
# _____________________________________________________________________________________________________________________
# _____________________________________________________________________________________________________________________
# ______________


# Question 7 — Tuple Analysis
# Given:
# numbers = (10, 20, 30, 20, 40, 50, 20)
# Find:
# 1.	Minimum value
# 2.	Maximum value
# 3.	Total of all values
# 4.	Number of times 20 occurs
# 5.	Index of the first 40

numbers = (10, 20, 30, 20, 40, 50, 20)
print("Minimum value is:", min(numbers))
print("Maximum value is:", max(numbers))
print("Total of all values is:", sum(numbers))
print("Number of times 20 occurs:", numbers.count(20))
print("Index of the first 40 is:", numbers.index(40))
print("\n")

# _____________________________________________________________________________________________________________________
# _____________________________________________________________________________________________________________________
# ______________


# Question 8 — Tuple Iteration
# Given:
# skills = (
#     "Python",
#     "SQL",
#     "Pandas",
#     "Power BI",
#     "Excel"
# )
# Use a for loop to print every skill on a separate line.

skills = ("Python","SQL","Pandas","Power BI","Excel")
for i in skills:
    print(i)

print("\n")

# _____________________________________________________________________________________________________________________
# _____________________________________________________________________________________________________________________
# ______________

# Question 9 — Remove Duplicates
# Given:
# numbers = (
#     10, 20, 20, 30,
#     40, 30, 50, 50, 60
# )
# Convert this tuple into a set and print only the unique values.

numbers = (10, 20, 20, 30,40, 30, 50, 50, 60)
s1 = set(numbers)
print(s1)
print("\n")

# _____________________________________________________________________________________________________________________
# _____________________________________________________________________________________________________________________
# ______________

# Question 10 — Set Operations
# Given:
# skills = {"Python", "SQL", "Excel"}
# Perform the following:
# 1.	Add "Power BI"
# 2.	Add "Pandas"
# 3.	Remove "Excel" using discard()
# 4.	Iterate through the final set using a for loop
# 5.	Print the final set

skills = {"Python", "SQL", "Excel"}
skills.add('Power BI')
skills.add('Pandas')
skills.discard('Excel')
print ("final set is ")
for i in skills:
    print(i)
