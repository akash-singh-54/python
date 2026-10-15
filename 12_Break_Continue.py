# BREAK AND CONTINUE
# ==================

# break:
# The break statement stops the loop completely.
# When break is executed, the loop terminates immediately.


# Example 1:
# Print numbers from 1 to 10, but stop the loop when i becomes 6.

for i in range(1, 11):
    if i == 6:
        break
    print(i)

# Output:
# 1
# 2
# 3
# 4
# 5


# Example 2:
# Print the table of 2, but stop the loop when the value becomes 14.

for i in range(2, 21, 2):
    if i == 14:
        break
    print(i)

# Output:
# 2
# 4
# 6
# 8
# 10
# 12


# Example 3:
# Using break with a while loop.

num = 2

while num <= 20:
    if num == 14:
        break
    print(num)
    num += 2

# Output:
# 2
# 4
# 6
# 8
# 10
# 12



# CONTINUE
# =========

# The continue statement skips the current iteration
# and moves to the next iteration of the loop.


# Example 1:
# Skip 2, 5 and 7.
# Stop the loop when i becomes 8.

for i in range(1, 11):
    if i == 2:
        continue

    elif i == 5:
        continue

    elif i == 7:
        continue

    elif i == 8:
        break

    print(i)

# Output:
# 1
# 3
# 4
# 6


# Example 2:
# Using continue with a while loop.
# Skip 2, 4 and 6.

num = 0

while num < 10:
    num += 1

    if num == 2:
        continue

    elif num == 4:
        continue

    elif num == 6:
        continue

    print(num)

# Output:
# 1
# 3
# 5
# 7
# 8
# 9
# 10



# PRACTICE QUESTION
# =================

# WAP (Write A Program) to print even numbers
# from 1 to 30 and stop the loop when the value reaches 18.

num = 1

while num <= 30:
    if num % 2 == 0:
        if num == 18:
            break
        print(num)

    num = num + 1

# Output:
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16