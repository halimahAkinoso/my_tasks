# STUDENTS BIO DATA

# Collect students bio data  form user input
name =input("Please enter your Name:  ")
age = int(input("Please enter your Age:  "))
gender =input("Please enter your Sex:  ")
courses =input("Please enter your course of stu dy:  ")

students_bio = dict(
  name = name,
  age =  age,
  gender = gender,  
  course =courses
)
# print(students_bio)
print(f"Student Bio Data \n============== \nName = {name}\nAge = {age}\nGender = {gender}\nCourses = {courses}")
