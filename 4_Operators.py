# * Operators:-  It is a special symbols that perform a specific task. It is used to perform operations on variables and values.

# *Types of operators:- 

# 1. Arithmetic operators:- used to perform mathematical calculation.
# ## symbols:-  +,-,,/,%(modulus),*(exponents),//(floor division) example:-  

print(10+20)  #30  sum 
print(50-40)  #10  difference
print(10*5)   #50  multiplication
print(20/10)  #2   division
print(11%7)   #4  modulus used to get the remainder of the division
print(5**2)   #25 exponent used to get the power of the number
print(11//7)  #1 floor division used to get the quotient of the division


# _____________________________________________________________________________________________
#2. Assignment operators:- used to assign values and increment and decrement. 
# symbols:- =,+=,-=,*=,/= 

x=50
print(x)  #50 
x=50
x+=10
print(x)  #60 increment of 10
x=50
x-=10
print(x)  #40 decrement of 10
x=50
x*=10
print(x)  #500 multiplication by 10
x=50
x/=10
print(x)  #5 division by 10


# _____________________________________________________________________________________________
#3. Comparison operators: It is used to compare values. 
# symbols:-  ==, !=, <,>,<=,>=

x=100
y=100
print(x==y) #true
x=100
y=50
print(x!=y)  #true 
x=40
y=50
print(x<y)  #true 
x=50
y=40
print(x>y)  #true 
x=40
y=50
print(x<=y) #true 
x=60
y=50
print(x>=y)  #true 


# _____________________________________________________________________________________________
#4. Identity operators:- It is used to check if two variables refer to the same object. 
# #symbols:-   is, is not 

x=40
y=40
print(x is y) #true 
x=40
y=50
print(x is not y)  #true 


# _______________________________________________________________________________________________________________
#5. Membership operators:- It is used to check whether a value is present or not in the given variables. 
# symbols:-  in, not in 


s="welcome to codedesk"
print("to" in s)  #true 
s="welcome to codedesk"
print("too" not in s)  #true 

# _____________________________________________________________________________________________
#6. logical operators:- It is used to combine conditional statements. And, Or, Not are the logical operators. 
# symbols:- and, or, not 


#i. and:- It is True when both conditions are true. If either condition is false, the result is false.  
# example:- 

x=100
y=50
print(x>y and x!=y)  #true 
print(x==y and x!=y)  #false 

#ii. or:- It is True when at least one of the conditions is true. If both conditions are false, the result is false.  
# example:- 

x=50
y=100
print(x>y or x!=y)  #true 

#iii. not:- It is used to reverse the logical state of its operand. If a condition is true, then the not operator will make it false. If a condition is false, then the not operator will make it true. 

x=50
y=100
print(not(x!=y and x<y))  #false 


# _____________________________________________________________________________________________
#practical examples of operators:-

#arithmatic operators

# wap to find the sum of 10 and 20
print("sum of 10 and 20 is", 10+20 )

# wap to find the square of 9
print("square of 9 is", 9**2 )

#write a program to get the area of the circle
r = 5
pi = 3.14
area = pi*(r**2)
print("area of circle is", area)

# wap to get the floor division of 3 and 2
a = 3
b=2
c= a//b
print(c)

# wap to get the sum of three float numbers
f1 = 2.4
f2 = 3.5
f3 = 4.6
fs = f1 + f2 + f3
print("firrst float number is", f1, "second float number is", f2, "third float number is", f3, "sum of three float number is", fs)


#assignment operator

#wap to perform increament of 20 then decrement of 10 from the given number 

num1 =150
num1 += 20
num1 -= 10
print(num1)

#comparison operator

num1 = 50 
num2 = 70
num3 = 50
# wap to get false output using <
print("Is ", num2 ,"is < than ", num3,"=" ,num1<num3)

#wap to get the true output using >=
print("Is ", num3 ,"is >= to ", num1,"=" ,num3>=num1)

#wap to get the false output using !=
print("Is ", num1 ,"is != to ", num3,"=" ,num1!=num3)

#wap to get the true output using ==
print("Is ", num1 ,"is == to ", num3,"=" ,num1==num3)



#logical operators 

#wap to get the false output using 'or' operator
num1 = 70
num2 = 45
print(num1 < num2 or num1<= num2)

#wap to get the true output using 'not' operator
print(not(num1 < num2 or num1<= num2))


#membership operators

#wap to get the true output using 'in' operator
s1 = "welcome to the world of python"
print("Is python is present in s1?", "python" in s1)

#wap to get the false output using 'not in' operator
print("Is python is not present in s1?", "python" not in s1)

#identity operators

#wap to get the true output using 'is' operator
x = 10
y = 10
print("Is x is same object as y?", x is y)

#wap to get the false output using 'is not' operator
print("Is x is not same object as y?", x is not y)
