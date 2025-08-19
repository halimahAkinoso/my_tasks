student = {}
# Student info
age = int(input("enter your age: "))
utme_score = int(input("Enter your UTME score:"))
first_choice = input("Enter your first university choice: ").upper()
o_level = input("Did you have at least five (5) credit passes at one sitting in relevant O'Level subjects, including English Language and Mathematics?(yes/no): ")
post_utme = input("Did you participate in the university's online Post-UTME screening?Yes/No: ").title()
post_utme_score = int(input("Enter your post utme score: "))


# Add student info to the dictionary
student['Age'] = age
student['UTME Score'] = utme_score
student['University First Choice'] = first_choice 
student['The Five 0 level credit pass'] = o_level.lower() == 'yes'
student['Did UNILAG Post UTME'] = post_utme.lower() == 'yes'
student['Post - UTME score'] = post_utme_score

# calculated cutt off mark
depart_cutoff = (age>=16) and (utme_score >= 200) and (first_choice == "UNILAG") and (student['The Five 0 level credit pass']) and (student['Did UNILAG Post UTME']) and (post_utme_score >= 50)
# depart_cutoff = (age>=16) and (((utme_score + post_utme_score) / 500) * 100) >= 50


print("Applicant Eligibility Check")
print(f"Age: {age}\nUtme Score: {utme_score}\nYour University First Choice: {first_choice}\nFive O'Level Credit Pass: {student['The Five 0 level credit pass']}\nDid you participate in UNILAG Post UTME: {student['Did UNILAG Post UTME']}\nPost-UTME Score: {post_utme_score}\n\
      Eligibilty for Admission: {depart_cutoff}")