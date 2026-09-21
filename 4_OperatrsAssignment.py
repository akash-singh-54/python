# Python Operators – Assignment

# ____________________________________________________________________________
# Logical Operators

num1 = 36
num2 = 56 
num3 = 56
# 1. Write a Python program to get a False output using the and and or operators.

print("(",num3 ,"==", num2,") and (",num1, ">", num2,") is true/false? \n", num3 == num2 and num1 > num2 )

print("(",num3 ,"!=", num2,") or (",num1, ">", num2,") is true/false? \n", num3 != num2 and num1 > num2 )

print("\n")

# 2. Write a Python program to get a True output using the not operator.

print("not of (",num3 ,"==", num2,") is true/false? \n", num3 == num2 )

print("\n")

# 3. Write a Python program to get a False output using the and operator.
# Use:
# xyz = 645
# pqr = 414

xyz = 645
pqr = 414

print("(",xyz ,"<=", pqr,") and (",xyz, "<", pqr,") is true/false? \n", xyz <= pqr and xyz < pqr )

print("\n")



# ___________________________________________________________________________
# Membership Operators
# 4. Write a Python program to check whether a space " " is present in the given string.
# s = "hello codedesk"

s = "hello codedesk"

print("Is space is pesent in string s? \n"," " in s)

print("\n")

# 5. Write a Python program to get a True output using the not in operator.
# xyz = "i am a python developer"

xyz = "i am a python developer"
print("Is python is present in string xyz? \n","python" in xyz)
print("\n")




# _____________________________________________________________________________________________
# Identity Operators

n1 = 10
n2 = 10
# 6. Write a Python program to get a False output using 'is not' operator.

print(n1,"is not",n2,"?\n", n1 is not n2)
print("\n")

# 7. Write a Python program to get a True output using 'is' identity operator.

print(n1,"is",n2,"?\n", n1 is n2)
print("\n")

# ____________________________________________________________________________

# Arithmetic Operators
# 8. Write a Python program to add an integer and a float value.

n1 = 40
f1 = 35.5

print("Sum of integer number", n1, "and float number", f1, "is equal to", n1+f1)
print("\n")

# 9. Write a Python program to concatenate (join) two string values using the + operator.

s1 = "Hello"
s2 = "World"
print(s1+s2)

print("\n")

# 10. Write a Python program to find the square and cube of 10.

print("square of 10 is", 10*2, "and cube of 10 is", 10*3)
print("\n")


# ____________________________________________________________________________
# Assignment Operators
# 11. Write a Python program using assignment operators to increment a variable's value.

var1 = 20
print("old value of variable is", var1)
var1 += 5
print("new value of the variable is ",var1)
print("\n")

# 12. Write a Python program using assignment operators to decrement a variable's value.

var2 = 40
print("old value of variable is", var2)
var2 -= 5
print("new value of the variable is ",var2)
print("\n")



# ____________________________________________________________________________
# Comparison Operators

num1 = 100
num2 =50
num3 =100
# 13. Write a Python program to get a False output using the less than or equal to (<=) operator.

print("Is (",num1 ,"<=", num2,") is true/false? \n", num1 <= num2 )
print("\n")

# 14. Write a Python program to get a True output using the greater than or equal to (>=) operator.

print("Is (",num1 ,">=", num2,") is true/false? \n", num1 >= num2 )

print("\n")

# 15. Write a Python program to get a False output using the not equal to (!=) operator.

print("Is (",num1 ,"!=", num3,") is true/false? \n", num1 != num3 )
print("\n")
