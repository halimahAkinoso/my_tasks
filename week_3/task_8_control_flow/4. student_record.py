student = {}
student['name'] = input("Enter your your name: ")
student['age'] = int(input("Enter your age: "))
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