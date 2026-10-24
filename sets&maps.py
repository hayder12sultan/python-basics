# ============================================================
# PART 1: PYTHON SETS
# ============================================================

# 1. CREATING SETS

numbers = {1, 2, 3, 4, 5}
fruits = {"apple", "banana", "orange"}
empty_set = set()
empty_dict = {}

print(numbers)
# Output: {1, 2, 3, 4, 5}

print(empty_set)
# Output: set()

print(type(empty_set))
# Output: <class 'set'>

print(type(empty_dict))
# Output: <class 'dict'>

# Note: {} creates an empty dictionary, not an empty set.


# ============================================================
# 2. SETS AUTOMATICALLY REMOVE DUPLICATES
# ============================================================

numbers = {1, 2, 2, 3, 3, 4}

print(numbers)
# Output: {1, 2, 3, 4}
# Set display order is not guaranteed for general sets.

names = ["Sara", "Abebe", "Sara", "Mimi"]
unique_names = set(names)

print(unique_names)
# Output: A set containing 'Sara', 'Abebe', and 'Mimi'.


# ============================================================
# 3. CONVERTING LISTS AND TUPLES TO SETS
# ============================================================

my_list = [10, 20, 20, 30, 30, 40]
my_tuple = (1, 2, 2, 3)

print(set(my_list))
# Output: {10, 20, 30, 40}

print(set(my_tuple))
# Output: {1, 2, 3}


# ============================================================
# 4. ADDING ELEMENTS
# ============================================================

colors = {"red", "blue"}

colors.add("green")
print(colors)
# Output: A set containing 'red', 'blue', and 'green'.

colors.update(["yellow", "black"])
print(colors)
# Output: A set containing red, blue, green, yellow, black.

# add() adds one element.
# update() adds elements from an iterable.


# ============================================================
# 5. REMOVING ELEMENTS
# ============================================================

numbers = {10, 20, 30, 40}

numbers.remove(20)
print(numbers)
# Output: {10, 30, 40}

numbers.discard(100)
print(numbers)
# Output: {10, 30, 40}
# discard() does not raise an error if the item is absent.

removed = numbers.pop()
print(removed)
# Output: An arbitrary element from the set.

numbers.clear()
print(numbers)
# Output: set()

# remove(x) raises KeyError if x is missing.
# pop() removes an arbitrary element, not a guaranteed first item.


# ============================================================
# 6. CHECKING MEMBERSHIP
# ============================================================

fruits = {"apple", "banana", "orange"}

print("apple" in fruits)
# Output: True

print("grape" in fruits)
# Output: False

print("grape" not in fruits)
# Output: True


# ============================================================
# 7. SET LENGTH AND LOOPS
# ============================================================

numbers = {10, 20, 30}

print(len(numbers))
# Output: 3

for number in numbers:
    print(number)

# Output: 10, 20, and 30, in no guaranteed order.


# ============================================================
# 8. SET UNION
# Combine all unique elements.
# ============================================================

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)
# Output: {1, 2, 3, 4, 5}

print(a.union(b))
# Output: {1, 2, 3, 4, 5}


# ============================================================
# 9. SET INTERSECTION
# Get elements shared by both sets.
# ============================================================

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a & b)
# Output: {3, 4}

print(a.intersection(b))
# Output: {3, 4}


# ============================================================
# 10. SET DIFFERENCE
# Get elements in one set but not the other.
# ============================================================

a = {1, 2, 3, 4}
b = {3, 4, 5}

print(a - b)
# Output: {1, 2}

print(b - a)
# Output: {5}

print(a.difference(b))
# Output: {1, 2}


# ============================================================
# 11. SYMMETRIC DIFFERENCE
# Get elements in either set, but not both.
# ============================================================

a = {1, 2, 3}
b = {3, 4, 5}

print(a ^ b)
# Output: {1, 2, 4, 5}

print(a.symmetric_difference(b))
# Output: {1, 2, 4, 5}


# ============================================================
# 12. SUBSETS AND SUPERSETS
# ============================================================

a = {1, 2}
b = {1, 2, 3, 4}

print(a.issubset(b))
# Output: True

print(b.issuperset(a))
# Output: True

print(a <= b)
# Output: True

print(b >= a)
# Output: True

print(a < b)
# Output: True
# Proper subset: a is a subset of b, and a != b.


# ============================================================
# 13. DISJOINT SETS
# Sets with no common elements.
# ============================================================

a = {1, 2}
b = {3, 4}

print(a.isdisjoint(b))
# Output: True

c = {2, 3}

print(a.isdisjoint(c))
# Output: False


# ============================================================
# 14. UPDATE SETS IN PLACE
# ============================================================

a = {1, 2, 3}
b = {3, 4, 5}

a |= b
print(a)
# Output: {1, 2, 3, 4, 5}

a = {1, 2, 3}
a &= {2, 3, 4}
print(a)
# Output: {2, 3}

a = {1, 2, 3}
a -= {2}
print(a)
# Output: {1, 3}

a = {1, 2, 3}
a ^= {3, 4}
print(a)
# Output: {1, 2, 4}


# ============================================================
# 15. SET COMPREHENSIONS
# ============================================================

squares = {number ** 2 for number in range(1, 6)}
print(squares)
# Output: {1, 4, 9, 16, 25}

even_numbers = {
    number for number in range(1, 11)
    if number % 2 == 0
}
print(even_numbers)
# Output: {2, 4, 6, 8, 10}


# ============================================================
# 16. FROZEN SETS
# Immutable sets that cannot be changed after creation.
# ============================================================

fixed_numbers = frozenset([1, 2, 3, 3])

print(fixed_numbers)
# Output: frozenset({1, 2, 3})

print(2 in fixed_numbers)
# Output: True

# fixed_numbers.add(4)
# Raises AttributeError because frozensets are immutable.


# ============================================================
# 17. REMOVING DUPLICATES WHILE PRESERVING ORDER
# ============================================================

numbers = [3, 1, 3, 2, 1, 4]

unique_numbers = list(dict.fromkeys(numbers))

print(unique_numbers)
# Output: [3, 1, 2, 4]

# Use this approach when original order matters.
# Converting directly to a set does not preserve a reliable order.


# ============================================================
# PART 2: PYTHON DICTIONARIES (MAPS)
# ============================================================

# 18. CREATING DICTIONARIES

student = {
    "name": "Sara",
    "age": 22,
    "city": "Addis Ababa"
}

print(student)
# Output: {'name': 'Sara', 'age': 22, 'city': 'Addis Ababa'}

empty_map = {}
another_empty_map = dict()

print(type(empty_map))
# Output: <class 'dict'>


# ============================================================
# 19. ACCESSING VALUES
# ============================================================

student = {"name": "Abebe", "age": 20}

print(student["name"])
# Output: Abebe

print(student["age"])
# Output: 20

print(student.get("city"))
# Output: None

print(student.get("city", "Unknown"))
# Output: Unknown

# [] raises KeyError if the key is absent.
# get() returns None or a supplied default instead.


# ============================================================
# 20. ADDING AND UPDATING VALUES
# ============================================================

student = {"name": "Sara", "age": 22}

student["city"] = "Adama"
print(student)
# Output: {'name': 'Sara', 'age': 22, 'city': 'Adama'}

student["age"] = 23
print(student["age"])
# Output: 23

student.update({"age": 24, "country": "Ethiopia"})
print(student)
# Output: {'name': 'Sara', 'age': 24, 'city': 'Adama',
#          'country': 'Ethiopia'}


# ============================================================
# 21. REMOVING DICTIONARY ITEMS
# ============================================================

student = {"name": "Sara", "age": 22, "city": "Adama"}

del student["age"]
print(student)
# Output: {'name': 'Sara', 'city': 'Adama'}

city = student.pop("city")
print(city)
# Output: Adama

print(student)
# Output: {'name': 'Sara'}

student["age"] = 22
last_item = student.popitem()
print(last_item)
# Output: ('age', 22)
# popitem() removes the last inserted key-value pair.

student.clear()
print(student)
# Output: {}


# ============================================================
# 22. DICTIONARY KEYS, VALUES, AND ITEMS
# ============================================================

student = {"name": "Abebe", "age": 20, "city": "Hawassa"}

print(list(student.keys()))
# Output: ['name', 'age', 'city']

print(list(student.values()))
# Output: ['Abebe', 20, 'Hawassa']

print(list(student.items()))
# Output: [('name', 'Abebe'), ('age', 20), ('city', 'Hawassa')]


# ============================================================
# 23. LOOPING THROUGH DICTIONARIES
# ============================================================

student = {"name": "Sara", "age": 22}

for key in student:
    print(key)

# Output:
# name
# age

for value in student.values():
    print(value)

# Output:
# Sara
# 22

for key, value in student.items():
    print(key, value)

# Output:
# name Sara
# age 22


# ============================================================
# 24. CHECKING KEY MEMBERSHIP
# ============================================================

student = {"name": "Sara", "age": 22}

print("name" in student)
# Output: True

print("Sara" in student)
# Output: False

print("Sara" in student.values())
# Output: True

print("city" not in student)
# Output: True


# ============================================================
# 25. DICTIONARY COMPREHENSIONS
# ============================================================

squares = {
    number: number ** 2
    for number in range(1, 6)
}

print(squares)
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

even_squares = {
    number: number ** 2
    for number in range(1, 11)
    if number % 2 == 0
}

print(even_squares)
# Output: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}


# ============================================================
# 26. MERGING DICTIONARIES
# Python 3.9+
# ============================================================

first = {"name": "Sara", "age": 22}
second = {"age": 23, "city": "Adama"}

merged = first | second

print(merged)
# Output: {'name': 'Sara', 'age': 23, 'city': 'Adama'}

first |= second
print(first)
# Output: {'name': 'Sara', 'age': 23, 'city': 'Adama'}

# Duplicate keys take the value from the right-hand mapping.


# ============================================================
# 27. NESTED DICTIONARIES
# ============================================================

school = {
    "student1": {"name": "Sara", "grade": 90},
    "student2": {"name": "Abebe", "grade": 85}
}

print(school["student1"]["name"])
# Output: Sara

print(school["student2"]["grade"])
# Output: 85

school["student1"]["grade"] = 95

print(school["student1"]["grade"])
# Output: 95


# ============================================================
# 28. DICTIONARY WITH LIST VALUES
# ============================================================

classroom = {
    "students": ["Sara", "Abebe", "Mimi"],
    "subjects": ["Python", "Math"]
}

classroom["students"].append("Dawit")

print(classroom["students"])
# Output: ['Sara', 'Abebe', 'Mimi', 'Dawit']


# ============================================================
# 29. DICTIONARY FROM TWO LISTS
# ============================================================

keys = ["name", "age", "city"]
values = ["Sara", 22, "Adama"]

student = dict(zip(keys, values))

print(student)
# Output: {'name': 'Sara', 'age': 22, 'city': 'Adama'}


# ============================================================
# 30. DICTIONARY FROM KEY-VALUE PAIRS
# ============================================================

pairs = [
    ("name", "Abebe"),
    ("age", 20),
    ("country", "Ethiopia")
]

person = dict(pairs)

print(person)
# Output: {'name': 'Abebe', 'age': 20, 'country': 'Ethiopia'}


# ============================================================
# 31. SET DEFAULT
# Add a key only if it does not already exist.
# ============================================================

student = {"name": "Sara"}

student.setdefault("age", 22)
student.setdefault("name", "Mimi")

print(student)
# Output: {'name': 'Sara', 'age': 22}


# ============================================================
# 32. DICTIONARY COPY
# ============================================================

original = {"name": "Sara", "scores": [80, 90]}

shallow_copy = original.copy()

shallow_copy["name"] = "Abebe"
shallow_copy["scores"].append(100)

print(original["name"])
# Output: Sara

print(original["scores"])
# Output: [80, 90, 100]

# A shallow copy shares nested mutable objects.
# Use copy.deepcopy() when a fully independent nested copy is needed.


# ============================================================
# 33. COUNTING ITEMS WITH A DICTIONARY
# ============================================================

words = ["apple", "banana", "apple", "orange", "banana", "apple"]

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)
# Output: {'apple': 3, 'banana': 2, 'orange': 1}


# ============================================================
# 34. SETS AND DICTIONARIES: DIFFERENCES
# ============================================================

unique_ids = {101, 102, 103}

user = {
    "id": 101,
    "name": "Sara"
}

print(101 in unique_ids)
# Output: True

print(user["name"])
# Output: Sara

# Set: unique elements.
# Dictionary: key-value pairs.
# Dictionary keys must be hashable; values can be any type.


# ============================================================
# PART 3: THE map() BUILT-IN FUNCTION
# ============================================================

# 35. BASIC map()
# Apply a function to each item.

def double(number):
    return number * 2

numbers = [1, 2, 3, 4]

result = map(double, numbers)

print(list(result))
# Output: [2, 4, 6, 8]


# ============================================================
# 36. map() WITH LAMBDA
# ============================================================

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda number: number ** 2, numbers))

print(squares)
# Output: [1, 4, 9, 16, 25]


# ============================================================
# 37. map() WITH MULTIPLE ITERABLES
# ============================================================

a = [1, 2, 3]
b = [10, 20, 30]

result = list(map(lambda x, y: x + y, a, b))

print(result)
# Output: [11, 22, 33]

# map() stops when the shortest iterable is exhausted.


# ============================================================
# 38. map() WITH STRINGS
# ============================================================

names = ["sara", "abebe", "mimi"]

capitalized = list(map(str.title, names))

print(capitalized)
# Output: ['Sara', 'Abebe', 'Mimi']


# ============================================================
# 39. map() TO CONVERT DATA TYPES
# ============================================================

values = ["10", "20", "30"]

numbers = list(map(int, values))

print(numbers)
# Output: [10, 20, 30]


# ============================================================
# 40. map() WITH DICTIONARY VALUES
# ============================================================

prices = {"apple": 10, "banana": 20, "orange": 30}

discounted_prices = dict(
    map(
        lambda item: (item[0], item[1] * 0.9),
        prices.items()
    )
)

print(discounted_prices)
# Output: {'apple': 9.0, 'banana': 18.0, 'orange': 27.0}


# ============================================================
# 41. map() RETURNS AN ITERATOR
# ============================================================

numbers = [1, 2, 3]

mapped = map(double, numbers)

print(next(mapped))
# Output: 2

print(next(mapped))
# Output: 4

print(list(mapped))
# Output: [6]

# Values already consumed with next() are not returned again.


# ============================================================
# PART 4: PRACTICAL EXAMPLES
# ============================================================

# 42. FINDING COMMON STUDENTS IN TWO COURSES

python_students = {"Sara", "Abebe", "Mimi"}
java_students = {"Mimi", "Dawit", "Sara"}

print(python_students & java_students)
# Output: {'Sara', 'Mimi'} (order may vary)


# ============================================================
# 43. FINDING STUDENTS ENROLLED IN EITHER COURSE
# ============================================================

all_students = python_students | java_students

print(all_students)
# Output: A set containing Sara, Abebe, Mimi, and Dawit.


# ============================================================
# 44. INVENTORY USING A DICTIONARY
# ============================================================

inventory = {
    "laptop": 5,
    "mouse": 20,
    "keyboard": 10
}

inventory["mouse"] -= 2
inventory["monitor"] = 4

print(inventory["mouse"])
# Output: 18

print(inventory["monitor"])
# Output: 4


# ============================================================
# 45. REMOVING DUPLICATE RECORDS
# ============================================================

emails = [
    "a@example.com",
    "b@example.com",
    "a@example.com",
    "c@example.com"
]

unique_emails = set(emails)

print(len(unique_emails))
# Output: 3


# ============================================================
# 46. GROUPING VALUES WITH A DICTIONARY
# ============================================================

scores = [
    ("Sara", 90),
    ("Abebe", 80),
    ("Sara", 95),
    ("Abebe", 85)
]

grouped_scores = {}

for name, score in scores:
    grouped_scores.setdefault(name, []).append(score)

print(grouped_scores)
# Output: {'Sara': [90, 95], 'Abebe': [80, 85]}


# ============================================================
# 47. FILTERING A DICTIONARY
# ============================================================

scores = {
    "Sara": 90,
    "Abebe": 45,
    "Mimi": 75,
    "Dawit": 35
}

passed = {
    name: score
    for name, score in scores.items()
    if score >= 50
}

print(passed)
# Output: {'Sara': 90, 'Mimi': 75}


# ============================================================
# END OF SETS, DICTIONARIES, AND map() EXAMPLES
# ============================================================# ============================================================
# PART 1: PYTHON SETS
# ============================================================

# 1. CREATING SETS

numbers = {1, 2, 3, 4, 5}
fruits = {"apple", "banana", "orange"}
empty_set = set()
empty_dict = {}

print(numbers)
# Output: {1, 2, 3, 4, 5}

print(empty_set)
# Output: set()

print(type(empty_set))
# Output: <class 'set'>

print(type(empty_dict))
# Output: <class 'dict'>

# Note: {} creates an empty dictionary, not an empty set.


# ============================================================
# 2. SETS AUTOMATICALLY REMOVE DUPLICATES
# ============================================================

numbers = {1, 2, 2, 3, 3, 4}

print(numbers)
# Output: {1, 2, 3, 4}
# Set display order is not guaranteed for general sets.

names = ["Sara", "Abebe", "Sara", "Mimi"]
unique_names = set(names)

print(unique_names)
# Output: A set containing 'Sara', 'Abebe', and 'Mimi'.


# ============================================================
# 3. CONVERTING LISTS AND TUPLES TO SETS
# ============================================================

my_list = [10, 20, 20, 30, 30, 40]
my_tuple = (1, 2, 2, 3)

print(set(my_list))
# Output: {10, 20, 30, 40}

print(set(my_tuple))
# Output: {1, 2, 3}


# ============================================================
# 4. ADDING ELEMENTS
# ============================================================

colors = {"red", "blue"}

colors.add("green")
print(colors)
# Output: A set containing 'red', 'blue', and 'green'.

colors.update(["yellow", "black"])
print(colors)
# Output: A set containing red, blue, green, yellow, black.

# add() adds one element.
# update() adds elements from an iterable.


# ============================================================
# 5. REMOVING ELEMENTS
# ============================================================

numbers = {10, 20, 30, 40}

numbers.remove(20)
print(numbers)
# Output: {10, 30, 40}

numbers.discard(100)
print(numbers)
# Output: {10, 30, 40}
# discard() does not raise an error if the item is absent.

removed = numbers.pop()
print(removed)
# Output: An arbitrary element from the set.

numbers.clear()
print(numbers)
# Output: set()

# remove(x) raises KeyError if x is missing.
# pop() removes an arbitrary element, not a guaranteed first item.


# ============================================================
# 6. CHECKING MEMBERSHIP
# ============================================================

fruits = {"apple", "banana", "orange"}

print("apple" in fruits)
# Output: True

print("grape" in fruits)
# Output: False

print("grape" not in fruits)
# Output: True


# ============================================================
# 7. SET LENGTH AND LOOPS
# ============================================================

numbers = {10, 20, 30}

print(len(numbers))
# Output: 3

for number in numbers:
    print(number)

# Output: 10, 20, and 30, in no guaranteed order.


# ============================================================
# 8. SET UNION
# Combine all unique elements.
# ============================================================

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)
# Output: {1, 2, 3, 4, 5}

print(a.union(b))
# Output: {1, 2, 3, 4, 5}


# ============================================================
# 9. SET INTERSECTION
# Get elements shared by both sets.
# ============================================================

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a & b)
# Output: {3, 4}

print(a.intersection(b))
# Output: {3, 4}


# ============================================================
# 10. SET DIFFERENCE
# Get elements in one set but not the other.
# ============================================================

a = {1, 2, 3, 4}
b = {3, 4, 5}

print(a - b)
# Output: {1, 2}

print(b - a)
# Output: {5}

print(a.difference(b))
# Output: {1, 2}


# ============================================================
# 11. SYMMETRIC DIFFERENCE
# Get elements in either set, but not both.
# ============================================================

a = {1, 2, 3}
b = {3, 4, 5}

print(a ^ b)
# Output: {1, 2, 4, 5}

print(a.symmetric_difference(b))
# Output: {1, 2, 4, 5}


# ============================================================
# 12. SUBSETS AND SUPERSETS
# ============================================================

a = {1, 2}
b = {1, 2, 3, 4}

print(a.issubset(b))
# Output: True

print(b.issuperset(a))
# Output: True

print(a <= b)
# Output: True

print(b >= a)
# Output: True

print(a < b)
# Output: True
# Proper subset: a is a subset of b, and a != b.


# ============================================================
# 13. DISJOINT SETS
# Sets with no common elements.
# ============================================================

a = {1, 2}
b = {3, 4}

print(a.isdisjoint(b))
# Output: True

c = {2, 3}

print(a.isdisjoint(c))
# Output: False


# ============================================================
# 14. UPDATE SETS IN PLACE
# ============================================================

a = {1, 2, 3}
b = {3, 4, 5}

a |= b
print(a)
# Output: {1, 2, 3, 4, 5}

a = {1, 2, 3}
a &= {2, 3, 4}
print(a)
# Output: {2, 3}

a = {1, 2, 3}
a -= {2}
print(a)
# Output: {1, 3}

a = {1, 2, 3}
a ^= {3, 4}
print(a)
# Output: {1, 2, 4}


# ============================================================
# 15. SET COMPREHENSIONS
# ============================================================

squares = {number ** 2 for number in range(1, 6)}
print(squares)
# Output: {1, 4, 9, 16, 25}

even_numbers = {
    number for number in range(1, 11)
    if number % 2 == 0
}
print(even_numbers)
# Output: {2, 4, 6, 8, 10}


# ============================================================
# 16. FROZEN SETS
# Immutable sets that cannot be changed after creation.
# ============================================================

fixed_numbers = frozenset([1, 2, 3, 3])

print(fixed_numbers)
# Output: frozenset({1, 2, 3})

print(2 in fixed_numbers)
# Output: True

# fixed_numbers.add(4)
# Raises AttributeError because frozensets are immutable.


# ============================================================
# 17. REMOVING DUPLICATES WHILE PRESERVING ORDER
# ============================================================

numbers = [3, 1, 3, 2, 1, 4]

unique_numbers = list(dict.fromkeys(numbers))

print(unique_numbers)
# Output: [3, 1, 2, 4]

# Use this approach when original order matters.
# Converting directly to a set does not preserve a reliable order.


# ============================================================
# PART 2: PYTHON DICTIONARIES (MAPS)
# ============================================================

# 18. CREATING DICTIONARIES

student = {
    "name": "Sara",
    "age": 22,
    "city": "Addis Ababa"
}

print(student)
# Output: {'name': 'Sara', 'age': 22, 'city': 'Addis Ababa'}

empty_map = {}
another_empty_map = dict()

print(type(empty_map))
# Output: <class 'dict'>


# ============================================================
# 19. ACCESSING VALUES
# ============================================================

student = {"name": "Abebe", "age": 20}

print(student["name"])
# Output: Abebe

print(student["age"])
# Output: 20

print(student.get("city"))
# Output: None

print(student.get("city", "Unknown"))
# Output: Unknown

# [] raises KeyError if the key is absent.
# get() returns None or a supplied default instead.


# ============================================================
# 20. ADDING AND UPDATING VALUES
# ============================================================

student = {"name": "Sara", "age": 22}

student["city"] = "Adama"
print(student)
# Output: {'name': 'Sara', 'age': 22, 'city': 'Adama'}

student["age"] = 23
print(student["age"])
# Output: 23

student.update({"age": 24, "country": "Ethiopia"})
print(student)
# Output: {'name': 'Sara', 'age': 24, 'city': 'Adama',
#          'country': 'Ethiopia'}


# ============================================================
# 21. REMOVING DICTIONARY ITEMS
# ============================================================

student = {"name": "Sara", "age": 22, "city": "Adama"}

del student["age"]
print(student)
# Output: {'name': 'Sara', 'city': 'Adama'}

city = student.pop("city")
print(city)
# Output: Adama

print(student)
# Output: {'name': 'Sara'}

student["age"] = 22
last_item = student.popitem()
print(last_item)
# Output: ('age', 22)
# popitem() removes the last inserted key-value pair.

student.clear()
print(student)
# Output: {}


# ============================================================
# 22. DICTIONARY KEYS, VALUES, AND ITEMS
# ============================================================

student = {"name": "Abebe", "age": 20, "city": "Hawassa"}

print(list(student.keys()))
# Output: ['name', 'age', 'city']

print(list(student.values()))
# Output: ['Abebe', 20, 'Hawassa']

print(list(student.items()))
# Output: [('name', 'Abebe'), ('age', 20), ('city', 'Hawassa')]


# ============================================================
# 23. LOOPING THROUGH DICTIONARIES
# ============================================================

student = {"name": "Sara", "age": 22}

for key in student:
    print(key)

# Output:
# name
# age

for value in student.values():
    print(value)

# Output:
# Sara
# 22

for key, value in student.items():
    print(key, value)

# Output:
# name Sara
# age 22


# ============================================================
# 24. CHECKING KEY MEMBERSHIP
# ============================================================

student = {"name": "Sara", "age": 22}

print("name" in student)
# Output: True

print("Sara" in student)
# Output: False

print("Sara" in student.values())
# Output: True

print("city" not in student)
# Output: True


# ============================================================
# 25. DICTIONARY COMPREHENSIONS
# ============================================================

squares = {
    number: number ** 2
    for number in range(1, 6)
}

print(squares)
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

even_squares = {
    number: number ** 2
    for number in range(1, 11)
    if number % 2 == 0
}

print(even_squares)
# Output: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}


# ============================================================
# 26. MERGING DICTIONARIES
# Python 3.9+
# ============================================================

first = {"name": "Sara", "age": 22}
second = {"age": 23, "city": "Adama"}

merged = first | second

print(merged)
# Output: {'name': 'Sara', 'age': 23, 'city': 'Adama'}

first |= second
print(first)
# Output: {'name': 'Sara', 'age': 23, 'city': 'Adama'}

# Duplicate keys take the value from the right-hand mapping.


# ============================================================
# 27. NESTED DICTIONARIES
# ============================================================

school = {
    "student1": {"name": "Sara", "grade": 90},
    "student2": {"name": "Abebe", "grade": 85}
}

print(school["student1"]["name"])
# Output: Sara

print(school["student2"]["grade"])
# Output: 85

school["student1"]["grade"] = 95

print(school["student1"]["grade"])
# Output: 95


# ============================================================
# 28. DICTIONARY WITH LIST VALUES
# ============================================================

classroom = {
    "students": ["Sara", "Abebe", "Mimi"],
    "subjects": ["Python", "Math"]
}

classroom["students"].append("Dawit")

print(classroom["students"])
# Output: ['Sara', 'Abebe', 'Mimi', 'Dawit']


# ============================================================
# 29. DICTIONARY FROM TWO LISTS
# ============================================================

keys = ["name", "age", "city"]
values = ["Sara", 22, "Adama"]

student = dict(zip(keys, values))

print(student)
# Output: {'name': 'Sara', 'age': 22, 'city': 'Adama'}


# ============================================================
# 30. DICTIONARY FROM KEY-VALUE PAIRS
# ============================================================

pairs = [
    ("name", "Abebe"),
    ("age", 20),
    ("country", "Ethiopia")
]

person = dict(pairs)

print(person)
# Output: {'name': 'Abebe', 'age': 20, 'country': 'Ethiopia'}


# ============================================================
# 31. SET DEFAULT
# Add a key only if it does not already exist.
# ============================================================

student = {"name": "Sara"}

student.setdefault("age", 22)
student.setdefault("name", "Mimi")

print(student)
# Output: {'name': 'Sara', 'age': 22}


# ============================================================
# 32. DICTIONARY COPY
# ============================================================

original = {"name": "Sara", "scores": [80, 90]}

shallow_copy = original.copy()

shallow_copy["name"] = "Abebe"
shallow_copy["scores"].append(100)

print(original["name"])
# Output: Sara

print(original["scores"])
# Output: [80, 90, 100]

# A shallow copy shares nested mutable objects.
# Use copy.deepcopy() when a fully independent nested copy is needed.


# ============================================================
# 33. COUNTING ITEMS WITH A DICTIONARY
# ============================================================

words = ["apple", "banana", "apple", "orange", "banana", "apple"]

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)
# Output: {'apple': 3, 'banana': 2, 'orange': 1}


# ============================================================
# 34. SETS AND DICTIONARIES: DIFFERENCES
# ============================================================

unique_ids = {101, 102, 103}

user = {
    "id": 101,
    "name": "Sara"
}

print(101 in unique_ids)
# Output: True

print(user["name"])
# Output: Sara

# Set: unique elements.
# Dictionary: key-value pairs.
# Dictionary keys must be hashable; values can be any type.


# ============================================================
# PART 3: THE map() BUILT-IN FUNCTION
# ============================================================

# 35. BASIC map()
# Apply a function to each item.

def double(number):
    return number * 2

numbers = [1, 2, 3, 4]

result = map(double, numbers)

print(list(result))
# Output: [2, 4, 6, 8]


# ============================================================
# 36. map() WITH LAMBDA
# ============================================================

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda number: number ** 2, numbers))

print(squares)
# Output: [1, 4, 9, 16, 25]


# ============================================================
# 37. map() WITH MULTIPLE ITERABLES
# ============================================================

a = [1, 2, 3]
b = [10, 20, 30]

result = list(map(lambda x, y: x + y, a, b))

print(result)
# Output: [11, 22, 33]

# map() stops when the shortest iterable is exhausted.


# ============================================================
# 38. map() WITH STRINGS
# ============================================================

names = ["sara", "abebe", "mimi"]

capitalized = list(map(str.title, names))

print(capitalized)
# Output: ['Sara', 'Abebe', 'Mimi']


# ============================================================
# 39. map() TO CONVERT DATA TYPES
# ============================================================

values = ["10", "20", "30"]

numbers = list(map(int, values))

print(numbers)
# Output: [10, 20, 30]


# ============================================================
# 40. map() WITH DICTIONARY VALUES
# ============================================================

prices = {"apple": 10, "banana": 20, "orange": 30}

discounted_prices = dict(
    map(
        lambda item: (item[0], item[1] * 0.9),
        prices.items()
    )
)

print(discounted_prices)
# Output: {'apple': 9.0, 'banana': 18.0, 'orange': 27.0}


# ============================================================
# 41. map() RETURNS AN ITERATOR
# ============================================================

numbers = [1, 2, 3]

mapped = map(double, numbers)

print(next(mapped))
# Output: 2

print(next(mapped))
# Output: 4

print(list(mapped))
# Output: [6]

# Values already consumed with next() are not returned again.


# ============================================================
# PART 4: PRACTICAL EXAMPLES
# ============================================================

# 42. FINDING COMMON STUDENTS IN TWO COURSES

python_students = {"Sara", "Abebe", "Mimi"}
java_students = {"Mimi", "Dawit", "Sara"}

print(python_students & java_students)
# Output: {'Sara', 'Mimi'} (order may vary)


# ============================================================
# 43. FINDING STUDENTS ENROLLED IN EITHER COURSE
# ============================================================

all_students = python_students | java_students

print(all_students)
# Output: A set containing Sara, Abebe, Mimi, and Dawit.


# ============================================================
# 44. INVENTORY USING A DICTIONARY
# ============================================================

inventory = {
    "laptop": 5,
    "mouse": 20,
    "keyboard": 10
}

inventory["mouse"] -= 2
inventory["monitor"] = 4

print(inventory["mouse"])
# Output: 18

print(inventory["monitor"])
# Output: 4


# ============================================================
# 45. REMOVING DUPLICATE RECORDS
# ============================================================

emails = [
    "a@example.com",
    "b@example.com",
    "a@example.com",
    "c@example.com"
]

unique_emails = set(emails)

print(len(unique_emails))
# Output: 3


# ============================================================
# 46. GROUPING VALUES WITH A DICTIONARY
# ============================================================

scores = [
    ("Sara", 90),
    ("Abebe", 80),
    ("Sara", 95),
    ("Abebe", 85)
]

grouped_scores = {}

for name, score in scores:
    grouped_scores.setdefault(name, []).append(score)

print(grouped_scores)
# Output: {'Sara': [90, 95], 'Abebe': [80, 85]}


# ============================================================
# 47. FILTERING A DICTIONARY
# ============================================================

scores = {
    "Sara": 90,
    "Abebe": 45,
    "Mimi": 75,
    "Dawit": 35
}

passed = {
    name: score
    for name, score in scores.items()
    if score >= 50
}

print(passed)
# Output: {'Sara': 90, 'Mimi': 75}


# ============================================================
# END OF SETS, DICTIONARIES, AND map() EXAMPLES
# ============================================================