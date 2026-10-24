# ============================================================
# 1. STRING METHODS
# ============================================================

text = "  Hello Python World  "

print(text.lower())                  # hello python world
print(text.upper())                  # HELLO PYTHON WORLD
print(text.title())                  # Hello Python World
print(text.capitalize())             # Hello python world
print(text.swapcase())               # hELLO pYTHON wORLD
print(text.strip())                  # Hello Python World
print(text.lstrip())                 # Hello Python World  (right spaces remain)
print(text.rstrip())                 #   Hello Python World (left spaces remain)

print("hello".replace("l", "x"))     # hexxo
print("apple,banana".split(","))     # ['apple', 'banana']
print("-".join(["2026", "10", "24"]))  # 2026-10-24

print("python".find("th"))           # 2
print("python".index("th"))          # 2
print("banana".count("a"))           # 3
print("Python".startswith("Py"))     # True
print("Python".endswith("on"))       # True

print("python".isalpha())            # True
print("123".isdigit())               # True
print("123".isnumeric())             # True
print("hello123".isalnum())          # True
print("   ".isspace())               # True
print("hello".islower())             # True
print("HELLO".isupper())             # True
print("Hello World".istitle())       # True

print("42".zfill(5))                 # 00042
print("hello".center(9, "-"))        # --hello--
print("hello".ljust(8, "-"))         # hello---
print("hello".rjust(8, "-"))         # ---hello
print("Hello {}".format("Ali"))      # Hello Ali

# Strings are immutable: methods return new strings.
# text.upper() does not change the original text.


# ============================================================
# 2. LIST METHODS
# ============================================================

numbers = [10, 20, 30]

numbers.append(40)
print(numbers)                       # [10, 20, 30, 40]

numbers.extend([50, 60])
print(numbers)                       # [10, 20, 30, 40, 50, 60]

numbers.insert(1, 15)
print(numbers)                       # [10, 15, 20, 30, 40, 50, 60]

numbers.remove(30)
print(numbers)                       # [10, 15, 20, 40, 50, 60]

last = numbers.pop()
print(last)                          # 60
print(numbers)                       # [10, 15, 20, 40, 50]

first = numbers.pop(0)
print(first)                         # 10

numbers.append(20)
print(numbers.index(20))             # 1
print(numbers.count(20))             # 2

numbers.sort()
print(numbers)                       # [15, 20, 20, 40, 50]

numbers.sort(reverse=True)
print(numbers)                       # [50, 40, 20, 20, 15]

numbers.reverse()
print(numbers)                       # [15, 20, 20, 40, 50]

copy_numbers = numbers.copy()
print(copy_numbers)                  # [15, 20, 20, 40, 50]

numbers.clear()
print(numbers)                       # []

# Useful built-ins with lists
values = [4, 2, 9, 1]

print(len(values))                   # 4
print(min(values))                   # 1
print(max(values))                   # 9
print(sum(values))                   # 16
print(sorted(values))                # [1, 2, 4, 9]
print(list(reversed(values)))        # [1, 9, 2, 4]


# ============================================================
# 3. TUPLE METHODS
# ============================================================

items = ("apple", "banana", "apple", "orange")

print(items.count("apple"))          # 2
print(items.index("banana"))         # 1
print(len(items))                    # 4

# Tuples are immutable: no append(), remove(), or sort().
# Convert to a list if you need to modify the contents.
editable = list(items)
editable.append("grape")
items = tuple(editable)
print(items)                         # ('apple', 'banana', 'apple', 'orange', 'grape')


# ============================================================
# 4. SET METHODS
# ============================================================

a = {1, 2, 3}
b = {3, 4, 5}

a.add(6)
print(a)                             # {1, 2, 3, 6}

a.update([7, 8])
print(a)                             # Contains 1, 2, 3, 6, 7, 8

a.discard(100)                       # No error if missing
a.remove(8)                          # Error if missing
removed = a.pop()                    # Removes an arbitrary element

print(a.union(b))                    # All unique elements
print(a.intersection(b))             # Common elements
print(a.difference(b))               # In a but not b
print(a.symmetric_difference(b))     # In either set, but not both

print({1, 2}.issubset({1, 2, 3}))    # True
print({1, 2, 3}.issuperset({1, 2}))  # True
print({1, 2}.isdisjoint({3, 4}))     # True

a_copy = a.copy()
a.clear()
print(a)                             # set()

# Set methods modify the set or return a new set,
# depending on the method. Sets are unordered.


# ============================================================
# 5. DICTIONARY METHODS
# ============================================================

student = {
    "name": "Sara",
    "age": 21,
    "grade": 90
}

print(student.keys())                # dict_keys(['name', 'age', 'grade'])
print(student.values())              # dict_values(['Sara', 21, 90])
print(student.items())               # Key-value pairs

print(student.get("name"))           # Sara
print(student.get("city", "Unknown"))  # Unknown

student.update({"age": 22, "city": "Addis Ababa"})
print(student)

removed_grade = student.pop("grade")
print(removed_grade)                 # 90

last_pair = student.popitem()        # Removes the last inserted pair
print(last_pair)

student.setdefault("country", "Ethiopia")
print(student["country"])            # Ethiopia

student_copy = student.copy()
student.clear()
print(student)                       # {}

# Create a dictionary from keys
new_student = dict.fromkeys(["name", "age"], None)
print(new_student)                   # {'name': None, 'age': None}

# Merge dictionaries (Python 3.9+)
first_dict = {"a": 1, "b": 2}
second_dict = {"b": 9, "c": 3}

print(first_dict | second_dict)      # {'a': 1, 'b': 9, 'c': 3}
first_dict |= second_dict
print(first_dict)                    # {'a': 1, 'b': 9, 'c': 3}


# ============================================================
# 6. NUMBER METHODS AND MATHEMATICAL BUILT-INS
# ============================================================

import math

number = -15.7

print(abs(number))                   # 15.7
print(round(3.14159, 2))             # 3.14
print(pow(2, 3))                     # 8
print(divmod(17, 5))                 # (3, 2)

print(math.floor(3.9))               # 3
print(math.ceil(3.1))                # 4
print(math.sqrt(25))                 # 5.0
print(math.factorial(5))             # 120
print(math.gcd(12, 18))              # 6
print(math.pi)                       # 3.141592...

print(int("25"))                     # 25
print(float("3.5"))                  # 3.5
print(str(100))                      # "100"
print(bool(1))                       # True


# ============================================================
# 7. COMMON BUILT-IN FUNCTIONS
# ============================================================

names = ["Ali", "Sara", "Mimi"]

print(len(names))                    # 3
print(type(names))                   # <class 'list'>
print(isinstance(names, list))       # True
print(enumerate(names))              # An enumerate iterator
print(list(enumerate(names)))        # [(0, 'Ali'), (1, 'Sara'), (2, 'Mimi')]

scores = [75, 90, 82]
print(sum(scores))                   # 247
print(min(scores))                   # 75
print(max(scores))                   # 90
print(sorted(scores))                # [75, 82, 90]
print(any([False, True, False]))     # True
print(all([True, True, False]))      # False

print(list(zip(names, scores)))      # [('Ali', 75), ('Sara', 90), ('Mimi', 82)]

print(list(map(str, scores)))        # ['75', '90', '82']
print(list(filter(lambda x: x >= 80, scores)))  # [90, 82]

# any(): True if at least one item is truthy.
# all(): True if every item is truthy.
# map(): applies a function to each item.
# filter(): keeps items that pass a condition.


# ============================================================
# 8. FILE METHODS
# ============================================================

# Write to a file
with open("example.txt", "w", encoding="utf-8") as file:
    file.write("Hello Python\n")
    file.writelines(["First line\n", "Second line\n"])

# Read the whole file
with open("example.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

# Read one line
with open("example.txt", "r", encoding="utf-8") as file:
    print(file.readline())           # Hello Python

# Read all lines into a list
with open("example.txt", "r", encoding="utf-8") as file:
    print(file.readlines())

# Append instead of overwriting
with open("example.txt", "a", encoding="utf-8") as file:
    file.write("Appended line\n")

# Common file methods:
# read(), readline(), readlines(), write(), writelines(),
# seek(), tell(), close()
#
# "r" = read, "w" = overwrite/write, "a" = append.
# "with" closes the file automatically.


# ============================================================
# 9. OBJECT-ORIENTED PROGRAMMING METHODS
# ============================================================

class Student:
    school = "ABC School"            # Class attribute

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def introduce(self):             # Instance method
        return f"My name is {self.name}"

    def has_passed(self):
        return self.score >= 50

    @classmethod
    def get_school(cls):             # Class method
        return cls.school

    @staticmethod
    def is_valid_score(score):       # Static method
        return 0 <= score <= 100


s = Student("Sara", 85)

print(s.introduce())                 # My name is Sara
print(s.has_passed())                # True
print(Student.get_school())          # ABC School
print(Student.is_valid_score(85))    # True

# Common special/dunder methods:
# __init__()   initializes an object
# __str__()    defines its readable string representation
# __repr__()   defines its developer-oriented representation
# __len__()    defines behavior for len(object)
# __eq__()     defines equality using ==
# __add__()    defines behavior for +

class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return self.title

book = Book("Python Basics")
print(book)                          # Python Basics


# ============================================================
# 10. USEFUL METHODS FOR WORKING WITH DATA
# ============================================================

# Remove duplicates while preserving order
values = [1, 2, 2, 3, 1, 4]
unique_values = list(dict.fromkeys(values))
print(unique_values)                 # [1, 2, 3, 4]

# Count occurrences
from collections import Counter

colors = ["red", "blue", "red", "green", "blue", "red"]
print(Counter(colors))
# Counter({'red': 3, 'blue': 2, 'green': 1})

# Group data with a dictionary
students = [
    {"name": "Ali", "grade": "A"},
    {"name": "Sara", "grade": "B"},
    {"name": "Mimi", "grade": "A"}
]

grouped = {}

for student in students:
    grouped.setdefault(student["grade"], []).append(student["name"])

print(grouped)
# {'A': ['Ali', 'Mimi'], 'B': ['Sara']}

# Sort dictionaries by a value
products = [
    {"name": "Pen", "price": 10},
    {"name": "Book", "price": 50},
    {"name": "Bag", "price": 100}
]

products.sort(key=lambda product: product["price"])
print(products)                      # Cheapest product first

# Safely get a dictionary value
user = {"name": "Ali"}
print(user.get("email", "Not provided"))  # Not provided


# ============================================================
# 11. METHODS FOR INSPECTING AND MANIPULATING STRINGS
# ============================================================

email = "  ALI@example.com  "

clean_email = email.strip().lower()
print(clean_email)                   # ali@example.com

sentence = "Python is easy to learn"
words = sentence.split()
print(words)                          # ['Python', 'is', 'easy', 'to', 'learn']
print(" ".join(words))                # Python is easy to learn

url = "https://example.com"
print(url.removeprefix("https://"))   # example.com

filename = "report.txt"
print(filename.removesuffix(".txt"))  # report

# removeprefix() and removesuffix() are available in Python 3.9+.


# ============================================================
# 12. QUICK METHOD-CALLING RULES
# ============================================================

# object.method(arguments)

message = "hello"
print(message.upper())               # Method called on a string object

items = [1, 2]
items.append(3)                      # Modifies the list
print(items)                         # [1, 2, 3]

data = {"name": "Ali"}
print(data.get("name"))              # Safely retrieves a dictionary value

# A method belongs to an object or class.
# A built-in function is called directly, for example len(items).