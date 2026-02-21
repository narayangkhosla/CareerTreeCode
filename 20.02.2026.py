# Higher Order Functions
# A HOF takes another function as an argument, or
# returns a function as its result


def shout(text):
    return text.upper()


def whisper(text):
    return text.lower()


def greet(func):
    message = func("Hello World")
    print(message)


# greet(shout)
# greet(whisper)

# map, filter, reduce, sorted
# apply a function to every item in the object
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def square(n):
    return n * n


print(square)
print(id(square))
# result = map(square, numbers)
# print(result)
# print(id(result))
# print(id)


# filter
def is_odd(n):
    return n % 2 != 0


res1 = list(filter(is_odd, numbers))
print(res1)

squared = list(map(lambda n: n * n, numbers))
evens = list(filter(lambda n: n % 2 == 0, numbers))
odds = list(filter(lambda n: n % 2 != 0, numbers))

print(squared)
print(evens)
print(odds)
