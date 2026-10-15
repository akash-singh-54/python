 # #---------------------------------
# # While Loop — Practice Questions
# #---------------------------------
# #---------------------------------

# # 1. Print Numbers from 1 to 10
# # Use a while loop to print the numbers from 1 to 10.

# num = 1
# while(num <= 10):
#     print(num)
#     num += 1

# print("\n")

# # ⸻-------------------------------------------------------------------------------------------------

# # 2. Print Numbers from 10 to 1
# # Use a while loop to print the numbers from 10 to 1 in reverse order.


# num = 10
# while(num >= 1):
#     print(num)
#     num -= 1

# print("\n")

# # ⸻-----------------------------------------------------------------------------------------------------------

# # 3. Print Numbers from 1 to 50
# # Use a while loop to print the numbers from 1 to 50.


# num = 1
# while(num <= 50):
#     print(num)
#     num += 1

# print("\n")

# #--------------------------------------------------------------------------------------------------------------

# # 4. Print Numbers from 50 to 1
# # Use a while loop to print the numbers from 50 to 1 in reverse order.


# num = 50
# while(num >= 1):
#     print(num)
#     num -= 1

# print("\n")

# #--------------------------------------------------------------------------------------------------------------

# # 5. Print Even Numbers from 1 to 100
# # Use a while loop to print all even numbers from 1 to 100.


# num = 1
# while(num <= 100):
#     if(num%2 == 0):
#         print(num)
#     num += 1

# print("\n")

# #--------------------------------------------------------------------------------------------------------------

# # 6. Print Odd Numbers from 1 to 100
# # Use a while loop to print all odd numbers from 1 to 100.


# num = 1
# while(num <= 100):
#     if(num%2 != 0):
#         print(num)
#     num += 1

# print("\n")

# #--------------------------------------------------------------------------------------------------------------

# # 7. Print Multiples of 5 from 1 to 100
# # Use a while loop to print all multiples of 5 from 1 to 100.
# # Example:
# # 5 10 15 20 25 ... 100


# num = 1
# while(num <= 100):
#     if(num%5 == 0):
#         print(num)
#     num += 1

# print("\n")

# # -------------------------------------------------------------------------------------------------------------

# # 8. Print the Multiplication Table of a User-Entered Number
# # Take a number as input from the user and use a while loop to print its multiplication table from 1 to 10.
# # Example:
# # Input: 5
# # 5
# # 10
# # 15
# # 20
# # 25
# # 30
# # 35
# # 40
# # 45
# # 50

# x= int(input("Enter the number to get the multiplication table: "))
# num = 1
# while(num <= 10):
#     print(num*x)
#     num += 1

# print("\n")

# # -------------------------------------------------------------------------------------------------------------

# # 9. Calculate the Sum from 1 to 10
# # Use a while loop to calculate the sum of numbers from 1 to 10.
# # Expected Output:
# # Sum = 55

# num = 1
# sum = 0
# while(num <= 10):
#     sum += num
#     num += 1
# print(sum)
# print("\n")


# # -------------------------------------------------------------------------------------------------------------

# # 10. Calculate the Sum from 1 to 100
# # Use a while loop to calculate the total sum of numbers from 1 to 100.


# num = 1
# sum = 0
# while(num <= 100):
#     sum += num
#     num += 1
# print(sum)
# print("\n")

# # ---------------------------------------------------------------------------------------------------------------------

# # 11. Calculate the Sum of Even Numbers
# # Calculate the sum of all even numbers from 1 to 50 using a while loop.


# num = 1
# sum = 0
# while(num <= 50):
#     if(num%2 == 0):
#         sum += num
#     num += 1
# print(sum)
# print("\n")

# # ---------------------------------------------------------------------------------------------------------------------

# # 12. Calculate the Sum of Odd Numbers
# # Calculate the sum of all odd numbers from 1 to 50 using a while loop.


# num = 1
# sum = 0
# while(num <= 50):
#     if(num%2 != 0):
#         sum += num
#     num += 1
# print(sum)
# print("\n")

# # ---------------------------------------------------------------------------------------------------------------------

# # 13. Calculate the Sum from 1 to n
# # Take n as input from the user and calculate the sum of numbers from 1 to n using a while loop.
# # Example:
# # Input: 10
# # Output: 55



# x= int(input("Enter the Last number to get the sum: "))
# num = 1
# sum = 0
# while(num <= x):
#     sum += num
#     num += 1
# print(sum)
# print("\n")


# # ---------------------------------------------------------------------------------------------------------------------

# # 14. Count Even Numbers
# # Use a while loop to count how many even numbers there are from 1 to 100.

# num = 1
# sum = 0
# while(num <= 100):
#     if(num%2 == 0):
#         sum += 1
#     num += 1
# print(sum)
# print("\n")

# # ---------------------------------------------------------------------------------------------------------------------

# # 15. Count Odd Numbers
# # Use a while loop to count how many odd numbers there are from 1 to 100.

# num = 1
# sum = 0
# while(num <= 100):
#     if(num%2 != 0):
#         sum += 1
#     num += 1
# print(sum)
# print("\n")

# # --------------------------------------------------------------------------------------------------------------------------

# # 16. Count the Number of Digits
# # Take a number as input from the user and count the total number of digits in it using a while loop.
# # Example:
# # Input: 12345
# # Output: 5 digits

    

# # --------------------------------------------------------------------------------------------------------------------------

# # 17. Calculate the Sum of Digits
# # Take a number as input from the user and calculate the sum of all its digits.
# # Example:
# # Input: 1234
# # Output: 10

# # --------------------------------------------------------------------------------------------------------------------------

# # 18. Reverse a Number
# # Take a number as input from the user and use a while loop to reverse the number.
# # Example:
# # Input: 12345
# # Output: 54321

# # --------------------------------------------------------------------------------------------------------------------------

# # 19. Check Whether a Number Is a Palindrome
# # Take a number as input from the user and check whether it is a palindrome.
# # Example 1:
# # Input: 121
# # Output: Palindrome
# # Example 2:
# # Input: 123
# # Output: Not Palindrome

    


# # --------------------------------------------------------------------------------------------------------------------------

# # 20. Check Whether a Number Is Prime
# # Take a number as input from the user and use a while loop to check whether it is a prime number.
# # Example:
# # Input: 7
# # Output: Prime Number

# # ---------------------------------------------------------------------------------------------------------------------------

# # 21. Calculate the Sum Until the User Enters 0
# # Continuously take numbers as input from the user.
# # When the user enters 0:
# # * Stop taking input.
# # * Calculate and print the sum of all the numbers entered before 0.
# # Example:
# # Input:
# # 10
# # 20
# # 30
# # 0
# # Output:
# # Total = 60

sum =0
n = int(input("Enter The Numbers To get sum to see result Enter 0\n: "))

while (n != 0):
    sum += n
    n = int(input())
print("Sum of Numbers  =",sum)

print("\n")

# # ---------------------------------------------------------------------------------------------------------------------------

# # 22. Count Positive and Negative Numbers
# # Continuously take numbers as input from the user.
# # The program should stop when the user enters 0.
# # Count and display:
# # * Total number of positive numbers
# # * Total number of negative numbers
# # Example:
# # Input:
# # 10
# # -5
# # 20
# # -8
# # 0
# # Positive = 2
# # Negative = 2

pos = 0
neg = 0
n = int(input("Enter The Numbers To count Positive and Negative Numbers to see result Enter 0\n: "))

while (n != 0):
    if (n>0):
        pos+=1
    elif(n<0):
        neg+=1
    n = int(input())
print("Total Positive Numbers  =",pos,"\nTotal Negative Numbers =", neg)

print("\n")


# # ---------------------------------------------------------------------------------------------------------------------------

# # 23. Password Verification System
# # Set a password in the program.
# # Ask the user to enter the password.
# # Continue asking the user to enter the password until the correct password is entered.
# # When the correct password is entered, print:
# # Login Successful

password = input ("Enter the password: ")

while (password != "12345"):
    password = input ("Enter the password: ")

print("Login Successful")