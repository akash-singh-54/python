# PYTHON FOR LOOP
# Q1. Print numbers from 0 to 10 using a for loop.

for i in range(11):
    print(i)
print("\n")

#----------------------------------------------------------------------------------------------------------------
# Q2. Print numbers from 1 to 20 using a for loop.


for i in range(1,21):
    print(i) 
print("\n")

#----------------------------------------------------------------------------------------------------------------
# Q3. Print reverse counting from 20 to 1 using a for loop.


for i in range(20,0,-1):
    print(i)
print("\n")

#----------------------------------------------------------------------------------------------------------------
# Q4. Print numbers from 1 to 50 using a for loop.


for i in range(1,51):
    print(i)
print("\n")

#----------------------------------------------------------------------------------------------------------------
# Q5. Print even numbers from 1 to 100 using a for loop.


for i in range(1, 101):
    if (i%2 == 0):
        print(i)
print("\n")

#----------------------------------------------------------------------------------------------------------------
# Q6. Print odd numbers from 1 to 100 using a for loop.


for i in range(1, 101):
    if (i%2 != 0):
        print(i)
print("\n")

#----------------------------------------------------------------------------------------------------------------
# Q7. Print numbers from 10 to 100 with a gap of 10.


for i in range(10,101,10):
    print(i)
print("\n")

#----------------------------------------------------------------------------------------------------------------
# Q8. Print numbers from 100 to 0 with a decrement of 10.


for i in range(100,-1,-10):
    print(i)
print("\n")

#----------------------------------------------------------------------------------------------------------------

# Q9. Print the sequence: 1, 3, 5, 7 ... 19.


for i in range(1, 21):
    if (i%2 != 0):
        print(i)
print("\n")

#----------------------------------------------------------------------------------------------------------------
# Q10. Print the sequence: 2, 4, 6, 8 ... 20.


for i in range(1, 21):
    if (i%2 == 0):
        print(i)
print("\n")

#----------------------------------------------------------------------------------------------------------------
# Q11. Print the sequence: 5, 10, 15 ... 50.


for i in range(1,11):
    print(i*5)
print("\n")

#----------------------------------------------------------------------------------------------------------------
# Q12. Print the sequence: 100, 90, 80 ... 10.


for i in range(100,1,-10):
    print(i)
print("\n")

#----------------------------------------------------------------------------------------------------------------
# Q13. Print the sequence: 50, 45, 40 ... 5.


for i in range(10,0,-1):
    print(i*5)
print("\n")

#----------------------------------------------------------------------------------------------------------------

# Q14. Print the multiplication table of 2 using a for loop.


for i in range(1,11):
    print(i*2)
print("\n")

#----------------------------------------------------------------------------------------------------------------
# Q15. Take a number as input from the user and print its multiplication table from 1 to 10.

num = int(input("Enter The Number For Multiplication Table: "))
for i in range(1,11):
    print(i*num)
print("\n")

#----------------------------------------------------------------------------------------------------------------
# Q16. Take a number as input from the user and print its multiplication table from 1 to 20.


num = int(input("Enter The Number For Multiplication Table: "))
for i in range(1,21):
    print(i*num)
print("\n")

#----------------------------------------------------------------------------------------------------------------
# Q17. Print the multiplication tables from 2 to 5.

for j in range(2,7):
    print("The Table of", j,"is: ")
    for i in range(1,11):
        print(i*j)
print("\n")

#----------------------------------------------------------------------------------------------------------------

# Q18. Calculate the sum of numbers from 1 to 10.
count = 0
for i in range(1,11):
    count += i

print (count)

print("\n")

#----------------------------------------------------------------------------------------------------------------
# Q19. Calculate the sum of numbers from 1 to 100.

count = 0
for i in range(1,101):
    count += i

print (count)
print("\n")

#----------------------------------------------------------------------------------------------------------------
# Q20. Calculate the sum of even numbers from 1 to 50.

count = 0
for i in range(1,51):
    if (i%2 == 0):
        count += i
print(count)
print("\n")

#----------------------------------------------------------------------------------------------------------------
# Q21. Calculate the sum of odd numbers from 1 to 50.

count = 0
for i in range(1,51):
    if (i%2 != 0):
        count += i
print(count)
print("\n")

#----------------------------------------------------------------------------------------------------------------
# Q22. Print the squares of numbers from 1 to 10.
# Example:
# 1
# 4
# 9
# 16
# 25
# ...
# 100

for i in range(1,11):
    print("Square of", i, "is", i**2)
print("\n")

#----------------------------------------------------------------------------------------------------------------
# Q23. Print the cubes of numbers from 1 to 10.

for i in range(1,11):
    print("Cube of", i, "is", i**3)
print("\n")

#----------------------------------------------------------------------------------------------------------------
# Q24. Take a number as input from the user and calculate its factorial.
# Example:
# Enter number: 5
# Factorial = 120

int = int(input("Enter The Number For Factorial: "))
fact = 1
for i in range(1,int+1):
    fact *= i

print("Factorial of", int, "is", fact)
print("\n")

# ________________________________________
# 🔴 PRACTICAL LEVEL
# Q25. Take 'n' as input from the user and print numbers from 1 to n.
# Example:
# Enter n: 10

# 1
# 2
# 3
# ...
# 10

n = int(input("Enter The Number: "))
for i in range(1,n+1):
    print(i)
print("\n")

#----------------------------------------------------------------------------------------------------------------
# Q26. Take 'n' as input from the user and print reverse counting from n to 1.
# Example:
# Enter n: 10

# 10
# 9
# 8
# ...
# # 1

n = int(input("Enter The Number: "))
for i in range(n,0,-1):
    print(i)
print("\n")

#----------------------------------------------------------------------------------------------------------------
# Q27. Take a number as input from the user and print its factors.
# Example:
# Enter number: 12

# 1
# 2
# 3
# 4
# 6
# 12

n = int(input("Enter The Number: "))
print("Factors of", n, "are: ") 
for i in range(1,n+1):
    if (n%i == 0):
        print(i)
print("\n")

#----------------------------------------------------------------------------------------------------------------
# Q28. Print only the multiples of 3 from 1 to 100.
# Example:
# 3
# 6
# 9
# 12
# ...
# 99

for i in range(1,101):
    if (i%3 == 0):
        print(i)
print("\n")

#----------------------------------------------------------------------------------------------------------------
# Q29. Take start and end numbers as input from the user and calculate the sum of even numbers in that range.
# Example:
# Start: 1
# End: 10

# Even Sum = 30

s = int(input("Enter The Start Number: "))
e = int(input("Enter The End Number: "))
even_sum = 0
for i in range(s,e+1):
    if (i%2 == 0):
        even_sum += i
print("Even Sum =", even_sum)
print("\n")

#----------------------------------------------------------------------------------------------------------------
# Q30. Take a number as input from the user and print its multiplication table from 1 to 10 in the following format.
# Example:
# Enter number: 5

# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50

num = int(input("Enter The Number For Multiplication Table: "))
for i in range(1,11):
    print(num, "x", i, "=", num*i)

 