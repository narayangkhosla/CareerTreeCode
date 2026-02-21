# Instructions for Building the Student Management System
# Complete the following tasks step by step. Think carefully about how to implement each requirement. You'll need to decide on data structures, logic, and implementation details yourself.

# Part 1: Basic Setup (15 minutes)

# Create a way to store multiple students in your program. Think about what data structure would work best for a collection of students.
# Write a function that can add a new student to your system. Consider:

# What information should each student have?
# How will you identify each student uniquely?
# What should the function return?
# Where will the student data be stored?


# Add at least 3 students to test your function.
# Write a function that displays all students in your system. Think about:

# How should the information be formatted?
# What details are most important to show?


# Test your display function.


# Part 2: Managing Student Performance (15 minutes)

# Students need to have test scores. Write a function that can add a score for a specific student. Consider:

# How will you find the right student?
# How will you store multiple scores for one student?
# What should happen if the student doesn't exist?


# Add several test scores for each of your students.
# Write a function that calculates a student's average score. Think about:

# What happens if a student has no scores yet?
# What mathematical operation do you need?
# How should you handle errors?


# Test your average calculation for each student.
# Create a function that converts numeric averages to letter grades. Decide on:

# What ranges correspond to which letter grades?
# How will you structure this logic?


# Part 3: Finding and Filtering (15 minutes)

# Write a function that can find a specific student by their name. Consider:

# Should the search be case-sensitive?
# What should you return if the student isn't found?
# How will you search through your data?


# Write a function that finds all students who have a specific letter grade. Think about:

# How will you determine each student's grade?
# What data structure should you return?


# Create a function that identifies the best-performing student. Consider:

# What metric defines "best"?
# What if multiple students are tied?
# What if no students have scores yet?


# Test all your search and filter functions.


# Part 4: Flexible Data Entry (10 minutes)

# Enhance your add student function to accept optional information. Think about:

# What additional information might be useful? (courses, contact info, etc.)
# How can you make some parameters optional?
# How can you accept a variable number of inputs?


# Add 2 new students using your enhanced function with various optional information.
# Write a function that displays complete details for one student. Consider:

# How will you format optional information?
# What if some information doesn't exist?


# Test your detailed display function.


# Part 5: Statistics and Analysis (15 minutes)

# Create a function that provides overall statistics about your class. Think about:

# What statistics would be useful? (total students, average performance, etc.)
# How will you calculate these across all students?
# How should you present this information?


# Write a function that analyzes grade distribution. Consider:

# How will you count students in each grade category?
# What's the best way to organize this data?


# Design a report card function for individual students. Think about:

# What information belongs on a report card?
# How should it be formatted?
# What additional insights could you provide?


# Create a function that identifies students performing above average. Consider:

# What defines "above average"?
# How will you compare individual students to the class?


# Generate reports using your statistics functions.


# Part 6: Modifying Data (10 minutes)

# Write a function that can update student information. Think about:

# What fields should be updatable?
# How will you make it flexible enough to update any field?
# What validation is needed?


# Create a function to remove a student from your system. Consider:

# How will you identify which student to remove?
# What should you return to confirm the deletion?
# What if the student doesn't exist?


# Write a function to remove individual scores. Think about:

# How will you specify which score to remove?
# What if the score doesn't exist?


# Test your update and delete functionality.


# Part 7: Advanced Features (15 minutes)

# Create a function that can sort your students by different criteria. Consider:

# What fields might users want to sort by?
# Should you support both ascending and descending order?
# How will you make this flexible?


# Design a search function that looks for keywords across multiple fields. Think about:

# Where should you search? (names, courses, details?)
# Should partial matches count?
# How will you handle case sensitivity?


# Implement a way to iterate through students one at a time efficiently. Consider:

# What Python feature is designed for this?
# Why might this be better than returning all students at once?


# Add functionality to log when important actions happen. Think about:

# What actions should be logged?
# What information should the log include?
# How can you apply this to multiple functions without repeating code?


# Create a function that exports your data to a file. Consider:

# What file format should you use?
# How should the data be structured in the file?
# What information should be included?


# Part 8: User Interface (15 minutes)

# Design a menu system for your program. Think about:

# What operations should users be able to perform?
# How should the menu be organized?
# How will you make it user-friendly?


# Write a function that gets and validates user menu choices. Consider:

# How will you ensure users enter valid options?
# What should happen with invalid input?


# Create a main program loop that uses your menu. Think about:

# How will the program flow work?
# How will users exit the program?
# How will you connect menu choices to your functions?


# Add error handling throughout your program. Consider:

# What could go wrong in each function?
# How should errors be communicated to users?
# Should the program crash or continue?


# Run your complete program and fix any issues.


# Part 9: Creative Extensions (Optional)

# Add a GPA calculation system with your own scale conversion.
# Design an early warning system to identify struggling students.
# Create a progress tracking system that analyzes trends over time.
# Implement a way to add many students at once from structured data.
# Design a backup and restore system for your data.
# Add any validation functions you think are necessary.
# Create comparison tools to analyze differences between students.
# Implement ranking or leaderboard functionality.
# Design your own unique feature that would make the system more useful.


# Final Challenge
# Build a complete, working Student Management System that:

# Stores and manages student data effectively
# Performs calculations and analysis
# Provides a user-friendly interface
# Handles errors gracefully
# Is well-organized and documented

# Think about:

# How real schools track student information
# What features would actually be useful
# How to make your code maintainable and readable
# What edge cases you need to handle

from numpy import add


students_db = []


def add_student(name: str, age: int, *subjects, **details) -> dict:
    student = {
        "id": len(students_db) + 1,
        "name": name,
        "age": age,
        "subjects": list(subjects),
        "scores": [],
        "details": details,
    }
    students_db.append(student)
    return student


student1 = add_student(
    "Alice Johnson",
    20,
    "Maths",
    "Science",
    "Geography",
    email="alice@example.com",
    phone=678678,
)
student2 = add_student(
    "Bob Smith",
    21,
    "Maths",
    "History",
    "Biology",
    email="bob@example.com",
    area="London",
)
student3 = add_student(
    "Charlie Brown",
    25,
    "Human Resources",
    "PE",
    "French",
    email="charlie@example.com",
    area="Nottingham",
)
student4 = add_student(
    "Alice Brown",
    29,
    "Science",
    "Mathematics",
    "German",
    email="alice1@example.com",
    area="Birmingham",
)
# print(student4)


def add_score(student_id: int, score: int) -> bool:
    for student in students_db:
        if student["id"] == student_id:
            student["scores"].append(score)
            return True
    return False


add_score(1, 67)
add_score(1, 92)
add_score(1, 34)

add_score(2, 17)
add_score(2, 56)
add_score(2, 99)

add_score(3, 34)
add_score(3, 67)
add_score(3, 13)


# Below will return the first record that matches
def find_student_by_name(name: str):
    search_name = name.lower().strip()
    for student in students_db:
        if search_name in student["name"].lower():
            return student
    return "Sorry, no match found.!"  # No match found


# Below will return the first record that matches
def find_all_students_by_name(name: str):
    search_name = name.lower().strip()
    matching_students = []
    for student in students_db:
        if search_name in student["name"].lower():
            matching_students.append(student)
    return matching_students


# print(find_student_by_name("Alice"))  # bob Bob
# print(345, find_all_students_by_name("Alice"))

# calculate the average of scores for each student


# 67 92 34 = 67+92+34 / 3 = average
# search into the student db
# i will see if there is any score/s
# do the sum of all the scores / length of the scores
# return the average
def calculate_average(student_id: int) -> float:
    for student in students_db:
        if student["id"] == student_id:
            scores = student["scores"]
            if scores:
                return sum(scores) / len(scores)
            return 0.0
    return 0.0


# 5, 45+56+78+90+23 /5 = answer in float
# print(calculate_average(2))


#  list all the students
# display all the student information in whatever shape
def list_all_students() -> None:
    print("\n" + "=" * 70)
    print("ALL STUDENTS".center(70))
    print("=" * 70)
    print(f"{'ID':<5} {'Name':<20} {'Age':<5} {'Avg':<8}")

    for student in students_db:
        avg = calculate_average(student["id"])
        print(f"{student['id']:<5} {student['name']:<20} {student['age']:<5} {avg:.2f}")


# list_all_students()


# top scorer student
# averge function to take
# maximum of those
# max = 0
# max = 64.33
# return the corresponding student
def find_top_student() -> dict:
    if not students_db:
        return None

    top_student = None
    highest_avg = 0

    for student in students_db:
        if student["scores"]:
            avg = calculate_average(student["id"])
            if avg > highest_avg:
                highest_avg = avg
                top_student = student
    return top_student


# print(find_top_student())

# display one student
# display a student report card
# list students above average
# remove a student from the database
# sort the students by name, age, grade
# Advanced = export_to_text file
# Advanced = save to the database
# Advanced = updates the fields of a particular student

# # 1. display one student
# student3 = add_student(
#     "Charlie Brown",
#     25,
#     "Human Resources",
#     "PE",
#     "French",
#     email="charlie@example.com",
#     area="Nottingham",
# )


def display_student(student_id: int) -> None:
    for student in students_db:
        if student["id"] == student_id:
            print("\n" + "=" * 70)
            print(f"Student ID: {student['id']}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Subjects: {", ".join(student['subjects'])}")

            if student["scores"]:
                avg = calculate_average(student_id)
                print(f"Scores: {student['scores']}")
                print(f"Average: {avg:.2f}")
            else:
                print("No scores yet")

            if student["details"]:
                print("\nAdditional Details")
                for key, value in student["details"].items():
                    print(f"{key}:  {value}")
            print("\n" + "=" * 70)
            return
    print(f"Student with ID {student_id} does not exist!")


# display_student(11)
# remove a student from the database
def remove_student(student_id: int):
    for i, student in enumerate(students_db):
        if student["id"] == student_id:
            return students_db.pop(i)
    return None


def remove_student1(student_id: int):
    for student in students_db:
        if student["id"] == student_id:

            removed_student = student  # store reference first
            students_db.remove(student)
            print(f"Student: {student_id} has been removed.")
            return removed_student
    return None


# print(remove_student1(4))
# Advanced = updates the fields of a particular student
# list_all_students()
def update_student(student_id: int, **updates):
    for student in students_db:
        if student["id"] == student_id:
            # list of fields that CAN be updated
            updateable_fields = ["name", "age", "subjects", "details"]

            for field, new_value in updates.items():
                if field in updateable_fields:
                    if field == "age":
                        if isinstance(new_value, int):
                            student[field] = new_value
            return student


print(update_student(4, age=340))  # between 16 and 100
