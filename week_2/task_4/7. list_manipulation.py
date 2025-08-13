# List manipulation
# create a list of five cities
cities = ["Abeokuta", "Lagos", "Ibadan", "Osogbo", "Gbogan"]
# replace third city enter by user
new_city = input("Enter new city to replace the third one: ")
cities[2] = new_city
#Remove the last city
removed_city = cities[:-1]
print(removed_city)
# add a new city to the beginning of the list
cities.insert(0,"Oyo")
# print updated list
print("Updated list of city: ", cities)
