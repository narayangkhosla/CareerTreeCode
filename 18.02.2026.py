# Functions - default parameters
from numpy import multiply


def greet(phone, name="Charlie"):
    return f"{name} {phone}"


print(greet(456546, "Robert"))


#######################
def add(n1, n2):
    return n1 + n2


def add(n1, n2, n3):
    return n1 + n2 + n3


# *how to pass *args in a function
def add(*numbers):
    return sum(numbers)


def my_multiply(c, num):
    return c * num


print("29", my_multiply("t", 6))

# print(add(1, 2))
# print(add(1, 2, 89, 45, 6, 6))
# print(add(1, 2, 90, 78, 34, 35, 56, 676))

# print(add(189, 90))


# Lambda Functions
def square(x):
    return x * x


my_square = lambda y: y * y
print(my_square(6))

my_add = lambda a, b: a + b

# Unpacking operator in Lambda
add_all = lambda *args: sum(args)
print(add_all(1, 2, 3, 4))
print(add_all(1, 2, 3, 4, 5, 6, 7, 8, 9, 12))


def create_profile(name, age, city, role="user"):
    print(f"{name} | {age} | {city} | {role}")


# positional
create_profile("Alice", 30, "Nottingham", "Admin")
# keyword
create_profile(age=45, name="Robert", role="Test", city="London")
create_profile("Narayan", age=78, role="Test", city="London")
# mixing is possible if we put the positional arguments first followed by keyword arguments

# Error Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Sorry, you cannot divide by zero.")

# errors vs exceptions
# try,except, finally
# try:
#     f = open("data.txt")
#     my_data = f.read()
#     # process(my_data)
# except FileNotFoundError:
#     print("File missing!!")
# else:
# if no exceptions were raised
# finally:
#     f.close()  # always runs


# Raising an exception
# def set_age(age):
#     if age < 0:
#         raise ValueError(f"Age cannot be negative: {age}")


# set_age(-2)


def divide_100_by_input():
    try:
        raw_number = input("Enter a value to divide zero by: ")
        number = float(raw_number)
        result = 100 / number

    except ValueError:
        print(f"{raw_number} is not a valid number. Please enter a numeric value")

    except ZeroDivisionError:
        print("Cannot divide by 0.")

    except Exception as e:
        print(f"Unexcpected error occured: {e}")

    else:
        print(f"100 / {number} = {result}")
        return result
    finally:
        print("---Operation Complete ---")


divide_100_by_input()
