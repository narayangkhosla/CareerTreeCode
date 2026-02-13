# IF CONDITIONS
# age = 10
# if age >= 18:
#     print("You are an adult")
# else:
#     print("You are a minor")

# score = 85
# if score >= 90:
#     print("Grade A")
# elif score >= 80:
#     print("Grade B")
# elif score >= 70:
#     print("Grade C")
# else:
#     print("Grade F")

# logical operators - AND OR
# age = 30
# can_drive = False
# if not (can_drive and age >= 25):
#     # not(False and True)
#     # not(False)
#     # True
#     print("Welcome")

# number = int(input("Enter a number"))
# print(type(number))
# if number % 2 == 0:
#     print(f"{number} is even")
# else:
#     print(f"{number} is odd")

# number1 = 10
# number2 = 20

# print(number1 == number2)
# print(number1 <= number2)
# print(number1 >= number2)
# print(number1 != number2)
# print(number1 < number2)
# print(number1 > number2)

############################
# Strings
# name = "Alice"
# name1 = "Narayan"
# name2 = "I need to return Alice's book"
# name3 = 'I need to return Alice"s book'
# name4 = "I need to return Alice\"s book \tand Chris's \nbook as \\well"

# print(name4)

str1 = "Christophir"
str2 = "Narayan"

# print(str1 == str2)
# print(len(str1))
# password = input("Enter your password")
# pass_length = len(password)
# if pass_length <= 8:
#     print("Sorry, not strong enough")

str3 = "Robertaskjfhajklfhasjklfhkashfjasfhljsahfljsadhfjksdhlfjasdhfjsadfhasjfhasjfhlasjfhsdjhfjsfhjsadhfljsdhflkjashfljasdhfljaslf"

# print(str3[0])
# print(str3[1])
# print(str3[2])
# print(str3[3])
# print(str3[4])
# print(str3[50])
# print(str3[-1])

text = "CV2 7QA"
text1 = "Python Programming is one of the best languages"
print(text1[1:30])
print(text1[1:30:5])  # y rn o
# start end step
# every second character
str5 = "Narayan Khosla"
# print(str5[1 : len(str5) : 2])
print(str5[0 : len(str5) : 2])  # NrynKol
print(str5[1::2])  # aaa hsa
print(str5[::2])

str6 = "palindrome"
print(str6[::-1])  # emordnilap
print(str6[::1])  # palindrome
