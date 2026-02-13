from ctypes import addressof


name = "Tom"
new_name = name.replace("o", "i")  # Tim

print(name)
print(new_name)
# replace o -> i

my_name = "     narayan       "
clean_name = my_name.replace(" ", "")
print(clean_name)

country = "UK"
country = country.replace("UK", "United Kingdom")
print(country)
################
name = "Narayan"
print(id(name))
name = "Elliot"
print(id(name))

# Lists are mutable
empty_list = []
print(empty_list)


ages = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(ages)

mixed = [True, 1, 2, 3, "Strings", 78.89]
print(mixed)

letters = list("Python")
print(letters)

numbers = list(range(8, 4, -1))
print(numbers)  # [1, 2, 3, 4, 5, 6, 7]

fruits = ["apple", "banana", "strawberries", "mango", "kiwi", "Blueberry"]
print(fruits)
# access the list
# print(fruits[10]) #  index notation
print(fruits[0:4])

fruits[0] = "pineapple"
print(fruits)
# ['pineapple', 'banana', 'strawberries', 'mango', 'kiwi', 'Blueberry']
fruits[0:2] = ["apricot", "guava"]
# ['apricot', 'guava', 'strawberries', 'mango', 'kiwi', 'Blueberry']
print(fruits)

my_nums = [1, 2, 3, 4, 5]
print(my_nums)
print(id(my_nums))  # 2711262109376
my_nums[2] = 300
print(my_nums)
print(id(my_nums))  # 2711262109376

print(dir(list))

# ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
my_nums.append(800)
print(my_nums)  # [1, 2, 300, 4, 5, 800]
my_nums.append([9, 100, 110])
print(my_nums)  # [1, 2, 300, 4, 5, 800, [9, 100, 110]]
my_nums.extend([12, 13, 14])
print(my_nums)  # [1, 2, 300, 4, 5, 800, [9, 100, 110], 12, 13, 14]

my_nums.remove(14)
print(my_nums)

my_nums.clear()
print(my_nums)

print(fruits)  # ['apricot', 'guava', 'strawberries', 'mango', 'kiwi', 'Blueberry']
position = fruits.index("mango")
print(position)

# position1 = fruits.index("mango", 4)
print(fruits.count("mango"))

print("Length is", len(fruits))

# Dictionaries
empty_dict = {}
student = {
    "name": "Narayan",
    "grade": "A",
    "subjects": ["Maths", "Science", "Python"],
    "phone": 46237462,
}
print("Student Dictionary", student)
person = {
    "name": "Robert",
    "height": 67.8,
    "is_Student": False,
    "address": {"street": "123 Main Street", "city": "Nottingham"},
}
print(person)

print("Name", person["name"])  # Robert
print("Name", person.get("name", "No such key"))
print("Street", person["address"]["street"])

# modifying dictionaries
my_dictionary = {"first_name": "Narayan", "last_name": "Khosla"}
my_dictionary["age"] = 500
print(my_dictionary)

my_dictionary.update({"email": "narayan@abc.com", "phone": 567567})
print(my_dictionary)

# print(dir(dict))
# [ 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
del my_dictionary["age"]
print("After deleting", my_dictionary)
my_dictionary["age"] = 500
print(my_dictionary)

my_dictionary.pop("age")

my_dictionary["age"] = 500
print(my_dictionary)

print(my_dictionary.pop("age1", "No such column found"))

print("Name", my_dictionary.get("age1", "No such key"))
