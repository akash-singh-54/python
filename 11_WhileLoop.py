# WHILE LOOP
# ==========

# A while loop is used to repeatedly execute a block of code
# as long as the given condition is True.

# Syntax:

# while(condition):
#     statement


# Example 1:
# Print numbers from 1 to 10 using a while loop.

num = 1

while num <= 10:
    print(num)
    num = num + 1


# TABLE OF 2
# ===========

# Print the table of 2 using a while loop.

num = 2

while num <= 20:
    print(num)
    num = num + 2


# REVERSE LOOP
# ============

# Print numbers from 10 to 1 using a for loop.

for i in range(10, 0, -1):
    print(i)


# Print numbers from 10 to 1 using a while loop.

num = 10

while num >= 1:
    print(num)
    num -= 1


# NEGATIVE NUMBERS
# ================

# Print numbers from -10 to -1 using a for loop.

for i in range(-10, 0, 1):
    print(i)


# Print numbers from -10 to -1 using a while loop.

num = -10

while num <= -1:
    print(num)
    num += 1


# PRACTICE QUESTION
# =================

# WAP to print even numbers from 1 to 30
# and stop the loop when the value reaches 18.
# Using a for loop.

for i in range(1, 31):

    if i % 2 != 0:
        continue

    elif i == 18:
        break

    print(i)

# Output:
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16


# Using a while loop.

n = 1

while n <= 30:

    if n % 2 == 0:

        if n == 18:
            break

        print(n)

    n += 1

# Output:
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16