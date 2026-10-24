# 1. Creating a list (commonly used as an array in Python)
numbers = [10, 20, 30, 40, 50]

print("=== Creating a List ===")
print(numbers)
print(type(numbers))

# 2. Accessing array elements using indexes
print("\n=== Accessing Elements ===")
print(numbers[0])    # First element
print(numbers[1])    # Second element
print(numbers[-1])   # Last element
print(numbers[-2])   # Second-to-last element

# 3. Updating array elements
print("\n=== Updating Elements ===")
numbers[0] = 100
numbers[2] = 300
print(numbers)

# 4. Getting the length of an array
print("\n=== Array Length ===")
print(len(numbers))

# 5. Adding elements
print("\n=== Adding Elements ===")
numbers.append(60)          # Add one element at the end
print(numbers)

numbers.insert(1, 15)       # Insert at index 1
print(numbers)

numbers.extend([70, 80])    # Add multiple elements
print(numbers)

# 6. Removing elements
print("\n=== Removing Elements ===")
numbers.remove(300)         # Remove the first matching value
print(numbers)

numbers.pop()               # Remove the last element
print(numbers)

numbers.pop(0)              # Remove element at index 0
print(numbers)

# 7. Slicing arrays
print("\n=== Array Slicing ===")
values = [10, 20, 30, 40, 50, 60]

print(values[1:4])          # Index 1 through 3
print(values[:3])           # First three elements
print(values[3:])           # From index 3 to the end
print(values[::2])          # Every second element
print(values[::-1])         # Reverse order

# 8. Looping through an array
print("\n=== Looping Through Elements ===")
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)

# 9. Looping with indexes
print("\n=== Looping With Indexes ===")
for index, fruit in enumerate(fruits):
    print(index, fruit)

# 10. Searching for elements
print("\n=== Searching ===")
numbers = [10, 20, 30, 20, 40]

print(30 in numbers)
print(100 in numbers)
print(numbers.index(20))
print(numbers.count(20))

# 11. Sorting and reversing
print("\n=== Sorting and Reversing ===")
numbers = [50, 10, 40, 20, 30]

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

numbers.reverse()
print(numbers)

# sorted() returns a new sorted list
original = [3, 1, 2]
sorted_numbers = sorted(original)

print("Original:", original)
print("Sorted:", sorted_numbers)

# 12. Mathematical operations
print("\n=== Mathematical Operations ===")
numbers = [10, 20, 30, 40, 50]

print("Total:", sum(numbers))
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Length:", len(numbers))
print("Average:", sum(numbers) / len(numbers))

# 13. Combining arrays
print("\n=== Combining Arrays ===")
first = [1, 2, 3]
second = [4, 5, 6]

combined = first + second
print(combined)

repeated = first * 3
print(repeated)

# 14. Copying arrays
print("\n=== Copying Arrays ===")
original = [10, 20, 30]
copied = original.copy()

copied[0] = 999

print("Original:", original)
print("Copied:", copied)

# 15. Important: lists can contain mixed data types
print("\n=== Mixed Data Types ===")
mixed = [10, "Python", 3.14, True]

print(mixed)
print(mixed[0])
print(mixed[1])
print(mixed[2])
print(mixed[3])

# 16. List comprehension
print("\n=== List Comprehension ===")
numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]
print("Squares:", squares)

evens = [number for number in numbers if number % 2 == 0]
print("Even numbers:", evens)

# 17. Two-dimensional arrays (nested lists)
print("\n=== Two-Dimensional Lists ===")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)
print(matrix[0])
print(matrix[1][2])

matrix[0][0] = 100
print(matrix)

for row in matrix:
    for value in row:
        print(value, end=" ")
    print()

# 18. Creating a typed array using the array module
print("\n=== Typed Array ===")
from array import array

typed_numbers = array("i", [10, 20, 30, 40])

print(typed_numbers)
print(typed_numbers[0])
print(type(typed_numbers))

typed_numbers.append(50)
typed_numbers[1] = 200

print(typed_numbers)

# "i" represents a signed integer type.
# All elements must be compatible with that type.

# 19. Converting between lists and typed arrays
print("\n=== Conversion ===")
my_list = [1, 2, 3, 4]
my_array = array("i", my_list)

print("Array:", my_array)
print("List:", list(my_array))

# 20. Practical example: student scores
print("\n=== Student Scores ===")
scores = [85, 90, 78, 92, 88]

print("Scores:", scores)
print("Number of scores:", len(scores))
print("Total:", sum(scores))
print("Average:", sum(scores) / len(scores))
print("Highest:", max(scores))
print("Lowest:", min(scores))

scores.append(95)
print("After adding a score:", scores)

scores.sort()
print("Sorted scores:", scores)

# 21. Practical example: shopping cart
print("\n=== Shopping Cart ===")
prices = [100, 250, 75]
quantities = [2, 1, 3]

total = 0

for index in range(len(prices)):
    total += prices[index] * quantities[index]

print("Prices:", prices)
print("Quantities:", quantities)
print("Total cost:", total)