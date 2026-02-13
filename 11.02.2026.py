# Dictionary
student = {"name": "Alice", "age": 20, "grade": "A"}

if "name" in student:
    print("Yayyyy")

if "Alice" in student.values():
    print("We found Alice")

# users = {"alice": "password123", "bob": "secret666", "charlie": "pass4545"}
# username = input("\nEnter a username: ")
# password = input("\nEnter a password: ")

# bob narayan

# if username in users:
#     if users[username] == password:
#         print("Login successful")
#     else:
#         print("Wrong password")
# else:
#     print("Username not found!!")

print(dir(float))

# two dictionaries students and users. make one dictionary
dict1 = {"name": "Narayan", "language": "Python", "city": "London"}

dict2 = {"empID": 101, "canDrive": True, "hobby": "Cricket"}

print(dir(dict))

# merged_dict = dict1.copy()
# merged_dict.update(dict2)

# merged_dict = {**dict1, **dict2}

merged_dict = dict1 | dict2

print("merged dictionary", merged_dict)

# Tuples - immutable
coordinates = (89, 899)
print(type(coordinates))

empty_tuple = ()
print(empty_tuple)

mixed_tuple = ("Alice", 25, 24.56, True)
print(mixed_tuple)

one_value = (78,)
print(type(one_value))

my_fruits = ("apple", "pineapple", "guava", "kiwi", "blueberries")
print(len(my_fruits))

print(my_fruits[-1])

print("line 60", my_fruits[0:2])
print("line 61", my_fruits[-2::])
print("line 62", my_fruits[-2::-1])
print("line 63", my_fruits[::2])

person = ("Narayan", 40, "Junior Programmer")
name, age, job = person
print(f"Name: {name}")

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
first, middle, *last = numbers
first, middle, last = numbers[0:9:3]
print(f"Last_Number: {last}")
print(f"First_Number: {first}")
print(f"Middle: {middle}")

point = (10, 20)
print("Original Tuple", point)
print("Memory Address", id(point))

# Error Handling
# try:
# point[0] = 16
# print(point)
# except TypeError as e:
#     print("Sorry, Narayan. You should know that tuples are immutable")

print("Hello")

# Tuples with mutuable objects
# Tuples are immutable but can contain mutable objects
data = (1, 2, 3, [4, 5])
print(type(data))

data[3].append(67)
print(data)
