# 1. Simple if statement
print("=== Simple if ===")

age = 20

if age >= 18:
    print("You are an adult.")

# Output:
# You are an adult.


# 2. if-else statement
print("\n=== if-else ===")

age = 16

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Output:
# You are a minor.


# 3. if-elif-else statement
print("\n=== if-elif-else ===")

score = 85

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 50:
    print("Grade D")
else:
    print("Grade F")

# Output:
# Grade B


# 4. Multiple conditions using and
print("\n=== and operator ===")

age = 22
has_id = True

if age >= 18 and has_id:
    print("Access granted.")
else:
    print("Access denied.")

# Output:
# Access granted.


# 5. Multiple conditions using or
print("\n=== or operator ===")

day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("It is the weekend.")
else:
    print("It is a weekday.")

# Output:
# It is the weekend.


# 6. Using not
print("\n=== not operator ===")

is_raining = False

if not is_raining:
    print("You can go outside.")
else:
    print("Take an umbrella.")

# Output:
# You can go outside.


# 7. Comparison operators
print("\n=== Comparison operators ===")

a = 10
b = 5

print(a == b)  # Equal to
print(a != b)  # Not equal to
print(a > b)   # Greater than
print(a < b)   # Less than
print(a >= b)  # Greater than or equal to
print(a <= b)  # Less than or equal to

# Output:
# False
# True
# True
# False
# True
# False


# 8. Checking whether a number is positive, negative, or zero
print("\n=== Positive, Negative, or Zero ===")

number = -5

if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")

# Output:
# Negative number


# 9. Checking even or odd numbers
print("\n=== Even or Odd ===")

number = 7

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Output:
# Odd number


# 10. Nested if statements
print("\n=== Nested if ===")

age = 22
has_license = True

if age >= 18:
    print("You meet the age requirement.")

    if has_license:
        print("You can drive.")
    else:
        print("You need a driving license.")
else:
    print("You are too young to drive.")

# Output:
# You meet the age requirement.
# You can drive.


# 11. Checking multiple ranges
print("\n=== Number Ranges ===")

temperature = 28

if temperature < 0:
    print("Freezing conditions")
elif temperature < 15:
    print("Cold weather")
elif temperature < 25:
    print("Moderate weather")
elif temperature < 35:
    print("Warm weather")
else:
    print("Hot weather")

# Output:
# Warm weather


# 12. Membership conditions using in
print("\n=== Membership with in ===")

fruits = ["apple", "banana", "orange"]

if "banana" in fruits:
    print("Banana is available.")
else:
    print("Banana is not available.")

# Output:
# Banana is available.


# 13. Membership using not in
print("\n=== Membership with not in ===")

blocked_users = ["admin", "guest"]
username = "abebe"

if username not in blocked_users:
    print("Username is allowed.")
else:
    print("Username is blocked.")

# Output:
# Username is allowed.


# 14. String comparisons
print("\n=== String Comparisons ===")

password = "python123"

if password == "python123":
    print("Password matches.")
else:
    print("Incorrect password.")

# Output:
# Password matches.


# 15. Checking empty and non-empty values
print("\n=== Truthy and Falsy Values ===")

username = ""

if username:
    print("Username provided.")
else:
    print("Username is empty.")

items = [1, 2, 3]

if items:
    print("The list contains items.")
else:
    print("The list is empty.")

# Output:
# Username is empty.
# The list contains items.


# 16. Checking None
print("\n=== Checking None ===")

result = None

if result is None:
    print("No result available.")
else:
    print("Result:", result)

# Output:
# No result available.


# 17. Conditional expression (ternary operator)
print("\n=== Conditional Expression ===")

age = 20

status = "Adult" if age >= 18 else "Minor"

print(status)

# Output:
# Adult


# 18. Conditional expression with calculations
print("\n=== Conditional Calculation ===")

a = 10
b = 20

largest = a if a > b else b

print("Largest:", largest)

# Output:
# Largest: 20


# 19. Using conditions in list comprehensions
print("\n=== Conditional List Comprehension ===")

numbers = [1, 2, 3, 4, 5, 6]

evens = [n for n in numbers if n % 2 == 0]

print(evens)

# Output:
# [2, 4, 6]


# 20. Using if-else inside a list comprehension
print("\n=== if-else in List Comprehension ===")

numbers = [1, 2, 3, 4, 5]

labels = ["Even" if n % 2 == 0 else "Odd" for n in numbers]

print(labels)

# Output:
# ['Odd', 'Even', 'Odd', 'Even', 'Odd']


# 21. Checking login credentials
print("\n=== Login Example ===")

username = "abebe"
password = "pass123"

if username == "abebe" and password == "pass123":
    print("Login successful.")
else:
    print("Invalid username or password.")

# Output:
# Login successful.


# 22. Student grading system
print("\n=== Student Grading System ===")

score = 78

if score < 0 or score > 100:
    print("Invalid score.")
elif score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Output:
# Grade: C


# 23. Checking leap years
print("\n=== Leap Year ===")

year = 2024

if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")

# Output:
# Leap year


# 24. Using conditions with dictionaries
print("\n=== Dictionary Condition ===")

student = {
    "name": "Abebe",
    "score": 88
}

if student["score"] >= 50:
    print(student["name"], "passed.")
else:
    print(student["name"], "failed.")

# Output:
# Abebe passed.


# 25. Practical example: shopping discount
print("\n=== Shopping Discount ===")

total_price = 1200

if total_price >= 1000:
    discount = total_price * 0.10
elif total_price >= 500:
    discount = total_price * 0.05
else:
    discount = 0

final_price = total_price - discount

print("Original price:", total_price)
print("Discount:", discount)
print("Final price:", final_price)

# Output:
# Original price: 1200
# Discount: 120.0
# Final price: 1080.0


# 26. Practical example: ATM withdrawal
print("\n=== ATM Withdrawal ===")

balance = 5000
withdrawal = 1500

if withdrawal <= 0:
    print("Enter a valid withdrawal amount.")
elif withdrawal > balance:
    print("Insufficient balance.")
else:
    balance -= withdrawal
    print("Withdrawal successful.")
    print("Remaining balance:", balance)

# Output:
# Withdrawal successful.
# Remaining balance: 3500


# 27. Practical example: determining access permissions
print("\n=== Access Permissions ===")

role = "admin"

if role == "admin":
    print("Full access granted.")
elif role == "editor":
    print("Editing access granted.")
elif role == "viewer":
    print("Read-only access granted.")
else:
    print("Access denied.")

# Output:
# Full access granted.


# 28. Practical example: validating user input
print("\n=== Input Validation ===")

email = "user@example.com"
age = 21

if not email:
    print("Email is required.")
elif "@" not in email:
    print("Email format is invalid.")
elif age < 18:
    print("You must be at least 18.")
else:
    print("Input accepted.")

# Output:
# Input accepted.