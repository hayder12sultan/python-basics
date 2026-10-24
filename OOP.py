# ============================================================
# 1. CLASS AND OBJECT
# ============================================================

class Student:
    def study(self):
        print("The student is studying.")


student1 = Student()  # Create an object
student1.study()
# Output: The student is studying.


# ============================================================
# 2. ATTRIBUTES AND __init__()
# ============================================================

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}, and I am {self.age}.")

person1 = Person("Abebe", 20)
person1.introduce()
# Output: My name is Abebe, and I am 20.


# ============================================================
# 3. INSTANCE ATTRIBUTES
# Each object can have different attribute values.
# ============================================================

person2 = Person("Sara", 22)

print(person1.name)
# Output: Abebe

print(person2.name)
# Output: Sara

print(person2.age)
# Output: 22


# ============================================================
# 4. INSTANCE METHODS
# self refers to the current object.
# ============================================================

class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

calc = Calculator()

print(calc.add(5, 3))
# Output: 8

print(calc.multiply(4, 2))
# Output: 8


# ============================================================
# 5. CLASS ATTRIBUTES
# Shared through the class and available to its objects.
# ============================================================

class Employee:
    company = "Tech Solutions"

    def __init__(self, name):
        self.name = name

employee1 = Employee("Abebe")
employee2 = Employee("Sara")

print(employee1.company)
# Output: Tech Solutions

print(employee2.company)
# Output: Tech Solutions

print(Employee.company)
# Output: Tech Solutions


# ============================================================
# 6. INSTANCE ATTRIBUTES VS CLASS ATTRIBUTES
# ============================================================

class Car:
    wheels = 4  # Class attribute

    def __init__(self, brand):
        self.brand = brand  # Instance attribute

car1 = Car("Toyota")
car2 = Car("Honda")

print(car1.brand)
# Output: Toyota

print(car2.brand)
# Output: Honda

print(car1.wheels)
# Output: 4


# ============================================================
# 7. MODIFYING OBJECT ATTRIBUTES
# ============================================================

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

account = BankAccount("Abebe", 1000)

account.balance = 1500

print(account.balance)
# Output: 1500


# ============================================================
# 8. INSTANCE METHODS, CLASS METHODS, STATIC METHODS
# ============================================================

class StudentRecord:
    school = "ABC School"

    def __init__(self, name):
        self.name = name

    # Instance method: works with an object
    def introduce(self):
        return f"I am {self.name}"

    # Class method: works with the class
    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

    # Static method: utility associated with the class
    @staticmethod
    def is_passing(score):
        return score >= 50


record = StudentRecord("Sara")

print(record.introduce())
# Output: I am Sara

StudentRecord.change_school("XYZ School")

print(record.school)
# Output: XYZ School

print(StudentRecord.is_passing(75))
# Output: True

print(StudentRecord.is_passing(35))
# Output: False


# ============================================================
# 9. ENCAPSULATION
# Keep data and related methods together.
# ============================================================

class Wallet:
    def __init__(self, balance):
        self.__balance = balance  # Name-mangled attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

wallet = Wallet(500)

wallet.deposit(200)

print(wallet.get_balance())
# Output: 700

# __balance is not intended to be accessed directly.
# Python name-mangles it; this is not strict security.


# ============================================================
# 10. VALIDATION WITH ENCAPSULATION
# ============================================================

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price  # Uses the property setter

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value

product = Product("Laptop", 50000)

print(product.price)
# Output: 50000

product.price = 55000
print(product.price)
# Output: 55000

# product.price = -100
# Raises ValueError: Price cannot be negative


# ============================================================
# 11. INHERITANCE
# A child class inherits from a parent class.
# ============================================================

class Animal:
    def eat(self):
        print("This animal eats food.")

class Dog(Animal):
    def bark(self):
        print("The dog barks.")

dog = Dog()

dog.eat()
# Output: This animal eats food.

dog.bark()
# Output: The dog barks.


# ============================================================
# 12. EXTENDING A PARENT CLASS WITH super()
# ============================================================

class PersonBase:
    def __init__(self, name):
        self.name = name

class Teacher(PersonBase):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def teach(self):
        print(f"{self.name} teaches {self.subject}.")

teacher = Teacher("Sara", "Python")

teacher.teach()
# Output: Sara teaches Python.


# ============================================================
# 13. METHOD OVERRIDING
# A child class provides its own implementation.
# ============================================================

class AnimalSound:
    def sound(self):
        print("The animal makes a sound.")

class Cat(AnimalSound):
    def sound(self):
        print("Meow!")

class Cow(AnimalSound):
    def sound(self):
        print("Moo!")

Cat().sound()
# Output: Meow!

Cow().sound()
# Output: Moo!


# ============================================================
# 14. POLYMORPHISM
# Different objects respond to the same method differently.
# ============================================================

animals = [Cat(), Dog(), Cow()]

for animal in animals:
    if hasattr(animal, "sound"):
        animal.sound()
    else:
        print("This animal has no sound method defined.")

# Output:
# Meow!
# This animal has no sound method defined.
# Moo!

# hasattr() checks whether an object has a named attribute.
# In production code, a shared interface is usually preferable.


# ============================================================
# 15. DUCK TYPING
# An object can be used if it supports the required behavior.
# ============================================================

class PDF:
    def open(self):
        print("Opening PDF file.")

class WordDocument:
    def open(self):
        print("Opening Word document.")

def open_document(document):
    document.open()

open_document(PDF())
# Output: Opening PDF file.

open_document(WordDocument())
# Output: Opening Word document.


# ============================================================
# 16. ABSTRACTION
# Define a required interface using an abstract base class.
# ============================================================

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rectangle = Rectangle(5, 4)

print(rectangle.area())
# Output: 20

# Shape() cannot be instantiated because area() is abstract.


# ============================================================
# 17. MULTIPLE INHERITANCE
# A class inherits from more than one parent class.
# ============================================================

class Camera:
    def take_photo(self):
        print("Taking a photo.")

class Phone:
    def make_call(self):
        print("Making a phone call.")

class Smartphone(Camera, Phone):
    pass

phone = Smartphone()

phone.take_photo()
# Output: Taking a photo.

phone.make_call()
# Output: Making a phone call.


# ============================================================
# 18. METHOD RESOLUTION ORDER (MRO)
# Python uses MRO to determine which method is selected.
# ============================================================

class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):
    pass

D().show()
# Output: Class B

print([cls.__name__ for cls in D.mro()])
# Output: ['D', 'B', 'C', 'A', 'object']


# ============================================================
# 19. COMPOSITION
# One object contains or uses another object.
# ============================================================

class Engine:
    def start(self):
        print("Engine started.")

class Vehicle:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()
        print("Vehicle is ready.")

vehicle = Vehicle()
vehicle.start()

# Output:
# Engine started.
# Vehicle is ready.

# Composition often models "has-a" relationships.


# ============================================================
# 20. AGGREGATION
# An object uses another object that exists independently.
# ============================================================

class Department:
    def __init__(self, name):
        self.name = name

class University:
    def __init__(self, department):
        self.department = department

department = Department("Computer Science")
university = University(department)

print(university.department.name)
# Output: Computer Science

# The department was created separately and passed in.


# ============================================================
# 21. SPECIAL METHODS (__str__ AND __repr__)
# ============================================================

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"Book({self.title!r}, {self.author!r})"

book = Book("Clean Code", "Robert C. Martin")

print(book)
# Output: Clean Code by Robert C. Martin

print(repr(book))
# Output: Book('Clean Code', 'Robert C. Martin')


# ============================================================
# 22. OPERATOR OVERLOADING
# Define how operators work with your objects.
# ============================================================

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)

print(v1 + v2)
# Output: (6, 8)


# ============================================================
# 23. COMPARISON METHODS
# ============================================================

class Score:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if not isinstance(other, Score):
            return NotImplemented
        return self.value == other.value

    def __lt__(self, other):
        if not isinstance(other, Score):
            return NotImplemented
        return self.value < other.value

score1 = Score(80)
score2 = Score(90)
score3 = Score(80)

print(score1 == score3)
# Output: True

print(score1 < score2)
# Output: True


# ============================================================
# 24. CLASS COMPOSITION WITH MULTIPLE OBJECTS
# ============================================================

class Course:
    def __init__(self, title):
        self.title = title

class Learner:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

    def show_courses(self):
        for course in self.courses:
            print(course.title)

learner = Learner("Abebe")
learner.enroll(Course("Python"))
learner.enroll(Course("Database Systems"))

learner.show_courses()
# Output:
# Python
# Database Systems


# ============================================================
# 25. CLASS METHODS AS ALTERNATIVE CONSTRUCTORS
# ============================================================

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def from_full_name(cls, full_name):
        first, last = full_name.split()
        return cls(first, last)

user = User.from_full_name("Abebe Kebede")

print(user.first_name)
# Output: Abebe

print(user.last_name)
# Output: Kebede


# ============================================================
# 26. DATACLASSES
# Generate common methods automatically.
# ============================================================

from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

point1 = Point(2, 3)
point2 = Point(2, 3)

print(point1)
# Output: Point(x=2, y=3)

print(point1 == point2)
# Output: True


# ============================================================
# 27. ENUMS
# Represent a fixed set of named values.
# ============================================================

from enum import Enum

class OrderStatus(Enum):
    PENDING = "pending"
    PAID = "paid"
    SHIPPED = "shipped"

status = OrderStatus.PAID

print(status.name)
# Output: PAID

print(status.value)
# Output: paid


# ============================================================
# 28. CLASS DECORATOR: PROPERTY
# Calculate a value from other attributes.
# ============================================================

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

circle = Circle(5)

print(circle.diameter)
# Output: 10

# Accessed like an attribute, but calculated by a method.


# ============================================================
# 29. SLOTS
# Restrict which attributes an instance can have.
# ============================================================

class Coordinate:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

coordinate = Coordinate(10, 20)

print(coordinate.x, coordinate.y)
# Output: 10 20

# coordinate.z = 30
# Raises AttributeError because z is not in __slots__.


# ============================================================
# 30. PRACTICAL OOP PROJECT: BANK ACCOUNT
# Combines classes, attributes, methods, validation,
# encapsulation, and object interaction.
# ============================================================

class BankAccountProject:
    bank_name = "Python Bank"

    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")

        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            return "Deposit must be positive"

        self.__balance += amount
        return f"Deposited {amount}"

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal must be positive"

        if amount > self.__balance:
            return "Insufficient funds"

        self.__balance -= amount
        return f"Withdrew {amount}"

    def get_balance(self):
        return self.__balance

    def display(self):
        print(f"Bank: {self.bank_name}")
        print(f"Owner: {self.owner}")
        print(f"Balance: {self.__balance}")


account1 = BankAccountProject("Abebe", 1000)

print(account1.deposit(500))
# Output: Deposited 500

print(account1.withdraw(200))
# Output: Withdrew 200

print(account1.withdraw(5000))
# Output: Insufficient funds

account1.display()
# Output:
# Bank: Python Bank
# Owner: Abebe
# Balance: 1300

print(account1.get_balance())
# Output: 1300


# ============================================================
# 31. PRACTICAL OOP PROJECT: EMPLOYEE PAYROLL
# Demonstrates inheritance and polymorphism.
# ============================================================

class EmployeeBase:
    def __init__(self, name):
        self.name = name

    def calculate_pay(self):
        raise NotImplementedError("Subclass must implement calculate_pay")

class SalariedEmployee(EmployeeBase):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_pay(self):
        return self.monthly_salary

class HourlyEmployee(EmployeeBase):
    def __init__(self, name, hours, hourly_rate):
        super().__init__(name)
        self.hours = hours
        self.hourly_rate = hourly_rate

    def calculate_pay(self):
        return self.hours * self.hourly_rate

employees = [
    SalariedEmployee("Abebe", 30000),
    HourlyEmployee("Sara", 40, 200)
]

for employee in employees:
    print(employee.name, employee.calculate_pay())

# Output:
# Abebe 30000
# Sara 8000


# ============================================================
# 32. PRACTICAL OOP PROJECT: LIBRARY SYSTEM
# Demonstrates classes, object relationships, and state.
# ============================================================

class LibraryBook:
    def __init__(self, title):
        self.title = title
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            return f"{self.title} is already borrowed"

        self.is_borrowed = True
        return f"{self.title} borrowed successfully"

    def return_book(self):
        if not self.is_borrowed:
            return f"{self.title} was not borrowed"

        self.is_borrowed = False
        return f"{self.title} returned successfully"


library_book = LibraryBook("Python Basics")

print(library_book.borrow())
# Output: Python Basics borrowed successfully

print(library_book.borrow())
# Output: Python Basics is already borrowed

print(library_book.return_book())
# Output: Python Basics returned successfully


# ============================================================
# 33. OBJECT IDENTITY VS EQUALITY
# ============================================================

class Item:
    def __init__(self, name):
        self.name = name

item1 = Item("Laptop")
item2 = Item("Laptop")
item3 = item1

print(item1 is item2)
# Output: False

print(item1 is item3)
# Output: True

print(item1 == item2)
# Output: False

# Without a custom __eq__, == usually compares object identity
# for ordinary user-defined classes.


# ============================================================
# 34. TYPE CHECKING AND isinstance()
# ============================================================

class VehicleBase:
    pass

class Bus(VehicleBase):
    pass

bus = Bus()

print(isinstance(bus, Bus))
# Output: True

print(isinstance(bus, VehicleBase))
# Output: True

print(type(bus).__name__)
# Output: Bus


# ============================================================
# 35. CLEAN OOP DESIGN: SINGLE RESPONSIBILITY
# Keep each class focused on one job.
# ============================================================

class Order:
    def __init__(self, items):
        self.items = items

    def total(self):
        return sum(self.items)

class ReceiptPrinter:
    def print_receipt(self, order):
        print(f"Order total: {order.total()}")

order = Order([100, 200, 50])
printer = ReceiptPrinter()

printer.print_receipt(order)
# Output: Order total: 350


# ============================================================
# END OF PYTHON OOP EXAMPLES
# ============================================================