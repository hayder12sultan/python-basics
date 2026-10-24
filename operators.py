# ============================================================
# 1. ARITHMETIC OPERATORS
# Perform mathematical calculations.
# ============================================================

a = 10
b = 3

print(a + b)   # Addition:        13
print(a - b)   # Subtraction:     7
print(a * b)   # Multiplication:  30
print(a / b)   # Division:        3.3333333333333335
print(a // b)  # Floor division:  3
print(a % b)   # Modulus:         1
print(a ** b)  # Exponentiation:  1000


# ============================================================
# 2. NEGATIVE NUMBERS AND FLOOR DIVISION
# Floor division rounds down, not toward zero.
# ============================================================

print(-7 // 3)  # Output: -3
print(-7 % 3)   # Output: 2

# Relationship: a == (a // b) * b + (a % b)
# Here: -7 == (-3 * 3) + 2


# ============================================================
# 3. ORDER OF OPERATIONS
# Parentheses can make calculations clearer.
# ============================================================

print(2 + 3 * 4)      # Output: 14
print((2 + 3) * 4)    # Output: 20
print(2 ** 3 ** 2)    # Output: 512
print(-2 ** 2)        # Output: -4
print((-2) ** 2)      # Output: 4

# Exponentiation groups from right to left.
# -2 ** 2 means -(2 ** 2), which is -4.


# ============================================================
# 4. COMPARISON OPERATORS
# Compare two values and return True or False.
# ============================================================

x = 10
y = 5

print(x == y)   # Equal:             False
print(x != y)   # Not equal:         True
print(x > y)    # Greater than:      True
print(x < y)    # Less than:         False
print(x >= y)   # Greater or equal:  True
print(x <= y)   # Less or equal:     False


# ============================================================
# 5. CHAINED COMPARISONS
# Compare multiple conditions in one expression.
# ============================================================

age = 20

print(18 <= age <= 65)  # Output: True
print(0 < age < 18)     # Output: False

number = 5
print(1 < number < 10)  # Output: True

# Equivalent to:
# 1 < number and number < 10


# ============================================================
# 6. ASSIGNMENT OPERATORS
# Assign or update variable values.
# ============================================================

number = 10
print(number)  # Output: 10

number += 5
print(number)  # Output: 15

number -= 3
print(number)  # Output: 12

number *= 2
print(number)  # Output: 24

number /= 4
print(number)  # Output: 6.0

number = 10
number //= 3
print(number)  # Output: 3

number = 10
number %= 4
print(number)  # Output: 2

number = 2
number **= 3
print(number)  # Output: 8


# ============================================================
# 7. BITWISE ASSIGNMENT OPERATORS
# Update integer bits in place.
# ============================================================

number = 6       # Binary: 0110

number &= 3       # 0110 & 0011 = 0010
print(number)    # Output: 2

number = 6
number |= 3       # 0110 | 0011 = 0111
print(number)    # Output: 7

number = 6
number ^= 3       # 0110 ^ 0011 = 0101
print(number)    # Output: 5

number = 6
number <<= 1      # Shift left by one bit
print(number)    # Output: 12

number = 6
number >>= 1      # Shift right by one bit
print(number)    # Output: 3


# ============================================================
# 8. WALRUS OPERATOR :=
# Assign a value inside an expression.
# ============================================================

if (length := len("Python")) > 5:
    print(length)

# Output: 6

# Useful when a value is needed both in a condition
# and later in the same expression or block.


# ============================================================
# 9. LOGICAL OPERATORS
# Combine or reverse conditions.
# ============================================================

a = True
b = False

print(a and b)  # Output: False
print(a or b)   # Output: True
print(not a)    # Output: False
print(not b)    # Output: True


# ============================================================
# 10. LOGICAL OPERATORS WITH COMPARISONS
# ============================================================

age = 25
has_id = True

print(age >= 18 and has_id)
# Output: True

print(age < 18 or has_id)
# Output: True

print(not has_id)
# Output: False


# ============================================================
# 11. SHORT-CIRCUIT EVALUATION
# and/or may skip evaluating the second operand.
# ============================================================

def check():
    print("Function executed")
    return True

print(False and check())
# Output: False
# check() is not executed.

print(True or check())
# Output: True
# check() is not executed.

print(True and check())
# Output:
# Function executed
# True


# ============================================================
# 12. and AND or RETURN OPERANDS, NOT ALWAYS BOOLEANS
# ============================================================

print(0 or 100)           # Output: 100
print(25 or 100)          # Output: 25
print("" and "Python")    # Output: (empty string)
print("Hello" and "Python")  # Output: Python

# and returns the first falsy operand, or the last operand.
# or returns the first truthy operand, or the last operand.


# ============================================================
# 13. BITWISE OPERATORS
# Operate on the binary representation of integers.
# ============================================================

a = 6  # Binary: 0110
b = 3  # Binary: 0011

print(a & b)   # AND:       2  (0010)
print(a | b)   # OR:        7  (0111)
print(a ^ b)   # XOR:       5  (0101)
print(~a)      # NOT:      -7
print(a << 1)  # Left shift: 12
print(a >> 1)  # Right shift: 3

# For Python integers, ~x equals -x - 1.


# ============================================================
# 14. MEMBERSHIP OPERATORS: in AND not in
# Check whether a value belongs to a collection.
# ============================================================

fruits = ["apple", "banana", "orange"]

print("apple" in fruits)
# Output: True

print("grape" in fruits)
# Output: False

print("grape" not in fruits)
# Output: True

print("Py" in "Python")
# Output: True


# ============================================================
# 15. MEMBERSHIP IN DICTIONARIES
# By default, membership checks keys, not values.
# ============================================================

student = {
    "name": "Sara",
    "age": 22
}

print("name" in student)
# Output: True

print("Sara" in student)
# Output: False

print("Sara" in student.values())
# Output: True


# ============================================================
# 16. IDENTITY OPERATORS: is AND is not
# Check whether two references point to the same object.
# ============================================================

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(list1 == list2)
# Output: True
# Their contents are equal.

print(list1 is list2)
# Output: False
# They are different list objects.

print(list1 is list3)
# Output: True
# Both refer to the same object.

print(list1 is not list2)
# Output: True


# ============================================================
# 17. is NONE
# The recommended way to check for None.
# ============================================================

result = None

print(result is None)
# Output: True

print(result is not None)
# Output: False

# Prefer "is None" over "== None".


# ============================================================
# 18. TERNARY CONDITIONAL EXPRESSION
# Choose one value based on a condition.
# ============================================================

age = 20

status = "Adult" if age >= 18 else "Minor"

print(status)
# Output: Adult

number = 7
kind = "Even" if number % 2 == 0 else "Odd"

print(kind)
# Output: Odd


# ============================================================
# 19. OPERATOR PRECEDENCE
# Higher-precedence operations are evaluated first.
# ============================================================

print(2 + 3 * 4)       # Output: 14
print((2 + 3) * 4)     # Output: 20
print(10 > 5 and 3 < 4)  # Output: True
print(not True or True)  # Output: True

# When unsure, use parentheses to make your intention clear.


# ============================================================
# 20. STRING OPERATORS
# + concatenates; * repeats.
# ============================================================

first = "Hello"
second = "Python"

print(first + " " + second)
# Output: Hello Python

print("Hi! " * 3)
# Output: Hi! Hi! Hi!

print("Python" == "Python")
# Output: True

print("apple" < "banana")
# Output: True
# Strings compare lexicographically by Unicode values.


# ============================================================
# 21. LIST OPERATORS
# ============================================================

list1 = [1, 2]
list2 = [3, 4]

print(list1 + list2)
# Output: [1, 2, 3, 4]

print(list1 * 3)
# Output: [1, 2, 1, 2, 1, 2]

print(2 in list1)
# Output: True

print(list1 == [1, 2])
# Output: True


# ============================================================
# 22. SET OPERATORS
# ============================================================

set_a = {1, 2, 3}
set_b = {3, 4, 5}

print(set_a | set_b)
# Output: {1, 2, 3, 4, 5} (display order may vary)
# Union

print(set_a & set_b)
# Output: {3}
# Intersection

print(set_a - set_b)
# Output: {1, 2}
# Difference

print(set_a ^ set_b)
# Output: {1, 2, 4, 5} (display order may vary)
# Symmetric difference


# ============================================================
# 23. DICTIONARY MERGE OPERATOR |
# Python 3.9+
# ============================================================

defaults = {"theme": "light", "language": "en"}
settings = {"theme": "dark"}

combined = defaults | settings

print(combined)
# Output: {'theme': 'dark', 'language': 'en'}

# The right-hand dictionary wins when keys overlap.


# ============================================================
# 24. AUGMENTED ASSIGNMENT WITH MUTABLE OBJECTS
# ============================================================

numbers = [1, 2]
numbers += [3, 4]

print(numbers)
# Output: [1, 2, 3, 4]

# For lists, += modifies the existing list in place.
# This differs from ordinary assignment in some situations.


# ============================================================
# 25. OBJECT COMPARISON WITH CUSTOM OPERATORS
# Operators can be customized through special methods.
# ============================================================

class Price:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        if not isinstance(other, Price):
            return NotImplemented
        return self.amount == other.amount

    def __lt__(self, other):
        if not isinstance(other, Price):
            return NotImplemented
        return self.amount < other.amount

price1 = Price(100)
price2 = Price(200)
price3 = Price(100)

print(price1 == price3)
# Output: True

print(price1 < price2)
# Output: True


# ============================================================
# 26. PRACTICAL EXAMPLE: ELIGIBILITY CHECK
# Combines comparison, logical, and membership operators.
# ============================================================

age = 22
country = "Ethiopia"
has_document = True

eligible = (
    age >= 18
    and country in ["Ethiopia", "Kenya"]
    and has_document
)

print(eligible)
# Output: True


# ============================================================
# 27. PRACTICAL EXAMPLE: DISCOUNT CALCULATION
# Combines arithmetic and comparison operators.
# ============================================================

price = 1000
discount_percent = 15

if 0 <= discount_percent <= 100:
    discount = price * discount_percent / 100
    final_price = price - discount

    print("Discount:", discount)
    # Output: Discount: 150.0

    print("Final price:", final_price)
    # Output: Final price: 850.0


# ============================================================
# 28. PRACTICAL EXAMPLE: EVEN OR ODD
# Uses modulus and comparison operators.
# ============================================================

number = 12

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Output: Even


# ============================================================
# 29. PRACTICAL EXAMPLE: ACCESS CONTROL
# Uses comparison, logical, and not operators.
# ============================================================

username = "admin"
password_correct = True
account_locked = False

can_login = (
    username == "admin"
    and password_correct
    and not account_locked
)

print(can_login)
# Output: True


# ============================================================
# 30. PRACTICAL EXAMPLE: BIT FLAGS
# Uses bitwise operators to combine options.
# ============================================================

READ = 1       # Binary: 001
WRITE = 2      # Binary: 010
EXECUTE = 4    # Binary: 100

permissions = READ | WRITE

print(permissions)
# Output: 3

print(bool(permissions & READ))
# Output: True

print(bool(permissions & EXECUTE))
# Output: False

permissions |= EXECUTE
print(permissions)
# Output: 7

permissions &= ~WRITE
print(permissions)
# Output: 5


# ============================================================
# END OF PYTHON OPERATORS EXAMPLES
# ============================================================