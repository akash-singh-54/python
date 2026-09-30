# # # # Practical Practice Questions
# # # # 🟢 Level 1 — if Statement
# # # # 1.	Take two numbers from the user and check whether the first number is greater than the second number.

print("Is check x > y")
x = eval(input("Enter the value of x: "))
y = eval(input("Enter the value of y: "))
if(x>y):
    print("Yes X > Y")

print("\n")

# # # # 2.	Take a number from the user and check whether the number is positive.

print("To check the number is positive")
x = eval(input("Enter the value of x: "))
if(x>=0):
    print("Input number is positive")
print("\n")

# # # # 3.	Take a number from the user and check whether the number is greater than 100.


print("To check the number is grater than 100")
x = eval(input("Enter the value of x: "))
if(x>100):
    print("Input number is grater than 100")
print("\n")

# # # # 4.	Take a person's age and print "Eligible for Voting" if the age is 18 or above.

print("To check if the age of user is Eligible for Voting")
x = int(input("Enter the age of user: "))
if(x>=18):
    print("User is Eligible for Voting")

print("\n")

# # # # 5.	Take a student's marks and print "Pass" if marks are 40 or above.


print("To check if the student is pass")
x = eval(input("Enter the marks of student: "))
if(x>=40):
    print("Student is pass")

print("\n")

# # # # 6.	Take a number and check whether it is divisible by 5.

print("To check if number is divisible by 5")
x = eval(input("Enter the number: "))
if(x%5 == 0):
    print("The number is divisible by 5")

print("\n")

# # # # 7.	Take a number and check whether it is even.


print("To check if number is Even")
x = eval(input("Enter the number: "))
if(x%2 == 0):
    print("The number is Even")

print("\n")

# # # # 8.	Take a number and check whether it is greater than 50.


print("To check the number is grater than 50")
x = eval(input("Enter the value of x: "))
if(x>50):
    print("Input number is grater than 50")

print("\n")

# # # # 9.	Take the user's temperature and print "High Temperature" if it is greater than 35.


print("To check the user temperature is higher than 35")
x = eval(input("Enter the temperature of user: "))
if(x>35):
    print("High Temperature")

print("\n")

# # # # 10.	Take a person's salary and print "High Salary" if salary is greater than ₹50,000.


print("To check the user salary is higher than 50,000")
x = eval(input("Enter the salary of user: "))
if(x>50000):
    print("High Salary")

print("\n")

# # # #_____________________________________________________________________________________________________________________________________________________________
# # # #______________________________________________________________________________________________________________________________________________________________

# # # # 🟡 Level 2 — if-else Statement
# # # # 11.	Take a number and check whether it is even or odd.


print("To check if number is Even or Odd")
x = eval(input("Enter the number: "))
if(x%2 == 0):
    print("The number is Even")
else:
    print("The number is odd")

print("\n")

# # # # 12.	Take two numbers and print which number is greater.

print("Is check x > y or y > x")
x = eval(input("Enter the value of x: "))
y = eval(input("Enter the value of y: "))
if(x>y):
    print("X is Greater")
else:
    print("Y is Greater")

print("\n")

# # # # 13.	Take a number and check whether it is positive or negative.


print("To check the number is positive or negative")
x = eval(input("Enter the value of x: "))
if(x>=0):
    print("Input number is positive")
else:
    print("Input number is negative")

print("\n")

# # # # 14.	Take a student's marks and print:
# # # # •	"Pass" if marks are 40 or above
# # # # •	"Fail" otherwise


print("To check if the student is pass or fail")
x = eval(input("Enter the marks of student: "))
if(x>=40):
    print("Student is Pass")
else:
    print("Student is Fail")

print("\n")

# # # # 15.	Take age as input and check whether the person is eligible to vote or not.


print("To check if the age of user is Eligible for Voting or not")
x = int(input("Enter the age of user: "))
if(x>=18):
    print("User is Eligible for Voting")

else:
    print("User is Not Eligible for Voting")

print("\n")

# # # 16.	Take a number and check whether it is divisible by 3 or not.

print("To check if number is divisible by 3 or not")
x = eval(input("Enter the number: "))
if(x%3 == 0):
    print("The number is divisible by 3")
else:
    print("The number is not divisible by 3")

print("\n")

# # # # 17.	Take a number and check whether it is divisible by 5 or not.


print("To check if number is divisible by 5")
x = eval(input("Enter the number: "))
if(x%5 == 0):
    print("The number is divisible by 5")
else:
    print("The number is not divisible by 5")

print("\n")

# # # # 18.	Take a username and password and check:
# # # # username = "admin"
# # # # password = "12345"
# # # # Print "Login Successful" or "Invalid Login".

str1 = input("Enter the user name: ")
password = int(input("Enter your password: "))

if(str1 == "admin"):
    if(password == 12345):
        print("Login Successful")

else:
    print("Invalid Login")

print("\n")

# # # # 19.	Take the user's age and check:
# # # # •	Age ≥ 18 → "Adult"
# # # # •	Otherwise → "Minor"

print("To check if the age of user is Adult or not")
x = int(input("Enter the age of user: "))
if(x>=18):
    print("User is Adult")

else:
    print("User is Minor")



print("\n")

# # # # 20.	Take the purchase amount and check whether the customer gets free delivery.
# # # # •	Amount ≥ ₹500 → "Free Delivery"
# # # # •	Otherwise → "Delivery Charges Applicable"


print("To check whether the customer gets free delivery")
x = int(input("Enter the price: "))
if(x>=500):
    print("Free Delivery")

else:
    print("Delivery Charges Applicable")

print("\n")

# # #_________________________________________________________________________________________________________________
# # #_________________________________________________________________________________________________________________


# # # 🟠 Level 3 — if-elif-else Statement
# # # 21.	Take marks from the user and print the grade:
# # # 90–100  → A
# # # 75–89   → B
# # # 60–74   → C
# # # 40–59   → D
# # # Below 40 → Fail


marks = eval(input("Insert Student Percentage: "))
amount = 0
if (marks >= 90):
    print("This Student Got A Grade")
elif (marks >= 75):
    print("This Student Got B Grade")
    
elif (marks >= 60):
    print("This Student Got C Grade")

    
elif (marks >= 40):
    print("This Student Got D Grade")

else:
    print("This Student is Fail")


print("\n")

# # #-------------------------------------------------------------------------------------------
# # # 22.	Take a number and check whether it is:
# # # Positive
# # # Negative
# # # Zero

Num = eval(input("Enter any number: "))

if(Num > 0):
    print("Number is Positive")

elif(Num < 0):
    print("Number is Negative")

else:
    print("Number is Zero")

print("\n")

# # #-------------------------------------------------------------------------------------------
# # # 23.	Take a person's age and categorize them:
# # # 0–12   → Child
# # # 13–19  → Teenager
# # # 20–59  → Adult
# # # 60+    → Senior Citizen


age = int(input("Insert Your Age: "))

if (age >= 60):
    print("You Are a Senior Citizen")
elif (age >=20 ):
    print("You Are an Adult")
    
elif (age >= 13):
    print("You Are a Teenager")
    
else:
    print("You Are a Child")

print("\n")

# # #-------------------------------------------------------------------------------------------
# # # 24.	Create a simple calculator using if-elif-else.
# # # Input:
# # # •	First number
# # # •	Second number
# # # •	Operator (+, -, *, /)
# # # Example:
# # # Enter first number: 20
# # # Enter second number: 10
# # # Enter operator: +
# # # Output: 30


num1 = eval(input("Enter first number: "))

num2 = eval(input("Enter second number: "))

op = input("Enter operator (+ , -, *, /): ")

if (op == "+"):
    print(num1 + num2)

elif (op == "-"):
    print(num1 - num2)

elif(op == "*"):
    print(num1 * num2)

else:
    print(num1 / num2)

print("\n")

# # #-------------------------------------------------------------------------------------------
# # # 25.	Take a number from 1–7 and print the corresponding day:
# # # 1 → Monday
# # # 2 → Tuesday
# # # 3 → Wednesday
# # # 4 → Thursday
# # # 5 → Friday
# # # 6 → Saturday
# # # 7 → Sunday

num = int(input("Enter any number (1 to 7): "))


if (num == 1):
    print("Monday")

elif (num == 2):
    print("Tuesday")

elif(num == 3):
    print("Wednesday")

elif (num == 4):
    print("Thursday")

elif(num == 5):
    print("Friday")

elif (num == 6):
    print("Saturday")

elif(num == 7):
    print("Sunday")

else:
    print("Invalid Input")

print("\n")

# #-------------------------------------------------------------------------------------------
# # 26.	Take a number from 1–12 and print the corresponding month.

num = int(input("Enter any number (1 to 12): "))


if (num == 1):
    print("January")

elif (num == 2):
    print("February")

elif(num == 3):
    print("March")

elif (num == 4):
    print("April")

elif(num == 5):
    print("May")

elif (num == 6):
    print("June")

elif(num == 7):
    print("July")

elif (num == 8):
    print("August")

elif(num == 9):
    print("September")

elif (num == 10):
    print("October")

elif(num == 11):
    print("November")

elif (num == 12):
    print("December")

else:
    print("Invalid Input")

print("\n")

# #-------------------------------------------------------------------------------------------
# # 27.	Take a student's marks and print:
# # 90+       → Excellent
# # 75–89     → Very Good
# # 60–74     → Good
# # 40–59     → Average
# # Below 40  → Fail


marks = eval(input("Insert Student Percentage: "))

if (marks >= 90):
    print("This Student is Excellent")
elif (marks >= 75):
    print("This Student is Very Good")
    
elif (marks >= 60):
    print("This Student is Good")

    
elif (marks >= 40):
    print("This Student is Average")

else:
    print("This Student is Fail")


print("\n")


# #-------------------------------------------------------------------------------------------
# # 28.	Take the user's salary and categorize it:
# # Below ₹20,000       → Low Income
# # ₹20,000–₹50,000     → Middle Income
# # ₹50,001–₹1,00,000   → High Income
# # Above ₹1,00,000     → Premium Income


Salary = eval(input("Insert Salary: "))

if (Salary > 100000):
    print("Premium Income")
elif (Salary > 50000):
    print("High Income")
    
elif (Salary > 20000):
    print("Middle Income")

else:
    print("Low Income")


print("\n")



# #_________________________________________________________________________________________________________________
# #_________________________________________________________________________________________________________________

# # 🔴 Level 4 — Real-World Practical Questions
# # 29.	ATM Withdrawal
# # Take:
# # •	Account balance
# # •	Withdrawal amount
# # Check:
# # If amount ≤ balance → Withdrawal Successful
# # Otherwise           → Insufficient Balance

account_balance = eval(input("Insert Account Balance: "))
withdrawal_amount = eval(input("Insert Withdrawal Amount: "))

if (withdrawal_amount <= account_balance):
    print("Withdrawal Successful")
else:
    print("Insufficient Balance")

print("\n")

# #-------------------------------------------------------------------------------------------
# # 30.	Online Shopping Discount
# # Take the shopping amount:
# # ₹5000 or above  → 20% discount
# # ₹3000–4999      → 10% discount
# # ₹1000–2999      → 5% discount
# # Below ₹1000     → No discount
# # Print the final amount.

shopping_amount = eval(input("Insert Shopping Amount: "))

if (shopping_amount >= 5000):
    discount = shopping_amount * 0.2
elif (shopping_amount >= 3000):
    discount = shopping_amount * 0.1
elif (shopping_amount >= 1000):
    discount = shopping_amount * 0.05
else:
    discount = 0

final_amount = shopping_amount - discount
print("Final Amount: ", final_amount)

print("\n")

# #-------------------------------------------------------------------------------------------
# # 31.	Electricity Bill
# # Take electricity units and calculate:
# # 0–100 units      → ₹5/unit
# # 101–200 units    → ₹7/unit
# # 201–300 units    → ₹10/unit
# # Above 300 units  → ₹12/unit

bill = int(input("Insert unit: "))
amount = 0
if (bill <=100):
    amount = bill*5
    print("Your Bill is ", amount)
elif (bill >= 101 and bill <= 200):
    amount = (bill - 100)*7 + 100*5
    print("Your Bill is ", amount)
elif (bill >= 201 and bill <= 300):
    amount = (bill - 200)*10 + 100*7 + 100*5
    print("Your Bill is ", amount)
else:
    amount = (bill - 300)*12 + 100*7 + 100*10 + 100*5
    print("Your Bill is ", amount)


print("\n")

# #-------------------------------------------------------------------------------------------
# # 32.	Login System
# # Ask the user for:
# # Username
# # Password
# # Check whether both are correct.

username = input("Enter your username: ")
password = input("Enter your password: ")

if (username == "admin"):
    print("")
else:
    print("Invalid username")

if (password == "12345"):
    print("Login Successful")
else:
    print("Invalid password")

print("\n")

# # #-------------------------------------------------------------------------------------------
# # # 33.	Movie Ticket
# # # Take the user's age:
# # # Below 5   → Free
# # # 5–12      → ₹100
# # # 13–59     → ₹200
# # # 60+       → ₹120
# # # Print the ticket price.

age = int(input("Insert Your Age: "))
if (age < 5):
    print("Your Ticket is Free")
elif (age <= 12):
    print("Your Ticket Price is ₹100")
elif (age <= 59):
    print("Your Ticket Price is ₹200")
else:
    print("Your Ticket Price is ₹120")
print("\n")

# # #-------------------------------------------------------------------------------------------
# # # 34.	College Admission
# # # Take the student's percentage:
# # # 90+       → Computer Science
# # # 80–89     → Data Science
# # # 70–79     → Web Development
# # # 60–69     → Digital Marketing
# # # Below 60  → Not Eligible

marks = eval(input("Insert Student Percentage: "))

if (marks >= 90):
    print("Admission to Computer Science")
elif (marks >= 80):
    print("Admission to Data Science")
elif (marks >= 70):
    print("Admission to Web Development")
elif (marks >= 60):
    print("Admission to Digital Marketing")
else:
    print("Not Eligible")

print("\n")

# # #-------------------------------------------------------------------------------------------
# # # 35.	BMI Category
# # # Take weight and height and calculate BMI:
# # # BMI < 18.5       → Underweight
# # # 18.5–24.9        → Normal
# # # 25–29.9          → Overweight
# # # 30+              → Obese

weight = eval(input("Enter your weight in kg: "))
height = eval(input("Enter your height in meters: "))
BMI = weight / (height ** 2)
print("Your BMI is: ", BMI)
if (BMI < 18.5):
    print("Underweight")
elif (BMI < 25):
    print("Normal")
elif (BMI < 30):
    print("Overweight")
else:
    print("Obese")
print("\n")

# #-------------------------------------------------------------------------------------------
# # 36.	ATM Menu
# # Display:
# # 1. Check Balance
# # 2. Withdraw
# # 3. Deposit
# # Ask the user to select an option and perform the appropriate operation using if-elif-else.

Menue = int(input("Select an option:\n1. Check Balance\n2. Withdraw\n3. Deposit\n Enter your choice: "))
balance = 1000000
if (Menue == 1):
    print("Your Balance is: ", balance)
elif (Menue == 2):
    withdraw = eval(input("Enter the amount to withdraw: "))
    if (withdraw <= balance):
        balance -= withdraw
        print("Withdrawal Successful. New Balance: ", balance)
    else:
        print("Insufficient Balance") 
elif (Menue == 3):
    deposit = eval(input("Enter the amount to deposit: "))
    balance += deposit
    print("Deposit Successful. New Balance: ", balance)

else:
    print("Invalid Option")
