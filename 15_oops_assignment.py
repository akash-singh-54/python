# # Python OOP – 
# # 1. Student Class
# # Create a Student class with the following attributes:
# # •	name
# # •	age
# # •	course
# # Create an object and display all student details.

# class student():
#     name = "Akash Singh"
#     age = 24
#     course = "Python"

# object = student()
# print("Name is:",object.name)
# print("Age is:",object.age)
# print("Course is:",object.course)

# print("\n")

# # ___________________________________________________________________________________________________________________________________

# # 2. Employee Details
# # Create an Employee class with:
# # •	employee_id
# # •	name
# # •	position
# # •	department
# # Create an object and display the employee details.

# class employee():
#     def details(self):
#         emp_id = 2123
#         name = "Akash"
#         position = "Analyst"
#         department = "IT"
#         print("Employee id:",emp_id,"\nName is:",name,"\nPosition is:",position,"\nDepartment is:",department)

# object = employee()
# object.details()

# print("\n")


# # ___________________________________________________________________________________________________________________________________

# # 3. Calculator – Addition
# # Create a Calculator class with an add() method.
# # Pass two numbers to the method and print their sum.

# class calculator():
#     def ari(self,operation,num1,num2):
#         if(operation == "+"):
#             print(num1 + num2 )
#         elif(operation == "-"):
#             print(num1 - num2)
#         elif(operation == "*"):
#             print(num1 * num2)
#         elif(operation == "/"):
#             print(num1 / num2)
#         else:
#             print("wrong input")


# object = calculator()
# object.ari("+",3,4)

# print("\n")

# # ___________________________________________________________________________________________________________________________________

# # 4. Calculator – All Operations
# # Create a Calculator class with the following methods:
# # •	add()
# # •	subtract()
# # •	multiply()
# # •	divide()
# # Pass two numbers and perform all four operations.

# class calc():
#     def add(self,num1,num2):
#         print(num1,"+",num2,"=",num1+num2)
#     def substract(self,num1,num2):
#         print(num1,"-",num2,"=",num1-num2)
#     def multiply(self,num1,num2):
#         print(num1,"*",num2,"=",num1*num2)
#     def divide(self,num1,num2):
#         print(num1,"/",num2,"=",num1/num2)

# object = calc()
# object.add(5,6)
# object.divide(6,4)
# object.multiply(7,9)
# object.substract(9,5)

# print("\n")


# # ___________________________________________________________________________________________________________________________________

# # 5. Rectangle Area
# # Create a Rectangle class with an area() method.
# # Pass length and width to the method and calculate the area of the rectangle.

# class rectangle():
#     def area(self, l, b):
#         print("Area of the Rectangle: ", l*b)

# object = rectangle()
# object.area(5,7)

# print("\n")


# # ___________________________________________________________________________________________________________________________________

# # 6. Square Area
# # Create a Square class with an area() method.
# # Pass the side of the square and calculate its area.

# class square():
#     def ara(self,a):
#         print("Area of Square: ", a**2)

# object = square()
# object.ara(7)

# print("\n")

# # ___________________________________________________________________________________________________________________________________

# # 7. Student Result
# # Create a Student class with a result() method.
# # Pass marks of three subjects and calculate:
# # •	Total marks
# # •	Percentage

# class student():
#     def result(self, a,b,c):
#         print("Total marks: ", a+b+c)
#         print("Percentage: ", (a+b+c)/3 ,"%")

# object = student()
# object.result(66,78,59)

# print("\n")

# # ___________________________________________________________________________________________________________________________________

# # 8. Product Details
# # Create a Product class with:
# # •	product_name
# # •	price
# # •	quantity
# # Create an object and display all product details.

# class product():
#     def details(self):
#         product_name = "dell"
#         price = 50000
#         quantity = 5
#         print("Product name:", product_name,"\nPrice:",price,"\nQuantity:",quantity)

# object = product()
# object.details()

# print("\n")

# # ___________________________________________________________________________________________________________________________________

# # 9. Shopping Bill
# # Create a Shopping class with a calculate_bill() method.
# # Pass:
# # •	Product name
# # •	Price
# # •	Quantity
# # Calculate and display the total bill.


# print("\n")


# # ___________________________________________________________________________________________________________________________________

# # 10. Employee Salary
# # Create an Employee class with a calculate_salary() method.
# # Pass:
# # •	Basic salary
# # •	HRA
# # •	Bonus
# # Calculate and display the total salary.

# class employee():
#     def calculate_salary(self):
        
#         basic_salary = 68999
#         HRA = 5000
#         bonus = 4889
#         print("Total Salary:", basic_salary + HRA + bonus)      

# object = employee()
# object.calculate_salary()

# print("\n")

# # ___________________________________________________________________________________________________________________________________

# # 11. Bank Account
# # Create a BankAccount class with the following methods:
# # •	deposit()
# # •	withdraw()
# # •	display_balance()
# # Create an object and perform deposit and withdrawal operations.

# class bank_account():
    
#     def deposit(self,n, bal = 50555):
        
#         final = bal +n
#         print("Final balance: ", final)
    
#     def withdraw(self,n, bal = 50555):
        
#         if (n<= bal):
#             final = bal - n
#             print("Final balance: ", final)
#         else:
#             print("Insufficient balance")

#     def display_balance(self, bal = 50555):
        
#         final = bal
#         print("Final balance: ", final)

# object = bank_account()
# object.deposit(5000)
# object.withdraw(4000)
# object.display_balance()


# print("\n")

# # ___________________________________________________________________________________________________________________________________

# # 12. Mobile Details
# # Create a Mobile class with:
# # •	brand
# # •	model
# # •	price
# # •	storage
# # Create an object and display all mobile details.

# class mobile():
#     def details(self):
#         brand = "ROG"
#         model = "5VDF55X"
#         price = 59999
#         storage = "256 GB"
#         print("Product name:", brand,"\nPrice:",model,"\nQuantity:",price,"\nStorage:",storage)

# object = mobile()
# object.details()

# print("\n")

# # ___________________________________________________________________________________________________________________________________

# # 13. Discount Calculator
# # Create a Product class with a discount() method.
# # Pass the product price and calculate a 20% discount.
# # Display:
# # •	Original Price
# # •	Discount Amount
# # •	Final Price



# print("\n")

# # ___________________________________________________________________________________________________________________________________

# # 14. Electricity Bill
# # Create an Electricity class with a calculate_bill() method.
# # Pass the number of units consumed and calculate the electricity bill.
# # Use the following conditions:
# # •	Up to 100 units → ₹5 per unit
# # •	101–200 units → ₹7 per unit
# # •	Above 200 units → ₹10 per unit

# class electricity():
#     def bill(self,bill):
        
#         amount = 0
#         if (bill <=100):
#             amount = (bill)*5
#             print("Amount to be paid: ",amount)
#         elif (bill >= 101 and bill <= 200):
#             amount = (bill - 100)*7 + 100*5
#             print("Amount to be paid: ",amount)
#         else:
#             amount = (bill - 200)*10 + 100*5 +100*7
#             print("Amount to be paid: ",amount)
# object = electricity()
# object.bill(int(input("Insert unit: ")))

