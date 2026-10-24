# ============================================================
# 1. BASIC TRY AND EXCEPT
# ============================================================

try:
    number = int("abc")
except ValueError:
    print("Invalid number!")

# Output: Invalid number!

# try: code that might raise an exception
# except: code that handles a matching exception


# ============================================================
# 2. HANDLING MULTIPLE EXCEPTIONS
# ============================================================

try:
    number = int("10")
    result = 100 / 0

except ValueError:
    print("Invalid conversion.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

# Output: Cannot divide by zero.


# ============================================================
# 3. HANDLING DIFFERENT EXCEPTIONS IN ONE BLOCK
# ============================================================

try:
    number = int("abc")

except (ValueError, TypeError):
    print("The input could not be converted to an integer.")

# Output: The input could not be converted to an integer.


# ============================================================
# 4. TRY, EXCEPT, ELSE, AND FINALLY
# ============================================================

try:
    number = int("25")
    result = 100 / number

except (ValueError, ZeroDivisionError):
    print("An error occurred.")

else:
    print("Result:", result)

finally:
    print("Operation finished.")

# Output:
# Result: 4.0
# Operation finished.

# else runs if the try block raises no exception.
# finally runs whether an exception occurred or not.


# ============================================================
# 5. CATCHING A SPECIFIC EXCEPTION
# ============================================================

try:
    result = 10 / 0

except ZeroDivisionError:
    print("Division by zero is not allowed.")

# Output: Division by zero is not allowed.

# Prefer specific exceptions over a broad except clause.


# ============================================================
# 6. ACCESSING THE EXCEPTION MESSAGE
# ============================================================

try:
    number = int("hello")

except ValueError as error:
    print("Error:", error)

# Output:
# Error: invalid literal for int() with base 10: 'hello'

# The exact error wording can vary between Python versions.


# ============================================================
# 7. COMMON BUILT-IN EXCEPTIONS
# ============================================================

# ValueError
try:
    int("hello")
except ValueError:
    print("ValueError handled")

# Output: ValueError handled


# TypeError
try:
    result = "5" + 5
except TypeError:
    print("TypeError handled")

# Output: TypeError handled


# ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError:
    print("ZeroDivisionError handled")

# Output: ZeroDivisionError handled


# IndexError
try:
    items = [10, 20]
    print(items[5])
except IndexError:
    print("IndexError handled")

# Output: IndexError handled


# KeyError
try:
    person = {"name": "Sara"}
    print(person["age"])
except KeyError:
    print("KeyError handled")

# Output: KeyError handled


# NameError
try:
    print(unknown_variable)
except NameError:
    print("NameError handled")

# Output: NameError handled


# AttributeError
try:
    number = 10
    number.append(5)
except AttributeError:
    print("AttributeError handled")

# Output: AttributeError handled


# FileNotFoundError
try:
    with open("missing_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")

# Output: File not found.


# ============================================================
# 8. USING EXCEPTIONS FOR INPUT VALIDATION
# ============================================================

def get_integer(value):
    try:
        return int(value)
    except ValueError:
        return "Please provide a valid integer."

print(get_integer("25"))
# Output: 25

print(get_integer("abc"))
# Output: Please provide a valid integer.


# ============================================================
# 9. RETRYING AFTER AN ERROR
# ============================================================

def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero."

print(divide_numbers(10, 2))
# Output: 5.0

print(divide_numbers(10, 0))
# Output: Cannot divide by zero.


# ============================================================
# 10. RAISING AN EXCEPTION WITH raise
# ============================================================

def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive.")

    if amount > balance:
        raise ValueError("Insufficient balance.")

    return balance - amount

try:
    print(withdraw(1000, 200))
    # Output: 800

    print(withdraw(1000, 1500))

except ValueError as error:
    print("Transaction error:", error)

# Output:
# 800
# Transaction error: Insufficient balance.

# raise explicitly signals an error when a rule is violated.


# ============================================================
# 11. RAISING DIFFERENT EXCEPTIONS
# ============================================================

def calculate_average(total, count):
    if count < 0:
        raise ValueError("Count cannot be negative.")

    if count == 0:
        raise ZeroDivisionError("Count cannot be zero.")

    return total / count

try:
    print(calculate_average(100, 0))
except ZeroDivisionError as error:
    print(error)

# Output: Count cannot be zero.


# ============================================================
# 12. CUSTOM EXCEPTIONS
# ============================================================

class InsufficientFundsError(Exception):
    pass

def transfer(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("Not enough funds.")

    return balance - amount

try:
    print(transfer(500, 800))
except InsufficientFundsError as error:
    print("Transfer failed:", error)

# Output: Transfer failed: Not enough funds.

# Custom exceptions let you represent application-specific errors.


# ============================================================
# 13. CUSTOM EXCEPTION WITH ADDITIONAL DATA
# ============================================================

class InvalidAgeError(Exception):
    def __init__(self, age):
        self.age = age
        super().__init__(f"Invalid age: {age}")

def register_user(age):
    if age < 18:
        raise InvalidAgeError(age)

    return "Registration successful"

try:
    print(register_user(15))
except InvalidAgeError as error:
    print(error)
    print("Provided age:", error.age)

# Output:
# Invalid age: 15
# Provided age: 15


# ============================================================
# 14. EXCEPTION HIERARCHY
# ============================================================

try:
    int("abc")

except ValueError:
    print("This is a ValueError.")

# Output: This is a ValueError.

# ValueError is a subclass of Exception.
# Catching Exception also catches many unrelated errors,
# so catch the narrowest appropriate exception first.


# ============================================================
# 15. EXCEPTION ORDER MATTERS
# ============================================================

try:
    int("abc")

except ValueError:
    print("Handled as ValueError.")

except Exception:
    print("Handled as a general exception.")

# Output: Handled as ValueError.

# Put specific exception handlers before general handlers.


# ============================================================
# 16. FINALLY FOR CLEANUP
# ============================================================

try:
    print("Opening resource.")
    result = 10 / 0

except ZeroDivisionError:
    print("An error occurred.")

finally:
    print("Cleaning up resource.")

# Output:
# Opening resource.
# An error occurred.
# Cleaning up resource.

# finally is commonly used for cleanup that must be attempted.


# ============================================================
# 17. USING with FOR FILE HANDLING
# ============================================================

try:
    with open("example.txt", "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("The file does not exist.")

# If example.txt is absent:
# Output: The file does not exist.

# with automatically closes the file, even if an error occurs.


# ============================================================
# 18. HANDLING FILE WRITING ERRORS
# ============================================================

try:
    with open("example_output.txt", "w") as file:
        file.write("Hello from Python!")

    print("File written successfully.")

except OSError as error:
    print("File operation failed:", error)

# Typical output when writing succeeds:
# File written successfully.

# OSError covers many operating-system-related file errors.


# ============================================================
# 19. EXCEPTION CHAINING WITH raise ... from
# ============================================================

def parse_age(value):
    try:
        age = int(value)
    except ValueError as error:
        raise ValueError("Age must be a whole number.") from error

    return age

try:
    parse_age("twenty")
except ValueError as error:
    print(error)
    print("Original cause:", type(error.__cause__).__name__)

# Output:
# Age must be a whole number.
# Original cause: ValueError

# Exception chaining preserves the original cause for debugging.


# ============================================================
# 20. RE-RAISING AN EXCEPTION
# ============================================================

try:
    try:
        int("abc")
    except ValueError:
        print("Logging the conversion failure.")
        raise

except ValueError:
    print("The exception reached the outer handler.")

# Output:
# Logging the conversion failure.
# The exception reached the outer handler.

# Bare raise re-raises the currently handled exception.


# ============================================================
# 21. ASSERTIONS
# ============================================================

def calculate_discount(price, discount):
    assert price >= 0, "Price cannot be negative."
    assert 0 <= discount <= 100, "Discount must be between 0 and 100."

    return price * (1 - discount / 100)

print(calculate_discount(100, 20))
# Output: 80.0

# An invalid assertion raises AssertionError.
# Use assertions for programmer assumptions and debugging,
# not for validating untrusted user input.


# ============================================================
# 22. HANDLING ERRORS IN A LOOP
# ============================================================

values = ["10", "20", "abc", "30"]

for value in values:
    try:
        number = int(value)
        print(number * 2)
    except ValueError:
        print(f"Skipping invalid value: {value}")

# Output:
# 20
# 40
# Skipping invalid value: abc
# 60


# ============================================================
# 23. VALIDATING MULTIPLE USER VALUES
# ============================================================

def calculate_total(price_text, quantity_text):
    try:
        price = float(price_text)
        quantity = int(quantity_text)

        if price < 0:
            raise ValueError("Price cannot be negative.")

        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        return price * quantity

    except ValueError as error:
        return f"Invalid input: {error}"

print(calculate_total("25.5", "4"))
# Output: 102.0

print(calculate_total("abc", "4"))
# Output: Invalid input: could not convert string to float: 'abc'
# Exact wording may vary by Python version.


# ============================================================
# 24. AVOIDING BARE except
# ============================================================

# Avoid:
# try:
#     risky_operation()
# except:
#     print("Something went wrong.")

# Better:
def safe_convert(value):
    try:
        return int(value)
    except ValueError:
        return None

print(safe_convert("42"))
# Output: 42

print(safe_convert("hello"))
# Output: None

# A bare except catches almost everything, including exceptions
# such as KeyboardInterrupt and SystemExit.
# Catch only exceptions you know how to handle.


# ============================================================
# 25. HANDLING API-LIKE DATA
# ============================================================

def get_user_name(user_data):
    try:
        return user_data["user"]["name"]
    except KeyError:
        return "Name is missing."
    except TypeError:
        return "Invalid data structure."

print(get_user_name({"user": {"name": "Sara"}}))
# Output: Sara

print(get_user_name({"user": {}}))
# Output: Name is missing.

print(get_user_name(None))
# Output: Invalid data structure.


# ============================================================
# 26. PRACTICAL PROJECT: ATM TRANSACTION
# ============================================================

class ATM:
    def __init__(self, balance):
        if balance < 0:
            raise ValueError("Balance cannot be negative.")
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds.")

        self.balance -= amount
        return self.balance

atm = ATM(1000)

try:
    remaining = atm.withdraw(300)
    print("Remaining balance:", remaining)

    remaining = atm.withdraw(900)
    print("Remaining balance:", remaining)

except (ValueError, InsufficientFundsError) as error:
    print("Transaction failed:", error)

# Output:
# Remaining balance: 700
# Transaction failed: Insufficient funds.


# ============================================================
# 27. PRACTICAL PROJECT: SAFE CALCULATOR
# ============================================================

def calculator(a, operator, b):
    try:
        a = float(a)
        b = float(b)

        if operator == "+":
            return a + b
        elif operator == "-":
            return a - b
        elif operator == "*":
            return a * b
        elif operator == "/":
            return a / b
        else:
            raise ValueError("Unsupported operator.")

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError as error:
        return f"Error: {error}"

print(calculator("10", "+", "5"))
# Output: 15.0

print(calculator("10", "/", "0"))
# Output: Error: Cannot divide by zero.

print(calculator("ten", "+", "5"))
# Output: Error: could not convert string to float: 'ten'
# Exact wording may vary by Python version.


# ============================================================
# 28. PRACTICAL PROJECT: USER REGISTRATION
# ============================================================

class RegistrationError(Exception):
    pass

def register(name, age, email):
    if not name.strip():
        raise RegistrationError("Name is required.")

    if age < 18:
        raise RegistrationError("User must be at least 18.")

    if "@" not in email:
        raise RegistrationError("Invalid email address.")

    return "Registration successful."

try:
    print(register("Sara", 22, "sara@example.com"))
    # Output: Registration successful.

    print(register("Abebe", 16, "abebe@example.com"))

except RegistrationError as error:
    print("Registration failed:", error)

# Output:
# Registration successful.
# Registration failed: User must be at least 18.


# ============================================================
# END OF PYTHON EXCEPTION HANDLING EXAMPLES
# ============================================================