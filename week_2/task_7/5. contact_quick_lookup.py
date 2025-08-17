#Contact Quick LookUp
#Create two tuples, store names and numbers in each tuple
#Create a function to collect a users name such that their number is displayed and Use Zip() and dict() to combine tuples and . get for retreval
user_names = ("Ramlah", "Zubaydah", "Ashabi")
user_phone_numbers = ("08056159448", "08027197966", "09065432187")
contact_info = dict(zip(user_names, user_phone_numbers))
print(contact_info)
name = input("Enter a name to search for their phone number: ")
print(contact_info.get(name, "Name not found"))