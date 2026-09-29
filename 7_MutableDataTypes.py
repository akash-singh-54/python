# Mutable Data Types:- Mutable data types are those data types whose values can be changed after they are created. In Python, the most commonly used mutable data types are lists and dictionaries.

# Lists & Dictionaries
# ____________________________________________________________________________________________________________
# PART 1 — LIST
# 1. What is a List?
# A list is a mutable data type used to store multiple values in a single variable.
# Syntax
# list_name = [value1, value2, value3]
# Example
l1 = [10, 20, 30, 40, 50, 60]

print(l1)
print(type(l1))
# Output
# [10, 20, 30, 40, 50, 60]
# <class 'list'>
# Important Points
# •	List is mutable.
# •	List can store multiple values.
# •	List uses square brackets [ ].
# •	List supports indexing.
# •	List supports slicing.
# •	List can store different data types.
# •	List allows duplicate values.
# Example
data = [10, "Python", 2.5, True, 10]
print(data)


# ____________________________________________________________________________________________________________
# 2. List Indexing

# Indexing is used to access individual elements from a list.
# Indexing starts from 0.
# Value:   10   20   30   40   50
# Index:    0    1    2    3    4
# Example
l2 = [10, 20, 1.5, 1.8, "akash"]
print(l2[0])
print(l2[3])
print(l2[4])
# Output
# 10
# 1.8
# akash

# _______________________________________________________________________________________________________________
# 3. Negative Indexing

# Negative indexing starts from -1 from the last element.
# Value:       10    20    30    40
# Negative:   -4    -3    -2    -1
# Example

l1 = [10, 20, 30, 40]
print(l1[-1])
print(l1[-2])

# Output
# 40
# 30


# ______________________________________________________________________________________________________________

# 4. Nested List
# A list inside another list is called a nested list.
# Example

l3 = [10, 20, [30, [40, 50]]]
print(l3)

# To access 50:
# print(l3[2][1][1])

# Explanation
# l3
# ├── 10
# ├── 20
# └── [30, [40, 50]]
#           └── [40, 50]
#                 └── 50


# _________________________________________________________________________________________________________________


# 5. Complex Nested List:- Complex nested list is a list that contains multiple levels of nested lists.
# Example
l4 = [10, 20, [30, 40, 50, [60, 70, [80, 90, 100]]]]
# To access 100:
print(l4[2][3][2][2])


# ____________________________________________________________________________________________________________________


# 6. List Slicing:- list slicing is used to access multiple elements from a list.
# Slicing is used to access multiple elements from a list.
# Syntax
# list[start:end]
# The end index is not included.
# Example

l1 = [10, 20, 30, 40, 50, 60]
print(l1[1:4])

# Output
# [20, 30, 40]
# More Examples

print(l1[:3])
# Output:
# [10, 20, 30]

print(l1[2:])
# Output:
# [30, 40, 50, 60]

print(l1[:])
# Output:
# [10, 20, 30, 40, 50, 60]

# Slicing with Step

print(l1[0:6:2])
# Output:
# [10, 30, 50]


# ____________________________________________________________________________________________________________

# 7. List Iteration:- list iteration is used to access each element of a list one by one.
# Iteration means accessing list elements one by one.
# Example
l1 = [10, 20, 30, 40, 50]
for i in l1:
    print(i)

# Output
# 10
# 20
# 30
# 40
# 50

# Iteration with Index
l1 = [10, 20, 30, 40]
for i in range(len(l1)):
    print(i, l1[i])


# ____________________________________________________________________________________________________________

# 8. min()
# min() is used to find the smallest value.
# Example
l6 = [1.5, 1.1, 1.111, 1.9]
print(min(l6))

# Output
# 1.1

# _______________________________________________________________________________________________________________

# 9. max()
# max() is used to find the largest value.
# Example
l6 = [1.5, 1.1, 1.111, 1.9]
print(max(l6))
# Output
# 1.9

# ________________________________________________________________________________________________________________

# 10. del
# del is used to delete an element using its index.
# Example

l7 = [10, 20, 30, 40, 50, 60]
del l7[0]
print(l7)
# Output
# [20, 30, 40, 50, 60]

# Delete Multiple Elements

l7 = [10, 20, 30, 40, 50, 60]
del l7[1:3]
print(l7)

# __________________________________________________________________________________________________________________

# 11. pop()
# pop() removes an element using its index and returns the removed value.
# Example

l7 = [10, 20, 30, 40, 50, 60]
print(l7.pop(3))
print(l7)

# Output
# 40
# [10, 20, 30, 50, 60]

# Remove Last Element
l7.pop()
# If no index is provided, pop() removes the last element.

# __________________________________________________________________________________________________________________

# 12. remove()
# remove() removes an element using its value.

# Example

l7 = [10, 20, 30, 40, 50, 60]
l7.remove(20)
print(l7)
# Output
# [10, 30, 40, 50, 60]

# Difference
# del     → removes using index 
# pop()   → removes using index and returns the value
# remove  → removes using value

# __________________________________________________________________________________________________________________

# 13. insert()
# insert() is used to add an element at a specific position.
# Syntax
# list.insert(index, value)
# Example

l8 = [10, 20, 30, 40, 50]
l8.insert(0, 100)
print(l8)
# Output
# [100, 10, 20, 30, 40, 50]

# _________________________________________________________________________________________________________________

# 14. append()
# append() adds one element at the end of a list.
# Example

l8 = [10, 20, 30, 40, 50]
l8.append(200)
print(l8)
# Output
# [10, 20, 30, 40, 50, 200]
# Important
# append() adds the complete object as one element.

l8 = [10, 20, 30]
l8.append([40, 50])
print(l8)
# Output:
# [10, 20, 30, [40, 50]]

# ___________________________________________________________________________________________________________________
 
# 15. extend()
# extend() adds elements from another iterable into the list.
# Example

l9 = [1, 2, 3]
l10 = [4, 5, 6]
l9.extend(l10)
print(l9)
# Output
# [1, 2, 3, 4, 5, 6]

# _______________________________________________________________________________________________________________________

# 16. append() vs extend()

# append()
a = [1, 2, 3]
a.append([4, 5])
print(a)
# Output:
# [1, 2, 3, [4, 5]]

# extend()
a = [1, 2, 3]
a.extend([4, 5])
print(a)
# Output:
# [1, 2, 3, 4, 5]

# ________________________________________________________________________________________________________________________

# 17. zip()
# zip() is used to process corresponding elements from two or more iterables together.
# Example
l9 = [1, 2, 3]
l10 = [4, 5, 6]
for i, j in zip(l9, l10):
    print(i, j)

# Output
# 1 4
# 2 5
# 3 6

# Practical Example
names = ["Rahul", "Aman", "Priya"]
marks = [80, 90, 85]
for name, mark in zip(names, marks):
    print(name, mark)
# Output
# Rahul 80
# Aman 90
# Priya 85

# ________________________________________________________________________________________________________________

# 18. split()
# split() is a string method.
# It is used to break a string into multiple parts and returns a list.
# Example

str1 = "this is my python class"
str2 = str1.split()
print(str2)
# Output
# ['this', 'is', 'my', 'python', 'class']

# Split Using a Specific Character
str1 = "this is my python class"
str2 = str1.split("i")
print(str2)

# ________________________________________________________________________________________________________________

# 19. List Comprehension
# List comprehension is a short and concise way to create a new list.
# Normal Method: Print all even numbers from a list
l11 = [10, 20, 30, 40, 50, 25, 35, 45, 55]
l12 = []
for i in l11:
    if i % 2 == 0:
        l12.append(i)
print(l12)

# Using List Comprehension
l11 = [10, 20, 30, 40, 50, 25, 35, 45, 55]
l12 = [i for i in l11 if i % 2 == 0]
print(l12)
# Output
# [10, 20, 30, 40, 50]

# Syntax
# [expression for item in iterable if condition]

# Example: Print all the Squares
numbers = [1, 2, 3, 4, 5]
squares = [i ** 2 for i in numbers]
print(squares)
# Output
# [1, 4, 9, 16, 25]

# _________________________________________________________________________________________________________________________________________________
###################################################################################################################################################
# _________________________________________________________________________________________________________________________________________________
###################################################################################################################################################

# PART 2 — DICTIONARY

# 20. What is a Dictionary?
# A dictionary is a mutable data type used to store data in key-value pairs.

# Syntax
# dictionary_name = {
#     "key": "value"
# }

# Example
d1 = {
    "name": "CodeDesk",
    "course": "Python",
    "pincode": 302012
}

print(d1)
print(type(d1))


# Output
# {'name': 'CodeDesk', 'course': 'Python', 'pincode': 302012}
# <class 'dict'>

#____________________________________________________________________________
# Important Points
# •	Dictionary is mutable.
# •	Dictionary stores data in key-value pairs.
# •	Dictionary uses { }.
# •	Keys should be unique.
# •	Values can have different data types.
# •	Dictionary values are accessed using keys.
# •	Dictionary does not use normal numeric indexing like a list.
# ____________________________________________________________________________

#______________________________________________________________________________________________________________________________________________________________

# 21. Dictionary Access
# Values are accessed using their keys.

# Example
d1 = {
    "name": "CodeDesk",
    "course": "Python",
    "pincode": 302012
}

print(d1["name"])

# Output
# CodeDesk
# More Examples
print(d1["course"])
print(d1["pincode"])

# ________________________________________________________________________________________________________________________________________

# 22. Dictionary Iteration
# When we directly iterate over a dictionary, we get its keys.
d1 = {
    "name": "CodeDesk",
    "course": "Python",
    "pincode": 302012
}

for i in d1:
    print(i)

# Output
# name
# course
# pincode

# Get Values Using Keys
for i in d1:
    print(d1[i])
# Output
# CodeDesk
# Python
# 302012

# ________________________________________________________________________________________________________________________

# 23. keys()
# keys() returns all dictionary keys.
d1 = {
    "name": "CodeDesk",
    "course": "Python",
    "pincode": 302012
}

for i in d1.keys():
    print(i)

# ________________________________________________________________________________________________________________________________________

# 24. values()
# values() returns all dictionary values.
for i in d1.values():
    print(i)

# ________________________________________________________________________________________________________________________________________

# 25. items()
# items() returns both keys and values.
for i in d1.items():
    print(i)

# Output
# ('name', 'CodeDesk')
# ('course', 'Python')
# ('pincode', 302012)

# Practical Method
for key, value in d1.items():
    print(key, value)

# Output
# name CodeDesk
# course Python
# pincode 302012

# ___________________________________________________________________________________________________________________________

# 26. Nested Dictionary
# A dictionary inside another dictionary is called a nested dictionary.
# Example
info = {

    "car": {
        "name": "Tata",
        "model": "Safari"
    },

    "bike": {
        "name": "Yamaha",
        "model": "R15"
    }

}

print(info)

# Access Car Name
print(info["car"]["name"])
# Output:
# Tata

# Access Bike Model
print(info["bike"]["model"])
# Output:
# R15

# Structure
# info
# │
# ├── car
# │   ├── name  → Tata
# │   └── model → Safari
# │
# └── bike
#     ├── name  → Yamaha
#     └── model → R15


# ____________________________________________________________________________________________________________________________________________

# QUICK REVISION

# Concept	Use
# []	List
# {}	Dictionary
# list[index]	List element access
# list[start:end]	List slicing
# for	Iteration
# min()	Smallest value
# max()	Largest value
# del	Delete
# pop()	Remove by index
# remove()	Remove by value
# insert()	Add at specific index
# append()	Add one element
# extend()	Add multiple elements
# zip()	Process multiple iterables together
# split()	Break string into parts
# List comprehension	Create list concisely
# dict[key]	Access dictionary value
# keys()	Get keys
# values()	Get values
# items()	Get key-value pairs