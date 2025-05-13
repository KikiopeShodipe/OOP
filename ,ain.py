# Define the Class Student
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
        #Print a sentence inside the class
        print("\nStudent details;")
        print("Name:", self.name)
        print("Grade:", self.grade)
        print("Age:", self.age)
# Ask for user input
name_input = input("Enter student's name: ")
grade_input = input("Enter student's grade: ")
age_input = input("Enter student's age: ")
# Create an object of class Student using user input
student1 = Student(name_input, grade_input, age_input)