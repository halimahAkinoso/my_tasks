# Create a student score tracker
names = []
scores =[]
for i in range(3):
  name = input(f"Enter name of student {i+1}: ")
  score = input(f"Enter score for {name}: ")
  names.append(name)
  scores.append(score)

  print("\nStudent Scores: ")
  print("`Name\t\tScore")
  for i in range(3):
    print(f"{names[i]}\tscores[i]")

