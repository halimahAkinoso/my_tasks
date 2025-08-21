# the code allows user to enter their name, age and score
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# score = int(input("Enter your test score: "))

# # condition for the eligibilty 
# eligibility = (age < 18) and (score > 70)
# # print  out candidate eligibility status with their details c
# print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")


# this code check candidate eligibility based on specify requirements
#eligibility requirement include :
#CITIZENSHIP : MUST BE A CITIZEN OF nIGERIA
# Enrollment : must be reistered , full term undergraduate in Nigeria uni
#others scholarships: cannot be currently receiving any other 
# scholarshipan enettity in the oil and gas industry
# Academy Qualification: for under garduate courses applicant usually need five distintions
# (As or Bs) in their waec eaxms including English and mathematics


# Get candidate personal information
name = input("Enter your name: ")
age = int(input("Enter your age: "))
score = int(input("Enter your test score: "))

# Get scholarship specific information
citizenship = input("Are you a citizen of Nigeria? (yes/no): ").lower()
enrollment = input("Are you a registered, full-time undergraduate student in a recognised Nigeria University?(yes/no): ").lower()
other_scholarships = input("Are you currently receiving scholarship from oil and gas industry?(yes/no): ").lower()
academic_qualifcation = input("Do you have (As and Bs) in waec including English and Maths?(yes/no): ").lower()

# Evaluate eligibility baesd on all criterias

is_citizenship = (citizenship == "yes")
is_enrolled = (enrollment == "yes")
no_other_scholarships = (other_scholarships == "no")
meet_academic_qualifica = (academic_qualifcation == "yes")

all_eligibility = is_citizenship and is_enrolled and no_other_scholarships and meet_academic_qualifica and (score > 70)
 # print candidate information and eligibility status

print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {all_eligibility}")
