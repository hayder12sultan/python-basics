# ============================================================
# 1. VARIABLES AND CONSTANTS
# ============================================================

# PYTHON
name = "Sara"
age = 21
PI = 3.14  # Naming convention only; not a true constant
age = 22
print(name, age)  # Sara 22

# JAVASCRIPT
# let name = "Sara";
# let age = 21;
# const PI = 3.14;
# age = 22;
# console.log(name, age); // Sara 22

# Difference:
# Python does not use let or const.
# JavaScript uses let for reassignment and const for bindings
# that cannot be reassigned.


# ============================================================
# 2. DATA TYPES
# ============================================================

# PYTHON
name = "Sara"       # str
age = 21            # int
price = 19.99       # float
active = True       # bool
result = None       # NoneType

print(type(name))    # <class 'str'>
print(type(age))     # <class 'int'>
print(type(price))   # <class 'float'>
print(type(active))  # <class 'bool'>

# JAVASCRIPT
# let name = "Sara";       // string
# let age = 21;            // number
# let price = 19.99;       // number
# let active = true;       // boolean
# let result = null;
# let missing;
#
# console.log(typeof name);    // "string"
# console.log(typeof age);     // "number"
# console.log(typeof result);  // "object" (historical quirk)
# console.log(typeof missing); // "undefined"

# Difference:
# Python separates int and float.
# JavaScript uses number for ordinary integers and decimals.
# Python uses True, False, None.
# JavaScript uses true, false, null, undefined.


# ============================================================
# 3. TYPE CONVERSION
# ============================================================

# PYTHON
age = int("21")
price = float("19.99")
text = str(100)
active = bool(1)

print(age)     # 21
print(price)   # 19.99
print(text)    # "100"
print(active)  # True

# int("abc") raises ValueError.

# JAVASCRIPT
# let age = Number("21");
# let price = Number("19.99");
# let text = String(100);
# let active = Boolean(1);
#
# console.log(age);             // 21
# console.log(price);           // 19.99
# console.log(text);            // "100"
# console.log(active);          // true
# console.log(Number("abc"));   // NaN
# console.log(Number(""));      // 0

# Difference:
# Python commonly raises an exception for invalid conversion.
# JavaScript Number() often returns NaN instead.


# ============================================================
# 4. OPERATORS AND EQUALITY
# ============================================================

# PYTHON
print(5 == 5)     # True
print(5 != 3)     # True
print(5 > 3)      # True
print(5 == "5")   # False

# Comparing 5 > "3" raises TypeError.

# JAVASCRIPT
# console.log(5 === 5);  // true
# console.log(5 !== 3);  // true
# console.log(5 == "5"); // true (type coercion)
# console.log(5 === "5");// false
# console.log(5 > "3");  // true

# Difference:
# Python uses == for equality.
# JavaScript uses == for loose equality and === for strict equality.
# Prefer === and !== in JavaScript.


# ============================================================
# 5. LOGICAL OPERATORS
# ============================================================

# PYTHON
age = 21
has_id = True

print(age >= 18 and has_id)  # True
print(age < 18 or has_id)    # True
print(not has_id)            # False

# JAVASCRIPT
# let age = 21;
# let hasId = true;
# console.log(age >= 18 && hasId); // true
# console.log(age < 18 || hasId);  // true
# console.log(!hasId);             // false

# Python: and, or, not
# JavaScript: &&, ||, !

# Both languages can return an operand instead of a Boolean:
# Python:     print("" or "Guest")       # Guest
# JavaScript: console.log("" || "Guest");// Guest


# ============================================================
# 6. CONDITIONAL STATEMENTS
# ============================================================

# PYTHON
score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")
# Output: B

# JAVASCRIPT
# let score = 85;
# if (score >= 90) {
#     console.log("A");
# } else if (score >= 80) {
#     console.log("B");
# } else {
#     console.log("C");
# }
# Output: B

# Difference:
# Python uses elif and indentation.
# JavaScript uses else if and curly braces.


# ============================================================
# 7. STRINGS AND STRING METHODS
# ============================================================

# PYTHON
name = "  sara ali  "

print(name.strip())               # sara ali
print(name.upper())               #   SARA ALI
print(name.lower())               #   sara ali
print(name.replace("sara", "Mimi")) #   Mimi ali
print("python".startswith("py"))  # True
print("a,b,c".split(","))         # ['a', 'b', 'c']
print("-".join(["a", "b", "c"]))  # a-b-c
print(f"Hello {name.strip()}")    # Hello sara ali

# JAVASCRIPT
# let name = "  sara ali  ";
# console.log(name.trim());                    // sara ali
# console.log(name.toUpperCase());             //   SARA ALI
# console.log(name.toLowerCase());             //   sara ali
# console.log(name.replace("sara", "Mimi"));    //   Mimi ali
# console.log("python".startsWith("py"));       // true
# console.log("a,b,c".split(","));              // ["a", "b", "c"]
# console.log(["a", "b", "c"].join("-"));       // a-b-c
# console.log(`Hello ${name.trim()}`);          // Hello sara ali

# Difference:
# Python uses strip(), upper(), lower(), and f-strings.
# JavaScript uses trim(), toUpperCase(), toLowerCase(),
# and template literals.
# Strings are immutable in both languages.


# ============================================================
# 8. LISTS VS ARRAYS
# ============================================================

# PYTHON
numbers = [10, 20, 30]
numbers.append(40)
numbers.insert(0, 5)
numbers.remove(20)

print(numbers)       # [5, 10, 30, 40]
print(numbers[0])    # 5
print(len(numbers))  # 4
print(30 in numbers) # True
print(numbers.pop()) # 40

# JAVASCRIPT
# let numbers = [10, 20, 30];
# numbers.push(40);
# numbers.unshift(5);
# numbers.splice(numbers.indexOf(20), 1);
#
# console.log(numbers);               // [5, 10, 30, 40]
# console.log(numbers[0]);            // 5
# console.log(numbers.length);        // 4
# console.log(numbers.includes(30));  // true
# console.log(numbers.pop());         // 40

# Difference:
# Python list: append(), insert(), remove(), len()
# JavaScript array: push(), unshift(), splice(), length
# Both collections can contain values of different types.


# ============================================================
# 9. DICTIONARIES VS OBJECTS
# ============================================================

# PYTHON
student = {"name": "Sara", "age": 21}

print(student["name"])          # Sara
print(student.get("grade", 0))  # 0

student["age"] = 22
student["grade"] = 90

print("name" in student)        # True
print(list(student.keys()))     # ['name', 'age', 'grade']
print(list(student.values()))   # ['Sara', 22, 90]

# JAVASCRIPT
# let student = { name: "Sara", age: 21 };
# console.log(student.name);          // Sara
# console.log(student.grade ?? 0);    // 0
#
# student.age = 22;
# student.grade = 90;
#
# console.log("name" in student);     // true
# console.log(Object.keys(student));  // ["name", "age", "grade"]
# console.log(Object.values(student));// ["Sara", 22, 90]

# Difference:
# Python uses dictionaries with key-value pairs.
# JavaScript objects store properties and have prototype behavior.
# JavaScript also has Map for key-value collections.


# ============================================================
# 10. SETS
# ============================================================

# PYTHON
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # Union: {1, 2, 3, 4, 5}
print(a & b)  # Intersection: {3}
print(a - b)  # Difference: {1, 2}
print(2 in a) # True

a.add(4)
a.discard(1)
print(a)

# JAVASCRIPT
# let a = new Set([1, 2, 3]);
# let b = new Set([3, 4, 5]);
#
# console.log(a.has(2)); // true
# a.add(4);
# a.delete(1);
# console.log([...a]);   // [2, 3, 4]

# Difference:
# Python supports convenient set operators: |, &, -.
# JavaScript uses Set methods such as add(), has(), delete().
# Modern JavaScript supports set operations in newer runtimes;
# check compatibility before using them.


# ============================================================
# 11. LOOPS
# ============================================================

# PYTHON
numbers = [10, 20, 30]

for number in numbers:
    print(number)

for i in range(3):
    print(i)

# Output:
# 10
# 20
# 30
# 0
# 1
# 2

# JAVASCRIPT
# let numbers = [10, 20, 30];
#
# for (const number of numbers) {
#     console.log(number);
# }
#
# for (let i = 0; i < 3; i++) {
#     console.log(i);
# }

# Difference:
# Python uses for item in collection and range().
# JavaScript uses for...of to iterate values and classic for loops.


# ============================================================
# 12. FUNCTIONS
# ============================================================

# PYTHON
def add(a, b=0):
    return a + b

print(add(3, 4))  # 7
print(add(3))     # 3

# JAVASCRIPT
# function add(a, b = 0) {
#     return a + b;
# }
#
# console.log(add(3, 4)); // 7
# console.log(add(3));    // 3
#
# const multiply = (a, b) => a * b;
# console.log(multiply(3, 4)); // 12

# Difference:
# Python uses def.
# JavaScript supports function declarations and arrow functions.
# A Python function without return gives None.
# A JavaScript function without return gives undefined.


# ============================================================
# 13. MAP, FILTER, AND COMPREHENSIONS
# ============================================================

# PYTHON
numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))

print(squares)  # [1, 4, 9, 16, 25]
print(evens)    # [2, 4]

# Python comprehensions are often simpler:
print([x * x for x in numbers])
print([x for x in numbers if x % 2 == 0])

# JAVASCRIPT
# let numbers = [1, 2, 3, 4, 5];
# let squares = numbers.map(x => x * x);
# let evens = numbers.filter(x => x % 2 === 0);
#
# console.log(squares); // [1, 4, 9, 16, 25]
# console.log(evens);   // [2, 4]

# Difference:
# Python map() and filter() return iterators.
# JavaScript array map() and filter() return new arrays.


# ============================================================
# 14. MISSING VALUES
# ============================================================

# PYTHON
user = None

if user is None:
    print("No user")
# Output: No user

# JAVASCRIPT
# let user = null;
# if (user === null) {
#     console.log("No user");
# }

# Difference:
# Python commonly uses is None.
# JavaScript uses === null for explicit null values.
# JavaScript also has undefined for unassigned or missing values.


# ============================================================
# 15. ERROR HANDLING
# ============================================================

# PYTHON
try:
    number = int("abc")
except ValueError:
    print("Invalid number")
finally:
    print("Finished")

# Output:
# Invalid number
# Finished

# JAVASCRIPT
# try {
#     let number = Number("abc");
#     if (Number.isNaN(number)) {
#         throw new Error("Invalid number");
#     }
# } catch (error) {
#     console.log("Invalid number");
# } finally {
#     console.log("Finished");
# }

# Difference:
# Python uses except.
# JavaScript uses catch.
# int("abc") raises an exception.
# Number("abc") returns NaN, so JavaScript needs a check or throw.


# ============================================================
# 16. SORTING
# ============================================================

# PYTHON
numbers = [4, 1, 3, 2]

print(sorted(numbers))  # [1, 2, 3, 4]
numbers.sort()
print(numbers)          # [1, 2, 3, 4]

# JAVASCRIPT
# let numbers = [4, 1, 3, 2];
# console.log([...numbers].sort((a, b) => a - b));
# // [1, 2, 3, 4]
#
# numbers.sort((a, b) => a - b);
# console.log(numbers); // [1, 2, 3, 4]

# Difference:
# Python sorted() returns a new list.
# Python list.sort() modifies the original list.
# JavaScript array.sort() modifies the original array.
# JavaScript numeric sorting needs (a, b) => a - b.


# ============================================================
# 17. STRING AND NUMBER ADDITION
# ============================================================

# PYTHON
print("Age: " + str(21))  # Age: 21
print(10 + 5)              # 15
# print("10" + 5)          # TypeError

# JAVASCRIPT
# console.log("Age: " + 21); // Age: 21
# console.log(10 + 5);       // 15
# console.log("10" + 5);     // 105
# console.log("10" - 5);     // 5

# Difference:
# Python usually requires explicit string-number conversion.
# JavaScript + can concatenate strings, while - often converts
# numeric strings to numbers.


# ============================================================
# 18. VARIABLE SCOPE
# ============================================================

# PYTHON
x = 10

def show():
    x = 20
    print(x)

show()       # 20
print(x)     # 10

# JAVASCRIPT
# let x = 10;
#
# function show() {
#     let x = 20;
#     console.log(x);
# }
#
# show();       // 20
# console.log(x); // 10

# Difference:
# Both examples create a local variable that shadows an outer one.
# Python assignment in a function is local unless declared global
# or nonlocal. JavaScript let and const are block-scoped.


# ============================================================
# 19. CLASSES AND OBJECTS
# ============================================================

# PYTHON
class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"My name is {self.name}"

student = Student("Sara")
print(student.introduce())  # My name is Sara

# JAVASCRIPT
# class Student {
#     constructor(name) {
#         this.name = name;
#     }
#
#     introduce() {
#         return `My name is ${this.name}`;
#     }
# }
#
# let student = new Student("Sara");
# console.log(student.introduce()); // My name is Sara

# Difference:
# Python uses __init__() and self.
# JavaScript uses constructor() and this.


# ============================================================
# 20. ASYNCHRONOUS PROGRAMMING
# ============================================================

# PYTHON
import asyncio

async def get_message():
    return "Hello"

async def main():
    message = await get_message()
    print(message)

asyncio.run(main())
# Output: Hello

# JAVASCRIPT
# async function getMessage() {
#     return "Hello";
# }
#
# async function main() {
#     const message = await getMessage();
#     console.log(message);
# }
#
# main();
# Output: Hello

# Difference:
# Both use async and await.
# Python commonly uses asyncio to run asynchronous code.
# JavaScript uses promises and the event loop.


# ============================================================
# 21. QUICK COMPARISON
# ============================================================

# Print:
# Python:     print(x)
# JavaScript: console.log(x)

# Length:
# Python:     len(items)
# JavaScript: items.length

# Append:
# Python:     items.append(x)
# JavaScript: items.push(x)

# Equality:
# Python:     a == b
# JavaScript: a === b

# Logical AND:
# Python:     a and b
# JavaScript: a && b

# No value:
# Python:     None
# JavaScript: null / undefined

# Function:
# Python:     def add(a, b): return a + b
# JavaScript: function add(a, b) { return a + b; }

# String interpolation:
# Python:     f"Hello {name}"
# JavaScript: `Hello ${name}`

# Error handling:
# Python:     try / except
# JavaScript: try / catch

# Collections:
# Python:     list, dict, set
# JavaScript: Array, Object, Set

# Loop:
# Python:     for item in items:
# JavaScript: for (const item of items)