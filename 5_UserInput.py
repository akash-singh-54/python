# * user input and type casting:-  
# * user input:- It is a process to ask for the values at run time. 

# syntax:-  input 

# note:- By default, input works as a string. 
# example:-  

x=input("enter the value")
print(x)


# * type casting:- 
# int()
# float()
# eval()

# 1. int():-  use for integer values. 
# example:- 

x=int(input("enter the number1:- "))
y=int(input("enter the number2:-"))

print(x+y)

# 2. float():- use for decimal values. 

x=float(input("enter the number1:- "))
y=float(input("enter the number2:-"))

print(x+y)

# 3. eval():- use for both integer values and float values. 
# example:- 

x=eval(input("enter the number1:- "))
y=eval(input("enter the number2:-"))

print(x+y)


#________________________________________________________________________________________________________________
#________________________________________________________________________________________________________________


#wap to add two integer and two float numbers from the use input

n1 = int(input("Insert integer 1 ="))
n2 = int(input("Insert integer 2 = "))
f1 = float(input("Insert float number = "))
print ("Sum of two integer is ", n1+n2+f1)

#by user input get the square and cube of 7

num = int(input("Enter 2 for square of 7 and 3 for cube of 7 = "))
print(7**num)

name = input("Your name: ")
surname = input("Your surname: ")
print("User name is", name,"and surname is", surname)


#wap to perform logical operator using user input

print("to check (num1 >num2 and num1 != num2)")

num1 = int(input("input number 1 = "))
num2 = int(input("input number 2 = "))

print (num1 >num2 and num1 != num2)