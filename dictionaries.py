# 1. Creating a dictionary
student = {
    "name": "Abebe",
    "age": 20,
    "city": "Addis Ababa"
}

print("=== Creating a Dictionary ===")
print(student)
print(type(student))

# 2. Accessing values using keys
print("\n=== Accessing Values ===")
print(student["name"])
print(student["age"])
print(student["city"])

# get() safely accesses a key that may not exist
print(student.get("grade"))
print(student.get("grade", "Not assigned"))

# student["grade"] would raise KeyError because the key does not exist

# 3. Adding new key-value pairs
print("\n=== Adding Items ===")
student["grade"] = "A"
student["is_student"] = True
print(student)

# 4. Updating existing values
print("\n=== Updating Values ===")
student["age"] = 21
student["city"] = "Bahir Dar"
print(student)

# update() adds or updates multiple items
student.update({"age": 22, "country": "Ethiopia"})
print(student)

# 5. Dictionary keys must be unique
print("\n=== Unique Keys ===")
person = {
    "name": "Abebe",
    "age": 20,
    "age": 25
}
print(person)  # The last value for "age" wins

# 6. Getting all keys, values, and items
print("\n=== Keys, Values, and Items ===")
print(student.keys())
print(student.values())
print(student.items())

# Convert dictionary views to lists
print(list(student.keys()))
print(list(student.values()))
print(list(student.items()))

# 7. Checking whether a key exists
print("\n=== Checking Keys ===")
print("name" in student)
print("email" in student)
print("age" not in student)

# 8. Removing items
print("\n=== Removing Items ===")
person = {"name": "Hana", "age": 19, "city": "Hawassa"}

del person["age"]
print(person)

removed_city = person.pop("city")
print("Removed:", removed_city)
print(person)

last_item = person.popitem()
print("Last item:", last_item)
print(person)

# clear() removes all items
person.clear()
print("Cleared:", person)

# 9. Getting the dictionary length
print("\n=== Dictionary Length ===")
product = {"name": "Laptop", "price": 50000, "stock": 10}
print(len(product))

# 10. Looping through dictionary keys
print("\n=== Looping Through Keys ===")
student = {"name": "Abebe", "age": 20, "grade": "A"}

for key in student:
    print(key)

# 11. Looping through values
print("\n=== Looping Through Values ===")
for value in student.values():
    print(value)

# 12. Looping through keys and values
print("\n=== Looping Through Items ===")
for key, value in student.items():
    print(f"{key}: {value}")

# 13. Dictionaries with different data types
print("\n=== Different Data Types ===")
data = {
    "name": "Abebe",
    "age": 20,
    "height": 1.75,
    "is_student": True,
    "skills": ["Python", "HTML"],
    "address": None
}
print(data)

# 14. Nested dictionaries
print("\n=== Nested Dictionaries ===")
students = {
    "student1": {
        "name": "Abebe",
        "age": 20
    },
    "student2": {
        "name": "Hana",
        "age": 21
    }
}

print(students)
print(students["student1"]["name"])
print(students["student2"]["age"])

# Updating a nested dictionary
students["student1"]["age"] = 22
print(students["student1"])

# Adding a new nested item
students["student2"]["grade"] = "A"
print(students["student2"])

# 15. Dictionary methods: setdefault()
print("\n=== setdefault() ===")
settings = {"theme": "dark"}

settings.setdefault("language", "English")
settings.setdefault("theme", "light")

print(settings)  # Existing theme remains unchanged

# 16. Creating a dictionary with fromkeys()
print("\n=== fromkeys() ===")
keys = ["name", "age", "city"]
new_student = dict.fromkeys(keys, "Unknown")
print(new_student)

# 17. Copying dictionaries
print("\n=== Copying Dictionaries ===")
original = {"name": "Abebe", "age": 20}
copied = original.copy()

copied["age"] = 25

print("Original:", original)
print("Copied:", copied)

# 18. Combining dictionaries
print("\n=== Combining Dictionaries ===")
first = {"name": "Abebe", "age": 20}
second = {"city": "Addis Ababa", "age": 21}

combined = first | second
print(combined)  # Values from second win on duplicate keys

# update() also combines dictionaries by modifying the target
first.update(second)
print(first)

# 19. Dictionary comprehension
print("\n=== Dictionary Comprehension ===")
numbers = [1, 2, 3, 4, 5]

squares = {number: number ** 2 for number in numbers}
print(squares)

# Filter items with a condition
even_squares = {
    number: number ** 2
    for number in numbers
    if number % 2 == 0
}
print(even_squares)

# 20. Calculating from dictionary values
print("\n=== Calculations ===")
scores = {
    "Math": 85,
    "Python": 90,
    "English": 80
}

print("Total:", sum(scores.values()))
print("Average:", sum(scores.values()) / len(scores))
print("Highest:", max(scores.values()))
print("Lowest:", min(scores.values()))

# Find the subject with the highest score
best_subject = max(scores, key=scores.get)
print("Best subject:", best_subject)

# 21. Sorting dictionaries
print("\n=== Sorting Dictionaries ===")
prices = {"Banana": 20, "Apple": 50, "Orange": 30}

print("Sorted by key:", dict(sorted(prices.items())))
print(
    "Sorted by value:",
    dict(sorted(prices.items(), key=lambda item: item[1]))
)

# 22. Dictionary keys and mutability
print("\n=== Valid Dictionary Keys ===")
valid_keys = {
    "name": "Abebe",
    1: "One",
    (10, 20): "Coordinates"
}
print(valid_keys)
print(valid_keys[(10, 20)])

# Lists cannot be dictionary keys because they are mutable.
# invalid = {[1, 2]: "value"}  # TypeError

# 23. Practical example: inventory management
print("\n=== Inventory Management ===")
inventory = {
    "laptop": {"price": 50000, "quantity": 5},
    "phone": {"price": 15000, "quantity": 10},
    "mouse": {"price": 500, "quantity": 20}
}

print("Laptop price:", inventory["laptop"]["price"])

# Update inventory
inventory["laptop"]["quantity"] -= 1
inventory["keyboard"] = {"price": 1200, "quantity": 8}

print("Updated inventory:", inventory)

# Calculate the total inventory value
total_value = sum(
    item["price"] * item["quantity"]
    for item in inventory.values()
)
print("Total inventory value:", total_value)

# 24. Practical example: student records
print("\n=== Student Records ===")
students = {
    101: {"name": "Abebe", "scores": [85, 90, 95]},
    102: {"name": "Hana", "scores": [80, 88, 92]},
    103: {"name": "Kebede", "scores": [75, 85, 90]}
}

for student_id, info in students.items():
    average = sum(info["scores"]) / len(info["scores"])
    print(f"ID: {student_id}")
    print(f"Name: {info['name']}")
    print(f"Average: {average:.2f}")

# Add a new student
students[104] = {"name": "Sara", "scores": [90, 95, 98]}
print("Number of students:", len(students))