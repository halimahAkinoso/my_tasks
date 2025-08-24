student = {}
# add cannot be empty error handling
try:
    student['name'] = input("Enter your your name: ")
    if not student['name'].strip():
        raise ValueError("Name cannot be empty.")
    
except ValueError as e:
  print(f"Error: {e}. Please try again.")
except Exception as e:
  print("Unexpected error occur please try again.") 
  # handle invalid input error
try:
  student['age'] = int(input("Enter your age: "))
except ValueError:
  print("Invalid input for age. Please enter a   number.")  
score = [7, 85, 90]
#add score to dictionary
student['score'] = score
# average of the student score
average_score = sum(student['score'])/len(student['score']) 
student['passed'] = average_score >= 50
# to check if the student is a teenager
student['teenager'] = 13 <= student['age'] <= 19
for key, value in student.items():
  print(f"Student Name: {student['name'] }\nAge: {student['age'] }\nScores: {score}\nPassed: {student['passed']}\nTeenager: {student['teenager'] }")