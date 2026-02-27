f = open("hello2.txt", "w")
f.write("hello, how are you?\n")
f.write("Second line here...\n")
f.write("Third line here...\n")
f.close()  # data leakage

# f = open("hello1.txt")
# contents = f.read()
# f.close()

# print(contents)
# readline()
f = open("hello2.txt")
print(f.readline(), end="")
print(f.readline(), end="")
print(f.readline(), end="")

f.seek(0)
lines = f.readlines()
print("20", lines)
print(type(lines))
f.close()

# Context Managers - you do not need to explicitly close the file
with open("notes.txt", "w") as f:
    f.write("hello, how are you?\n")
    f.write("Second line here...\n")
    f.write("Third line here...\n")

with open("notes.txt", "a") as f:
    f.write("Fourth line appended")

with open("notes.txt") as f:
    for line in f:
        print(line.strip())

# work with multiple files
with open("notes.txt") as src, open("hello.txt", "w") as dest:
    for line in src:
        dest.write(line.upper())
