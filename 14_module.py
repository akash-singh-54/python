# * Module: a collection of functions is called a module and is used to move data from one file to another. 

# Syntax: import 

# * Types of modules:-

# 1. user-defined 
# 2. predefined 

# * user-defined:- In this method, the user can create a module according to their own needs. 

# *Steps to create a user-defined module:-
# - First, create a file of code 
# -Second, import the code file name into the second file. 

# example:- 
# Write a program to add three numbers from the 	user using the module:-
# 1. file1.py
 
#    def display():
#        num1=eval(input("enter the number 1:- ")) 
#        num2=eval(input("enter the number 2:- "))
#        num3=eval(input("enter the number 3:- ")) 
#        print(num1+num2+num3)


# def add(num1 , num2):
#     return(num1 + num2)


# def multi(num3 , num4):
#     return(num3 * num4)

# # useinput :- 

# def display():
#     name = input("enter the name ")

#     print(name)

# # using module perform logical operators :- 


# def logical(num1 , num2):
#     return(num1 > num2  and num1 != num2)


# #using module get square and cube `
# # 

# def check(num1):
#     return("square is ", num1 ** 2 , "cube is ",  num1**3)



# 2.file2.py

# import file1
# add.display()  

# print(file1.add(10,6))

# print(file1.add(8,9))

# print(file1.multi(4,6))

# file1.display()
# print(file1.logical(20,6))

# print(file1.check(15))

