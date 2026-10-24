# 1. Basic for loop
print("=== Basic For Loop ===")

for i in range(5):
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4


# 2. Using range(start, stop)
print("\n=== Range With Start and Stop ===")

for i in range(1, 6):
    print(i)

# Output:
# 1
# 2
# 3
# 4
# 5


# 3. Using range(start, stop, step)
print("\n=== Range With Step ===")

for i in range(0, 11, 2):
    print(i)

# Output:
# 0
# 2
# 4
# 6
# 8
# 10


# 4. Counting backward
print("\n=== Counting Backward ===")

for i in range(5, 0, -1):
    print(i)

# Output:
# 5
# 4
# 3
# 2
# 1


# 5. Looping through a string
print("\n=== Looping Through a String ===")

name = "Python"

for character in name:
    print(character)

# Output:
# P
# y
# t
# h
# o
# n


# 6. Looping through a list
print("\n=== Looping Through a List ===")

fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# orange


# 7. Looping through a tuple
print("\n=== Looping Through a Tuple ===")

colors = ("red", "green", "blue")

for color in colors:
    print(color)

# Output:
# red
# green
# blue


# 8. Looping through a dictionary
print("\n=== Looping Through a Dictionary ===")

student = {
    "name": "Abebe",
    "age": 20,
    "grade": "A"
}

for key in student:
    print(key)

# Output:
# name
# age
# grade


# 9. Looping through dictionary keys and values
print("\n=== Dictionary Items ===")

for key, value in student.items():
    print(f"{key}: {value}")

# Output:
# name: Abebe
# age: 20
# grade: A


# 10. Using enumerate() to get indexes
print("\n=== Enumerate ===")

fruits = ["apple", "banana", "orange"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

# Output:
# 0 apple
# 1 banana
# 2 orange


# 11. Using enumerate() with a starting index
print("\n=== Enumerate With Start ===")

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

# Output:
# 1 apple
# 2 banana
# 3 orange


# 12. Basic while loop
print("\n=== Basic While Loop ===")

count = 1

while count <= 5:
    print(count)
    count += 1

# Output:
# 1
# 2
# 3
# 4
# 5


# 13. While loop counting backward
print("\n=== While Countdown ===")

count = 3

while count > 0:
    print(count)
    count -= 1

print("Finished!")

# Output:
# 3
# 2
# 1
# Finished!


# 14. Using break to stop a loop
print("\n=== Break ===")

for i in range(1, 10):
    if i == 5:
        break
    print(i)

# Output:
# 1
# 2
# 3
# 4


# 15. Using continue to skip an iteration
print("\n=== Continue ===")

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# Output:
# 1
# 2
# 4
# 5


# 16. Using pass as a placeholder
print("\n=== Pass ===")

for i in range(3):
    if i == 1:
        pass
    print(i)

# Output:
# 0
# 1
# 2

# pass does nothing; the loop continues normally.


# 17. Nested loops
print("\n=== Nested Loops ===")

for i in range(1, 4):
    for j in range(1, 3):
        print(i, j)

# Output:
# 1 1
# 1 2
# 2 1
# 2 2
# 3 1
# 3 2


# 18. Printing a multiplication table
print("\n=== Multiplication Table ===")

number = 5

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# Output:
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


# 19. Summing numbers with a loop
print("\n=== Sum of Numbers ===")

total = 0

for i in range(1, 6):
    total += i

print("Total:", total)

# Output:
# Total: 15


# 20. Finding even numbers
print("\n=== Even Numbers ===")

for i in range(1, 11):
    if i % 2 == 0:
        print(i)

# Output:
# 2
# 4
# 6
# 8
# 10


# 21. Finding odd numbers
print("\n=== Odd Numbers ===")

for i in range(1, 11):
    if i % 2 != 0:
        print(i)

# Output:
# 1
# 3
# 5
# 7
# 9


# 22. List comprehension
print("\n=== List Comprehension ===")

numbers = [1, 2, 3, 4, 5]

squares = [n ** 2 for n in numbers]
print(squares)

# Output:
# [1, 4, 9, 16, 25]


# 23. List comprehension with a condition
print("\n=== Filter With Comprehension ===")

numbers = [1, 2, 3, 4, 5, 6]

evens = [n for n in numbers if n % 2 == 0]
print(evens)

# Output:
# [2, 4, 6]


# 24. Using zip() to loop over two lists
print("\n=== Zip ===")

names = ["Abebe", "Hana", "Sara"]
scores = [85, 90, 95]

for name, score in zip(names, scores):
    print(f"{name}: {score}")

# Output:
# Abebe: 85
# Hana: 90
# Sara: 95


# 25. Looping over a two-dimensional list
print("\n=== Nested List ===")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for value in row:
        print(value, end=" ")
    print()

# Output:
# 1 2 3
# 4 5 6
# 7 8 9


# 26. Using else with a for loop
print("\n=== For-Else ===")

for i in range(3):
    print(i)
else:
    print("Loop completed.")

# Output:
# 0
# 1
# 2
# Loop completed.


# 27. Using else when a loop is not interrupted
print("\n=== For-Else With Break ===")

for i in range(5):
    if i == 3:
        print("Stopping the loop.")
        break
else:
    print("Loop completed without break.")

# Output:
# Stopping the loop.


# 28. Searching with a loop
print("\n=== Searching ===")

numbers = [10, 25, 30, 45, 50]
target = 30

for number in numbers:
    if number == target:
        print("Number found!")
        break
else:
    print("Number not found.")

# Output:
# Number found!


# 29. While loop with a condition
print("\n=== While Loop With Condition ===")

balance = 100
withdrawal = 30

while balance >= withdrawal:
    balance -= withdrawal
    print("Remaining balance:", balance)

# Output:
# Remaining balance: 70
# Remaining balance: 40
# Remaining balance: 10


# 30. Practical example: student scores
print("\n=== Student Scores ===")

scores = [85, 70, 92, 45, 60]

for score in scores:
    if score >= 50:
        print(score, "Passed")
    else:
        print(score, "Failed")

# Output:
# 85 Passed
# 70 Passed
# 92 Passed
# 45 Failed
# 60 Passed


# 31. Practical example: counting character frequency
print("\n=== Character Frequency ===")

text = "python"
frequency = {}

for character in text:
    frequency[character] = frequency.get(character, 0) + 1

print(frequency)

# Output:
# {'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1}


# 32. Practical example: finding the largest number
print("\n=== Largest Number ===")

numbers = [12, 45, 7, 89, 23]
largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Largest:", largest)

# Output:
# Largest: 89


# 33. Practical example: login attempts
print("\n=== Login Attempts ===")

correct_password = "python123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    entered_password = "wrong"  # Example input
    attempts += 1

    if entered_password == correct_password:
        print("Login successful.")
        break
    else:
        print("Incorrect password.")

else:
    print("Account temporarily locked.")

# Output:
# Incorrect password.
# Incorrect password.
# Incorrect password.
# Account temporarily locked.


# 34. Practical example: generating a pattern
print("\n=== Star Pattern ===")

for i in range(1, 5):
    print("*" * i)

# Output:
# *
# **
# ***
# ****


# 35. Practical example: removing selected values
print("\n=== Filtering a List ===")

numbers = [1, 2, 3, 4, 5, 6]
filtered = []

for number in numbers:
    if number > 3:
        filtered.append(number)

print(filtered)

# Output:
# [4, 5, 6]