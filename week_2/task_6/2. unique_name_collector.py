# collect names of people attending a seminar
# create empty set
attendees = set()
attendees.add("Khadijah")
attendees.add("Ramlah")
attendees.add("Halima")
attendees.add("Zubaydah")
attendees.add("Abd Shakur")

another_attendee = input("Enter your name:  " )
attendees.add(another_attendee)

print(attendees)

# display alphabetically
alpha_attendee = sorted(attendees)
print("Nmaes of those that attends Seminar: ", alpha_attendee)
