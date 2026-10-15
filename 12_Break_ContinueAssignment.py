# # Python `break` and `continue` Practice Questions
# | **1**  | **Stop at 6**                          
# | Write a program to print numbers from **1 to 10**. Use the `break` statement to stop the loop when the number **6** is reached.                                                                                                                                                                                             
# | **Output:** `1, 2, 3, 4, 5`  

n=1
while (n <= 10):
    if n == 6:
        break
    print(n)
    n += 1                                            
print("\n")

# | **2**  | **Stop at 10**                         
# | Write a program to print numbers from **1 to 20**. Use the `break` statement to stop the loop when the number **10** is reached.                                                                                                                                                                                            
# | The loop should stop when it reaches **10**.                             

n=1
while (n <= 20):
    if n == 10:
        break
    print(n)
    n += 1
print("\n")

# | **3**  | **Even Numbers with Break**            
# | Write a program to print even numbers from **1 to 50**. Use the `break` statement to stop the loop when the number **20** is reached.                                                                                                                                                                                       
# | **Output:** `2, 4, 6, 8, 10, 12, 14, 16, 18`                             

n=1
while (n <= 50):
    if n % 2 == 0:
        if n == 20:
            break
        print(n)
    n += 1
print("\n")

# | **4**  | **Multiplication Table with Break**    
# | Write a program that takes a number as input and prints its multiplication table. Use the `break` statement to stop the loop after printing the **5th value**.                                                                                                                                                              
# | **Input:** `5` → **Output:** `5, 10, 15, 20, 25`                         

n = int(input("Enter a number for multiplication table: "))
for i in range(1, 11):
    if i > 5:
        break
    print(n * i)

# | **5**  | **Input Until Zero**                   
# | Write a program that continuously accepts numbers from the user. Use the `break` statement to stop the program when the user enters **0**.                                                                                                                                                                                  
# | **Input:** `10, 20, 30, 0` → **Output:** `Program Stopped`               

n=int(input("Enter a number (0 to stop): "))
while (n != 0):
    n=int(input("Enter a number (0 to stop): "))
print("Program Stopped")
print("\n")

# | **6**  | **Skip 5**                             
# | Write a program to print numbers from **1 to 10**. Use the `continue` statement to skip the number **5**.                                                                                                                                                                                                                   
# | **Output:** `1, 2, 3, 4, 6, 7, 8, 9, 10`                                 

for i in range(1, 11):
    if i == 5:
        continue
    print(i)

print("\n")

# | **7**  | **Skip Even Numbers**                  
# | Write a program to print numbers from **1 to 20**. Use the `continue` statement to skip all **even numbers**.                                                                                                                                                                                                               
# | **Output:** `1, 3, 5, 7, 9, 11, 13, 15, 17, 19`                          

for i in range(1, 21):
    if i % 2 == 0:
        continue
    print(i)
print("\n")

# | **8**  | **Skip Odd Numbers**                   
# | Write a program to print numbers from **1 to 20**. Use the `continue` statement to skip all **odd numbers**.                                                                                                                                                                                                                
# | **Output:** `2, 4, 6, 8, 10, 12, 14, 16, 18, 20`                         

for i in range(1, 21):
    if i % 2 != 0:
        continue
    print(i)
print("\n")

# | **9**  | **Skip Multiples of 5**                
# | Write a program to print numbers from **1 to 50**. Use the `continue` statement to skip all numbers that are **divisible by 5**.                                                                                                                                                                                            
# | Numbers divisible by 5 should not be printed.                            

for i in range(1, 51):
    if i % 5 == 0:
        continue
    print(i)
print("\n")

# | **10** | **Skip Specific Numbers**              
# | Write a program to print numbers from **1 to 20**. Use the `continue` statement to skip the numbers **5, 10, and 15**.                                                                                                                                                                                                      
# | **Output:** `1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 20` 

for i in range(1, 21):
    if (i == 5 or i == 10 or i == 15):
        continue
    print(i)
print("\n")

# | **11** | **Skip Even Numbers and Stop at 30**   
# | Write a program to process numbers from **1 to 50**. If the number is even, use `continue` to skip it. If the number reaches **30**, use `break` to stop the loop. Print the odd numbers before reaching 30.                                                                                                                
# | The program should print odd numbers less than 30 and then stop.         

for i in range(1, 51):
    if (i % 2 == 0):
        continue
    elif( i == 30):
        break
    print(i)

print("\n")

# | **12** | **Skip Multiples of 3 and Stop at 50** 
# | Write a program to process numbers from **1 to 100**. If a number is divisible by **3**, use `continue` to skip it. If the number reaches **50**, use `break` to stop the loop. Print all other numbers.                                                                                                                    
# | Multiples of 3 should be skipped, and the loop should stop at 50.        

for i in range(1, 101):
    if (i % 3 == 0):
        continue
    elif( i == 50):
        break
    print(i)
print("\n")

# | **13** | **Password Verification**              
# | Write a program that sets a password and allows the user a maximum of **3 attempts** to enter it. If the password is incorrect, use `continue` to allow another attempt. If the password is correct, print **"Login Successful"** and use `break` to stop the loop. After 3 incorrect attempts, print **"Account Locked"**. 
# | **Input:** `python123` → **Output:** `Login Successful`                  

set_password = "python123"
attempts = 0
for attempts in range(3):
    user_input = input("Enter password: ")
    if (user_input == set_password):
        print("Login Successful")
        break
    else:
        print("Incorrect password. Try again.")

print("\n")

# | **14** | **Number Search**                      
# | Write a program to search for a target number between **1 and 100**. Take the target number as input from the user. If the current number does not match the target, use `continue`. If the number is found, print **"Number Found"** and use `break` to stop the loop.                                                     
# | **Input:** `35` → **Output:** `Number Found: 35`                         

target = int(input("Enter the target number (1-100): "))
for i in range(1, 101):
    if (i != target):
        continue
    else:
        print("Number Found:", i)
        break

