day_of_weeks = ("Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
mon_activity = input("Enter activities for Monday: ")
tue_activity = input("Enter activities for Tuesday: ")
wed_activity = input("Enter activities for Monday: ")
days_and_activ = {
   day_of_weeks[0]:"domestic work",
  day_of_weeks[1]: mon_activity,  
  day_of_weeks[2]:tue_activity, 
  day_of_weeks[3]: wed_activity,
  day_of_weeks[4]: "revision",
  day_of_weeks[5] :"exercise",
  day_of_weeks[6]:"outing"
}
print(days_and_activ)