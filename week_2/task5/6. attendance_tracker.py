#6 attendance tracker that stores days of the week
days_of_week = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")
months_of_year = ("january", "february", "march", "april", "june", "july", "august", "september", "octomber", "november", "december")

students_name = input("Enter your name: ")
gender = input("Enter your gender: ")
course_track = input("Enter your course track: ")
current_month_num = int(input("Enter month in number: "))
current_day_num  = int(input("Enter the current day in number: "))
corect_month = months_of_year[current_month_num -1]
corect_day = days_of_week[current_day_num - 1]

# print(f"Name:\t{students_name}\nGender:\t{gender}\nTrack:\t{course_track}\nmonth:\t{current_month_num}\nDay:\t{current_day_num}")

print(f"Name\t|Gender\t|courseTrack\t|MonthNumber\t|DayNumber\n{students_name}\t|{gender}\t|{course_track}\t|{current_month_num}\t|{current_day_num}")