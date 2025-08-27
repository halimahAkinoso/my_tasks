student = {}
name = input("Enter student's name: ")
student['name'] = name
age = input("Enter student's age: ")
student['age'] = age
# Add a list of scores to the dictionary
score =[70, 65, 85]
student['score'] = score

# Check if the student has passed (average score >= 50)
average_score = sum(score) / len(score)
student['passed'] = average_score >= 50

# Check if the student is a teenager (age between 13 and 19)
student['teenager'] = 13 <= int(age) <= 19
print(" Students Record: ")

# Print out the complete record
print(f"Student Name: {name}\nAge: {age}\nScores: {score}\nPassed: {student['passed']}\nTeenager: {student['teenager'] }")


 