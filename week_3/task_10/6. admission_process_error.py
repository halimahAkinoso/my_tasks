try:
  candidate_utme_score = int(input("Enter your utme score: "))
        
except ValueError:
    print("Invalid input for UTME score. Please enter a number.")
 
first_choice = input("Is your first University choice UNILAG? yes/no: ").upper()
O_level_requirement = input("Did you have five credit pass in o level including English and Mathematics? yes/ no: ").upper()
online_post_utme = input("Did you participated in the university's online post-UTME screening? yes/no: ").upper()
depart_cutt_off_mark =int(input("Enter your post utme score: "))
if candidate_utme_score >= 200:
  if first_choice:
    if O_level_requirement:
      if online_post_utme:
        if depart_cutt_off_mark <= 200 >=320:
          print("Congratulations!, you are eligible for admission")
        else:
          print("Sorry you are not eligible! Your departmental cut off mark is low")
      else:
        print("Sorry you are not eligible! You did not participated in post utme screening exercise")
    else:
      print("Sorry you are not eligible!You did not meet the olevel requirement")
  else:
    print("Sorry you are not eligible! Unilag is not your University first choice ")
else:
  print("Sorry you are not eligible!Your UTME score is below 200")

