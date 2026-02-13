# Loops
from math import ceil, floor


fruits = ["apple", "banana", "mango", "strawberry", "guava"]
# for variable_name in object:
#   code....
for fruit in fruits:
    print(fruit)

word = "Python"
for w in word:
    print(w)

colors = ("apple", "banana", "mango", "strawberry", "guava")
for color in colors:
    print(color)

student = {"name": "Alice", "age": 20, "grade": "A"}
for key in student:
    print(f"{key}:{student[key]}")
    # name :Alice
    # age : 20

for i in range(5):
    print(i)

for i in range(10, 0, -1):
    print(i)

# Enumerate
print("Without Enumerate")
# index : fruit_name
for i in range(0, len(fruits)):
    print(f"{i} - {fruits[i]}")

# for i in fruits:
#     print(f"{i} - {fruits[i]}")
#     # apple - fruits[0] =

for index, fruit in enumerate(fruits, start=13):
    print(f"{index}:{fruit}")

print("=" * 30)

products = {
    "Laptop": 89.8935,
    "Mouse": 45.899,
    "Keyboard": 787.343,
    "Headphones": 178.894,
}
for product, price in products.items():
    print(f"{product:<20}:${price:0.2f}")

print(f"{'The total is':15}  ${sum(products.values()):>8.2f}")
print(f"{'The total is':<15}  ${sum(products.values()):>8.2f}")
print(f"{'The total is':>15}  ${sum(products.values()):>8.2f}")
x = 78.18
print(floor(x))
print(ceil(x))
print(round(x))

for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:3}", end=" ")
    print()

classes = {
    "Monday": ["Maths", "Science", "English"],
    "Tuesday": ["History", "Maths", "PE"],
    "Wednesday": ["Science", "English", "Art"],
}
# Monday:
# Period 1: Maths
# Period 2: Science
# Period 3: English
for day, subjects in classes.items():
    print(f"\n{day}:")
    for period, subject in enumerate(subjects, start=1):
        print(f"Period {period}: {subject}")

# exit from the loop
# while loops
# comprehensions - homework for today

numbers = [1, 3, 5, 7, 8, 9, 11, 12]
for num in numbers:
    if num % 2 == 0:
        print(f"Found it : {num}")
        break
    print(f" {num} is odd, continuing...")

my_fruits = ["apple", "banana", "mango", "strawberry", "guava"]
search = "guava"
for index, fruit in enumerate(fruits):
    if fruit == search:
        print(f"Found {fruit} at index {index}")
        break
print(f"{search} not found.")

# max-attempts = 3
# password8990
# correct_pass = "python123"
# max_attempts = 3
# for attempt in range(1, max_attempts + 1):
#     password = input(f"Attempt {attempt}/{max_attempts} - Enter password: ")

#     if password == correct_pass:
#         print("Login Successful")
#         break
#     else:
#         remaining = max_attempts - attempt
#         if remaining > 0:
#             print(f"Wrong password. You have {remaining} attempts remaining.")
#         else:
#             print("Account locked. Too many attempts")

# While loops
# when number of iterations is KNOWN - for or while
# when number of iterations is UNKNOWN - while
# enter a number -1  to exit

my_fruits1 = ["apple", "banana", "mango", "strawberry", "guava"]
for f in my_fruits1:
    print(f)

responses = ["hello", "quit", "more", "less"]
index = 0
while True:
    user_input = input("Enter something (type 'quit' to exit): ")
    print(f"User entered: {user_input}")
    if user_input == "quit":
        print("Exiting")
        break
    index = index + 1
