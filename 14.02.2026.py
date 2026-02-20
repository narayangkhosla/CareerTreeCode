# names = ["Narayan", "Elliot", "Charlie"]

# for name in names:
#     print(name.upper())
# name = Charlie

# index = 0
# while index<len(names):
#     print(names[index])
#     index +=1

# when you don't know how many iteration would you need?
# while True:
#     user_input = input("Enter your name: ")
#     print(f"User Entered {user_input}")

#     if user_input == 'quit':
#         print('Exiting')
#         break


# numbers = [10, 23, 45, 78, 67, 99]
# target = 67
# found = False

# for index, num in enumerate(numbers):
#     print(f"Checking position {index}:{num}")
#     if num == target:        
#         print(f"Number {target} found at index {index}")
#         found = True
#         break
# else:
#     print(f"Number {target} not found...")

# data = [100, -200, -50, 300, 150]

# all_valid = True
# has_errors = False
# for item in data:
#     if item < 0:
#         print(f"Invalid value: {item}")
#         all_valid = False
#         has_errors = True
#     else:
#         print(f"Valid: {item}")

# if all_valid:
#     print("All data is valid")
# else:
#     print("Some values are less than 0.")


# print("="*40)
# text = "Hello World, How are you?"
# vowels = 'aeiouAEIOU'

# vowel_count = 0
# for char in text:
#     if char in vowels:
#         vowel_count +=1
#         print(f"Vowel found: {char}")

# print(f"Total Vowels: {vowel_count}")

print("="*70)
# Functions
# defining/declaring the function
def greet():
    """a simple greeting function""" # docstring
    print("Hello World")

greet()

def welcome_message():
    """Displays a welcome message for all the users"""
    print("="*70)
    print("Welcome to Python Programming")
    print("Let's learn about FUNCTIONS today!!")
    print("="*70)

welcome_message()

# functions with parameters/arguments
def my_greet(name, age):
    """Greet a person with name""" # docstring
    print(f"Hello {name}. You are {age} years old.") # string formatting    
my_greet('narayan', 20)
my_greet('Alice', 21)

def add_numbers(num1, num2):
    result = num1 + num2
    print(f"The sum of {num1} + {num2} = {result}")

add_numbers(10,6)

print(id(my_greet)) # 1856791852864
def my_greet(phone_number):   
    print(f"Hello {phone_number}") # string formatting    
my_greet(2132132)
print(id(my_greet)) # 2632117729440

# functions with return values
def multiply(a, b):
    return a*b

def get_grade(score):
    """Return the grade based on the score"""
    if score>=90:
        return 'A'
    elif score>=80:
        return 'B'
    elif score>=70:
        return 'C'
    else:
        return 'F'
print(get_grade(56))
print(get_grade(99))
