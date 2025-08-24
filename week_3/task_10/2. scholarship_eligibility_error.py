name = input("Enter your name: ")
try:
  age = int(input("Enter your age: "))
except ValueError:
  print("Invalid input for age. Please enter a valid number: ")
  exit()

is_nig_citizenship = input("Are you a citizen of NIGERIA?(yes or No): ").upper()
full_enrollment = input("Are you a registered, full-time undergraduate student in Nigeria university?(yes/No): ").upper()
on_other_scholarship = input("Are you currently receiving any scholarship from oil and gas industry, either national of international?Yes/no: ").upper()
academic_qualification = input("Do you have five distinctions(As and Bs)in relevant subjects including English and Mathematics? Yes/No: ")
# print(citizenship)
if is_nig_citizenship:
  if full_enrollment:
    if academic_qualification:
      if not on_other_scholarship:
        print("Congratulations! you are eligible for federal government scholarship")
      else:
        print("Sorry !You are not eligible,you are currently receiving scholarship")
    else:
      print("Sorry !You are not eligible,you are not qualify academically")
  else:
    print("Sorry !You are not eligible,you are not full time registered in Nigeria university")
else:
  print("Sorry! You are not eligible,you are not Nigerian citizenship")

