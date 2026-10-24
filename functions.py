# ==================================================
# 1. BASIC FUNCTION
# ==================================================

def greet():
    print("Hello, world!")

greet()
# Output: Hello, world!


# ==================================================
# 2. FUNCTION WITH PARAMETERS
# ==================================================

def greet_user(name):
    print("Hello,", name)

greet_user("Abebe")
# Output: Hello, Abebe


# ==================================================
# 3. MULTIPLE PARAMETERS
# ==================================================

def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce("Abebe", 20)
# Output: My name is Abebe and I am 20 years old.


# ==================================================
# 4. RETURN STATEMENT
# ==================================================

def add(a, b):
    return a + b

result = add(5, 3)
print(result)
# Output: 8

# return sends a value back to the caller.
# print displays a value on the screen.


# ==================================================
# 5. FUNCTION WITH DEFAULT PARAMETERS
# ==================================================

def greet_person(name="Guest"):
    print(f"Welcome, {name}!")

greet_person()
# Output: Welcome, Guest!

greet_person("Sara")
# Output: Welcome, Sara!


# ==================================================
# 6. POSITIONAL ARGUMENTS
# ==================================================

def subtract(a, b):
    return a - b

print(subtract(10, 4))
# Output: 6

# Arguments are assigned according to their position.


# ==================================================
# 7. KEYWORD ARGUMENTS
# ==================================================

def student_info(name, age):
    print(name, age)

student_info(age=21, name="Sara")
# Output: Sara 21

# Keyword arguments specify parameter names.


# ==================================================
# 8. MIXING POSITIONAL AND KEYWORD ARGUMENTS
# ==================================================

def describe_person(name, age, city):
    print(f"{name}, {age}, from {city}")

describe_person("Abebe", 20, city="Addis Ababa")
# Output: Abebe, 20, from Addis Ababa

# Positional arguments must come before keyword arguments.


# ==================================================
# 9. RETURNING MULTIPLE VALUES
# ==================================================

def calculate(a, b):
    total = a + b
    difference = a - b
    return total, difference

sum_result, difference_result = calculate(10, 4)

print(sum_result)
# Output: 14

print(difference_result)
# Output: 6

# Python returns multiple values as a tuple.


# ==================================================
# 10. FUNCTION WITH A CONDITION
# ==================================================

def check_age(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"

print(check_age(20))
# Output: Adult

print(check_age(15))
# Output: Minor


# ==================================================
# 11. FUNCTION WITH A LOOP
# ==================================================

def print_numbers(limit):
    for number in range(1, limit + 1):
        print(number, end=" ")
    print()

print_numbers(5)
# Output: 1 2 3 4 5


# ==================================================
# 12. LOCAL VARIABLES
# ==================================================

def show_message():
    message = "This is a local variable."
    print(message)

show_message()
# Output: This is a local variable.

# message exists only inside show_message().
# print(message) outside the function would cause a NameError.


# ==================================================
# 13. GLOBAL VARIABLES
# ==================================================

company = "Tech Solutions"

def show_company():
    print(company)

show_company()
# Output: Tech Solutions

# A function can read a global variable.


# ==================================================
# 14. MODIFYING A GLOBAL VARIABLE
# ==================================================

counter = 0

def increase_counter():
    global counter
    counter += 1

increase_counter()
increase_counter()

print(counter)
# Output: 2

# Use global only when necessary.
# Returning a new value is often easier to maintain.


# ==================================================
# 15. *ARGS — VARIABLE POSITIONAL ARGUMENTS
# ==================================================

def add_all(*numbers):
    return sum(numbers)

print(add_all(1, 2, 3))
# Output: 6

print(add_all(10, 20, 30, 40))
# Output: 100

# *numbers collects positional arguments into a tuple.


# ==================================================
# 16. **KWARGS — VARIABLE KEYWORD ARGUMENTS
# ==================================================

def display_details(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

display_details(name="Sara", age=22, city="Adama")
# Output:
# name: Sara
# age: 22
# city: Adama

# **details collects keyword arguments into a dictionary.


# ==================================================
# 17. COMBINING PARAMETERS, *ARGS, AND **KWARGS
# ==================================================

def example(first, *args, **kwargs):
    print("First:", first)
    print("Extra positional:", args)
    print("Extra keyword:", kwargs)

example("Python", 1, 2, level="Beginner", active=True)
# Output:
# First: Python
# Extra positional: (1, 2)
# Extra keyword: {'level': 'Beginner', 'active': True}


# ==================================================
# 18. LAMBDA FUNCTIONS
# ==================================================

square = lambda number: number ** 2

print(square(5))
# Output: 25

multiply = lambda a, b: a * b

print(multiply(4, 3))
# Output: 12

# lambda creates a small anonymous function.
# Use def for most functions that need multiple statements.


# ==================================================
# 19. FUNCTION AS AN ARGUMENT
# ==================================================

def square_number(number):
    return number ** 2

def apply_function(function, value):
    return function(value)

print(apply_function(square_number, 4))
# Output: 16

# Functions can be passed to other functions.


# ==================================================
# 20. BUILT-IN FUNCTIONS WITH YOUR FUNCTION
# ==================================================

numbers = [4, 1, 8, 2, 5]

def is_even(number):
    return number % 2 == 0

even_numbers = list(filter(is_even, numbers))

print(even_numbers)
# Output: [4, 8, 2]

# filter() keeps items for which the function returns True.


# ==================================================
# 21. MAP FUNCTION
# ==================================================

def double(number):
    return number * 2

numbers = [1, 2, 3, 4]

doubled = list(map(double, numbers))

print(doubled)
# Output: [2, 4, 6, 8]

# map() applies a function to each item.


# ==================================================
# 22. RECURSION
# A FUNCTION CALLING ITSELF
# ==================================================

def factorial(number):
    if number <= 1:       # Base case: stops recursion
        return 1
    return number * factorial(number - 1)

print(factorial(5))
# Output: 120

# factorial(5) = 5 * 4 * 3 * 2 * 1
# Recursion needs a base case to stop.


# ==================================================
# 23. DOCSTRINGS
# DOCUMENTING A FUNCTION
# ==================================================

def calculate_area(length, width):
    """Return the area of a rectangle."""
    return length * width

print(calculate_area(5, 3))
# Output: 15

print(calculate_area.__doc__)
# Output: Return the area of a rectangle.


# ==================================================
# 24. TYPE HINTS
# ==================================================

def divide(a: float, b: float) -> float:
    return a / b

print(divide(10, 2))
# Output: 5.0

# Type hints explain expected types.
# Python does not automatically enforce these hints.


# ==================================================
# 25. PASSING A LIST TO A FUNCTION
# ==================================================

def add_item(items, item):
    items.append(item)

fruits = ["apple", "banana"]
add_item(fruits, "orange")

print(fruits)
# Output: ['apple', 'banana', 'orange']

# Lists are mutable; modifying the list affects the original object.


# ==================================================
# 26. AVOID MUTABLE DEFAULT ARGUMENTS
# ==================================================

# Avoid this pattern:
# def add_item(item, items=[]):
#     items.append(item)
#     return items

# The same default list is reused between calls.

def add_item_safely(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item_safely("apple"))
# Output: ['apple']

print(add_item_safely("banana"))
# Output: ['banana']


# ==================================================
# 27. FUNCTION COMPOSITION
# USING ONE FUNCTION INSIDE ANOTHER
# ==================================================

def double_number(number):
    return number * 2

def add_ten(number):
    return number + 10

result = add_ten(double_number(5))

print(result)
# Output: 20
# First: 5 * 2 = 10
# Then: 10 + 10 = 20


# ==================================================
# 28. PRACTICAL EXAMPLE: STUDENT GRADING
# ==================================================

def calculate_average(scores):
    if not scores:
        return 0
    return sum(scores) / len(scores)

def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"

student_scores = [85, 90, 78]

average = calculate_average(student_scores)
grade = get_grade(average)

print("Average:", average)
# Output: Average: 84.33333333333333

print("Grade:", grade)
# Output: Grade: B


# ==================================================
# 29. PRACTICAL EXAMPLE: SIMPLE CALCULATOR
# ==================================================

def calculator(a, operator, b):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            return "Cannot divide by zero"
        return a / b
    else:
        return "Invalid operator"

print(calculator(10, "+", 5))
# Output: 15

print(calculator(10, "/", 2))
# Output: 5.0

print(calculator(10, "/", 0))
# Output: Cannot divide by zero


# ==================================================
# 30. PRACTICAL EXAMPLE: USER VALIDATION
# ==================================================

def validate_username(username):
    if len(username) < 3:
        return "Username is too short"
    elif not username.isalnum():
        return "Use letters and numbers only"
    else:
        return "Username is valid"

print(validate_username("ab"))
# Output: Username is too short

print(validate_username("user123"))
# Output: Username is valid

print(validate_username("user_123"))
# Output: Use letters and numbers only


# ==================================================
# 31. FUNCTION RETURNING A BOOLEAN
# ==================================================

def is_positive(number):
    return number > 0

print(is_positive(10))
# Output: True

print(is_positive(-3))
# Output: False

if is_positive(7):
    print("The number is positive.")
# Output: The number is positive.


# ==================================================
# 32. EARLY RETURN
# EXITING A FUNCTION WHEN A CONDITION IS MET
# ==================================================

def divide_safely(a, b):
    if b == 0:
        return "Error: division by zero"
    return a / b

print(divide_safely(12, 3))
# Output: 4.0

print(divide_safely(12, 0))
# Output: Error: division by zero


# ==================================================
# 33. UNPACKING ARGUMENTS
# ==================================================

def show_coordinates(x, y):
    print(f"x={x}, y={y}")

coordinates = (10, 20)
show_coordinates(*coordinates)
# Output: x=10, y=20

person = {"name": "Sara", "age": 22}

def display_person(name, age):
    print(name, age)

display_person(**person)
# Output: Sara 22


# ==================================================
# 34. NESTED FUNCTIONS
# A FUNCTION DEFINED INSIDE ANOTHER FUNCTION
# ==================================================

def outer_function(name):
    def inner_function():
        return f"Hello, {name}!"

    return inner_function()

print(outer_function("Abebe"))
# Output: Hello, Abebe!


# ==================================================
# 35. CLOSURES
# AN INNER FUNCTION REMEMBERS ITS OUTER VARIABLES
# ==================================================

def make_multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply

triple = make_multiplier(3)

print(triple(5))
# Output: 15

print(triple(10))
# Output: 30


# ==================================================
# 36. GENERATOR FUNCTIONS
# YIELD VALUES ONE AT A TIME
# ==================================================

def count_up_to(limit):
    number = 1
    while number <= limit:
        yield number
        number += 1

for number in count_up_to(3):
    print(number)
# Output:
# 1
# 2
# 3

# yield produces a value while preserving the function's state.


# ==================================================
# 37. MAIN FUNCTION AND SCRIPT ENTRY POINT
# ==================================================

def main():
    message = "Program started."
    print(message)

if __name__ == "__main__":
    main()

# Output: Program started.
# This pattern lets a file be imported without automatically
# running main() when it is imported by another module.


# ==================================================
# END OF PYTHON FUNCTIONS EXAMPLES
# ==================================================