# 1. Creating variables
name = "Abebe"
age = 20
height = 1.75
is_student = True

print("=== Creating Variables ===")
print(name)
print(age)
print(height)
print(is_student)

# 2. Checking data types
print("\n=== Data Types ===")
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

# 3. Reassigning variables
print("\n=== Reassigning Variables ===")
score = 50
print(score)
score = 80
print(score)

# 4. Assigning one variable to another
print("\n=== Assigning Variables ===")
a = 10
b = a
a = 20
print("a =", a)
print("b =", b)

# 5. Multiple variable assignment
print("\n=== Multiple Assignment ===")
x, y, z = 10, 20, 30
print(x, y, z)

p = q = r = 100
print(p, q, r)

# 6. Swapping variables
print("\n=== Swapping Variables ===")
first = 5
second = 15
first, second = second, first
print("First:", first)
print("Second:", second)

# 7. Case-sensitive variables
print("\n=== Case Sensitivity ===")
city = "Addis Ababa"
City = "Dire Dawa"
print(city)
print(City)

# 8. Calculations with variables
print("\n=== Calculations ===")
price = 100
quantity = 3
total = price * quantity
print("Price:", price)
print("Quantity:", quantity)
print("Total:", total)

# 9. Compound assignment operators
print("\n=== Assignment Operators ===")
number = 10
number += 5
print(number)
number -= 3
print(number)
number *= 2
print(number)
number /= 4
print(number)

# 10. Combining variables with strings
print("\n=== Strings and Variables ===")
student = "Abebe"
student_age = 20
print("My name is", student)
print(f"I am {student_age} years old.")

# 11. Converting data types
print("\n=== Type Conversion ===")
age_text = "20"
price_text = "99.5"
age_number = int(age_text)
price_number = float(price_text)
print(age_number + 5)
print(price_number + 0.5)
print(str(age_number) + " years old")

# 12. Getting values from the user
print("\n=== User Input ===")
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
print(f"Hello, {user_name}!")
print(f"Next year, you will be {user_age + 1}.")

# 13. None value
print("\n=== None Value ===")
result = None
print(result)
print(result is None)
result = 100
print(result)

# 14. Constants
print("\n=== Constants ===")
PI = 3.14159
MAX_USERS = 100
radius = 5
area = PI * radius ** 2
print("Area:", area)
print("Maximum users:", MAX_USERS)

# 15. Local and global variables
print("\n=== Local and Global Variables ===")
message = "Global message"

def greet():
    message = "Local message"
    print(message)

greet()
print(message)

# 16. Checking whether a variable exists
print("\n=== Checking Variables ===")
student_name = "Abebe"
print("student_name" in globals())
print("unknown_name" in globals())

# 17. Deleting a variable
print("\n=== Deleting Variables ===")
temporary_score = 90
print(temporary_score)
del temporary_score
print("Variable deleted successfully.")

# 18. Complete student example
print("\n=== Student Information ===")
student_name = "Abebe"
student_age = 20
math_score = 85
python_score = 90
is_enrolled = True

average_score = (math_score + python_score) / 2
student_age += 1

print(f"Name: {student_name}")
print(f"Age next year: {student_age}")
print(f"Math score: {math_score}")
print(f"Python score: {python_score}")
print(f"Average score: {average_score}")
print(f"Enrolled: {is_enrolled}")
print(f"Average as integer: {int(average_score)}")