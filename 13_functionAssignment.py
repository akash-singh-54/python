# # Part 1: Basic Functions & Output
# # Q1. Display Name: Write a Python function that prints your name to the console.

# def name():
#     name = "Akash Singh"
#     print("Name is: ", name)

# name()

# print("\n")

# #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Q2. Welcome Message: Write a Python function that prints the message "Welcome to Python Programming".

# def welcome():
#     print("Welcome to Python Programming")

# welcome()

# print("\n")

# #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Q3. Display Course: Write a Python function that displays the course name, institute name, and city.

# def student():
#     institute_name = input("Enter Institute name: ")
#     course = input("Enter course: ")
#     city = input("Enter city: ")
    

#     print("Institute Name is: ", institute_name, "\nLearnung: ", course, "\nCity is: ", city)

# student()

# print("\n")

# #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Q4. Print 1 to 10: Write a Python function using a loop to print numbers from 1 to 10.

# def num():
#     n =1
#     while(n<=10):
#         print(n)
#         n += 1

# num()

# print("\n")

# #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Q5. Print Even Numbers: Write a Python function to print all even numbers from 1 to 20.

# def num():
#     n =1
#     while(n<=20):
#         if(n%2 == 0):
#             print(n)
#         n += 1

# num()

# print("\n")

# #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Q6. Print Odd Numbers: Write a Python function to print all odd numbers from 1 to 20.

# def num():
#     n =1
#     while(n<=20):
#         if(n%2 != 0):
#             print(n)
#         n += 1

# num()

# print("\n")

# #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Q7. Table of a Number: Write a Python function that accepts a number as a parameter and prints its multiplication table.

# def table():
#     n = int (input("Number: "))
#     for i in range(1,11):
#         print(n,"*",i,"=", n*i)

# table()

# print("\n")

# #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Q8. Sum of Three Numbers: Write a Python function that calculates and prints the sum of three predefined numbers.

# def sum():
#     a= 2
#     b=5
#     c=9
#     print("sum of three number is: ",a,"+",b,"+",c,"=", a+b+c)

# sum()
# print("\n")

# #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Part 2: Functions with Parameters
# # Q9. Add Two Numbers: Write a function named add(a, b) that takes two parameters, calculates their sum, and prints the result.

# def sum(a,b):
#     print("sum of three number is: ",a,"+",b,"=", a+b)

# sum(7,8)
# sum(8,9)

# print("\n")

# #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Q10. Square & Cube: Write a function named square_cube(num) that calculates and prints both the square and the cube of a given number.

# def exp(num):
#     square = num**2
#     cube = num**3
#     print("square of the number is ", square, " and cube of the number is ", cube)

# exp(4)
# exp(8)

# print("\n")

# #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Q11. Student Information: Write a function named student_info(name, course, city) that accepts these three values as parameters and displays the student's details.


# def student(name, course, city):

#     print("Student Name is: ", name, "\nLearnung: ", course, "\nBelongs to: ", city )

# student("Akash", "btech", "ksp")

# print("\n")

# #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Q12. Employee Information: Write a Python function that accepts an employee's name, salary, and department as parameters and displays them.


# def emp(name, salary, department):

#     print("Employee Name is: ", name, "\nSalary: ", salary, "\nDepartment: ", department )

# emp("Akash", 2637873, "Data Analytics")

# print("\n")

# #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Q13. Greater Number: Write a Python function that takes two numbers as parameters and finds/prints the greater of the two.

# def greater(n1, n2):
#     if (n1>n2):
#         print(n1,"is greater")
#     else:
#         print(n2,"is greater")

# greater(5,7)
# greater(8,3)

# print("\n")

# #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Q14. Even or Odd: Write a Python function that takes a number as a parameter and checks whether it is even or odd.

# def e_o(n):
#     if (n%2==0):
#         print(n, "is even")
#     else:
#         print(n, "is odd")

# e_o(6)
# e_o(7)
# print("\n")

# #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Q15. Positive, Negative, or Zero: Write a Python function that checks whether a given number parameter is positive, negative, or zero.

# def p_n_0(n):
#     if (n>0):
#         print(n, "is positive")
#     elif(n<0):
#         print(n, "is negative")
#     else:
#         print(n, "is zero")

# p_n_0(8)
# p_n_0(-4)
# p_n_0(0)

# print("\n")

# #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Q16. Calculate Percentage: Write a Python function that takes the marks of 5 subjects as parameters, calculates the total percentage, and displays it.

# def percent(s1,s2,s3,s4,s5):
#     sum = s1+s2+s3+s4+s5
#     print("Percentage is: ", sum/5,"%") #max marks 100 per subject

# percent(45,66,67,54,89)
# percent(99,78,89,89,88)
# print("\n")

# #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Part 3: Advanced Logic & Loops with Parameters
# # Q17. Sum from 1 to N: Write a Python function that accepts an integer parameter n and calculates the sum of all numbers from 1 to n.

# def sum(n):
#     i = 1
#     s = 0
#     while(i<=n):
#         s = i + s
#         i += 1
#     print("sum =", s) 

# sum(int(input("Enter nth term: ")))
# print("\n")

# #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Q18. Factorial: Write a Python function that accepts a number and calculates its factorial.

# def fac(n):
#     i = 1
#     s = 1
#     while(i<=n):
#         s = i *s
#         i += 1
#     print("factorial =", s) 

# fac(int(input("Enter factorial term: ")))

# print("\n")

# #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Q19. Count Digits: Write a Python function that takes an integer and counts the total number of digits it contains.

# def count(n):
#     print("Total charachter = ", len(n))

# count(input("Enter the number: "))


# print("\n")

# #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Q20. Reverse Number: Write a Python function that takes a number and returns or prints its reverse.

# def count(arr):
#     print("Total charachter = ", arr[::-1])

# count(input("Enter the number: "))

# print("\n")

# #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Q21. Palindrome Number: Write a Python function to check whether a given number is a palindrome (reads the same forwards and backwards).


# def count(arr):
#     if(arr == arr[::-1]):
#         print("It is palindrome")
#     else:
#         print("It is not palindrome")

# count(input("Enter the number to check palindrome: "))

# print("\n")

# #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Q22. Prime Number: Write a Python function that checks whether a given number is a prime number.

# def prime(num):
#     if num > 1:
#         is_prime = True
#         i = 2
#         while i < num :
#             if num % i == 0:
#                 is_prime = False  
#                 break
#             i += 1
#         if is_prime:
#             print("Prime Number")
#         else:
#             print("Not a Prime Number")
#     else:
#         print("Not a Prime Number")

# prime(int(input("Enter the number to check prime: ")))

# print("\n")

# #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Q23. Prime Numbers in a Range: Write a Python function that takes a range (start and end) as parameters and prints all prime numbers within that range.

def print_prime(start, end):
    for num in range(start, end + 1):
        # Prime numbers are strictly greater than 1
        if num > 1:
        
            for i in range(2, int(num**0.5) + 1):
                if (num % i) == 0:
                    break
            else:
                # The else block executes if the loop completes without hitting a 'break'
                print(num)

print_prime(1, 30)

                
# print("\n")

# #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Q24. Maximum of Three Numbers: Write a Python function that accepts three numbers as parameters and returns or prints the maximum among them.

# def great(a,b,c):
#     if (a>b and a>c):
#         print(a,"is greatest number")
#     elif (c>b and c>a):
#         print(c,"is greatest number")
#     else:
#         print(b,"is greatest number")

# great(5,7,8)
# great(9,4,7)

# print("\n")

# #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Part 4: Return Values in Functions
# # Q25. Return Addition: Write a function named add(a, b) that takes two numbers as parameters, computes their sum, and returns the result using the return statement.

# def sum(a,b):
#     s = a+b
#     return(s)
# print(sum(4,5))

# print("\n")

# #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Q26. Return Square: Write a Python function that takes a number, calculates its square, and returns the squared value.

# def square(a):
#     s = a**2
#     return(s)
# print(square(4))

# print("\n")

# #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # Q27. Return Even/Odd: Write a Python function that takes a number as a parameter and returns a string indicating whether the number is "Even" or "Odd".


# def even(n):
#     if (n%2==0):
#         return(print(n, "is even"))
#     else:
#         return(print(n, "is odd"))

# print(even(5))
# print(even(4))
