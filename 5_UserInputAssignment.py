# # 1. Write a program to print where the first two numbers will be added and the third number will be subtracted from the user input. 

print("expression => x + y - z")
x = eval(input("Type the value of x: "))
y = eval(input("Type the value of y: "))
z = eval(input("Type the value of z: "))
print("The result is: ", x+y-z)
print("\n")

# # 2. Write a program to get square and cube values from the user input. 

n1= int(input("Enter the value of which you need Squre or Cube "))
n2 = int(input("Enter 2 for square and 3 for cube"))
print(n1**n2)
print("\n")

# # 3. Write a program to create a floor division program from the user input. 

d1 = eval(input("Type the value of divident: "))
d2 = eval(input("Type the value of diviser: "))
print(d1//d2)
print("\n")

# # 4. Write a program to show the first number is an int second is a float, and the third is a string from the user input. 

n = int(input("Type the integer value: "))
f = float(input("Type the float value: "))
s = (input("Type the string: "))

print("first input is ", n ,"it is a", type(n))
print("second input is ", f ,"it is a", type(f))
print("third input is ", s ,"it is a", type(s))
print("\n")

# # 5. Write a program to perform or and not operators using user input. 

print("to check (num1 >num2 and num1 != num2)")

num1 = int(input("input number 1 = "))
num2 = int(input("input number 2 = "))

print (num1 >num2 and num1 != num2)

print("to check not(num1 >num2 or num1 != num2)")

num1 = int(input("input number 1 = "))
num2 = int(input("input number 2 = "))

print (not(num1 >num2 or num1 != num2))
print("\n")

# # 6. Write a program to get false output using <= operators using user input 

print("Expression:-  x <= y")
input1 = eval(input("Input value of x "))
input2 = eval(input("Input value of y "))
print("Answer is", input1 <= input2)
print("\n")

# # 7. Write a program to get true output using not(!) operators using user input 

print("Expression:-  not(x == y)")
input1 = eval(input("Input value of x "))
input2 = eval(input("Input value of y "))
print("Answer is", not(input1 == input2))
print("\n")

# # 8. Write a program to add first name and last name using user input 

first = (input("Type your first name: "))
last = (input("Type your last name: "))
print("user first name is", first,"and last name is",last)
print("\n")

# 9. Write a program to perform identity operators for values that are not equal using user input

print("To check x is y or not")
x = eval(input("Input value of x "))
y = eval(input("Input value of y "))
print("your answer is ", x is y)
print("\n")