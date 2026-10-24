# 1. Integer (int)
age = 20
year = 2026
temperature = -5

print("=== Integer ===")
print(age)
print(year)
print(temperature)
print(type(age))

# 2. Float (float)
price = 99.99
height = 1.75
percentage = 85.5

print("\n=== Float ===")
print(price)
print(height)
print(percentage)
print(type(price))

# 3. String (str)
name = "Abebe"
country = "Ethiopia"
message = "Python is easy to learn"

print("\n=== String ===")
print(name)
print(country)
print(message)
print(type(name))
print("First character:", name[0])
print("Length:", len(name))
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())

# 4. Boolean (bool)
is_student = True
is_employed = False

print("\n=== Boolean ===")
print(is_student)
print(is_employed)
print(type(is_student))
print("AND:", True and False)
print("OR:", True or False)
print("NOT:", not True)

# 5. List (list) - ordered and mutable
fruits = ["apple", "banana", "orange"]

print("\n=== List ===")
print(fruits)
print(fruits[0])
print(fruits[-1])

fruits.append("mango")
print("After append:", fruits)

fruits[0] = "grape"
print("After update:", fruits)

fruits.remove("banana")
print("After remove:", fruits)
print(type(fruits))

# 6. Tuple (tuple) - ordered and immutable
colors = ("red", "green", "blue")

print("\n=== Tuple ===")
print(colors)
print(colors[0])
print(len(colors))
print(type(colors))

# colors[0] = "black"  # TypeError: tuples cannot be changed

# 7. Range (range) - sequence of integers
numbers = range(1, 6)

print("\n=== Range ===")
print(list(numbers))
print(type(numbers))

# 8. Dictionary (dict) - key-value pairs
student = {
    "name": "Abebe",
    "age": 20,
    "grade": "A"
}

print("\n=== Dictionary ===")
print(student)
print(student["name"])
print(student["age"])

student["age"] = 21
student["city"] = "Addis Ababa"

print("After update:", student)
print("Keys:", list(student.keys()))
print("Values:", list(student.values()))
print(type(student))

# 9. Set (set) - unique values, unordered
numbers_set = {1, 2, 3, 3, 4, 4}

print("\n=== Set ===")
print(numbers_set)  # Duplicates are removed
print(type(numbers_set))

numbers_set.add(5)
print("After add:", numbers_set)

numbers_set.discard(2)
print("After discard:", numbers_set)

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)

# 10. Frozenset - immutable set
fixed_numbers = frozenset([1, 2, 3, 3])

print("\n=== Frozenset ===")
print(fixed_numbers)
print(type(fixed_numbers))

# 11. NoneType - represents no value
result = None

print("\n=== NoneType ===")
print(result)
print(type(result))
print(result is None)

# 12. Complex numbers (complex)
complex_number = 3 + 4j

print("\n=== Complex ===")
print(complex_number)
print("Real part:", complex_number.real)
print("Imaginary part:", complex_number.imag)
print("Type:", type(complex_number))

# 13. Bytes (bytes) - immutable binary data
data = bytes([65, 66, 67])

print("\n=== Bytes ===")
print(data)
print(type(data))
print(data.decode())

# 14. Bytearray - mutable binary data
mutable_data = bytearray([65, 66, 67])

print("\n=== Bytearray ===")
print(mutable_data)
mutable_data[0] = 90
print(mutable_data)
print(mutable_data.decode())
print(type(mutable_data))

# 15. Memoryview - view of binary data
binary_data = bytes([10, 20, 30])
view = memoryview(binary_data)

print("\n=== Memoryview ===")
print(view[0])
print(list(view))
print(type(view))

# 16. Type conversion
print("\n=== Type Conversion ===")
number_text = "100"
decimal_text = "25.5"

print(int(number_text))
print(float(decimal_text))
print(str(500))
print(bool(1))
print(list((1, 2, 3)))
print(tuple([1, 2, 3]))
print(set([1, 1, 2, 3]))

# 17. Checking types
print("\n=== Type Checking ===")
value = 10

print(type(value))
print(isinstance(value, int))
print(isinstance(value, float))
print(isinstance(value, (int, float)))

# 18. Mutable vs immutable examples
print("\n=== Mutable vs Immutable ===")

# Lists are mutable
my_list = [1, 2, 3]
my_list[0] = 100
print("Changed list:", my_list)

# Strings are immutable
my_string = "Python"
my_string = "J" + my_string[1:]
print("New string:", my_string)

# Integers are immutable
my_number = 10
my_number = my_number + 5
print("New number:", my_number)

# 19. Truthy and falsy values
print("\n=== Truthy and Falsy ===")
print(bool(0))
print(bool(1))
print(bool(""))
print(bool("Python"))
print(bool([]))
print(bool([1, 2]))
print(bool(None))

# 20. Practical example combining data types
print("\n=== Practical Example ===")

student_info = {
    "name": "Abebe",
    "age": 20,
    "scores": [85, 90, 95],
    "is_enrolled": True,
    "address": None
}

average = sum(student_info["scores"]) / len(student_info["scores"])

print("Name:", student_info["name"])
print("Age:", student_info["age"])
print("Scores:", student_info["scores"])
print("Average:", average)
print("Enrolled:", student_info["is_enrolled"])
print("Address:", student_info["address"])
print("Student data type:", type(student_info))