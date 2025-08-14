
# # # Unique voters Registration system
registered_voters ={"Ashabi", "Arike", "Omolola"} 
# registered_voter = set()
#ask voters to enter their name
voter_name = input("Enter your name before you vote: ")
# add the name entered to the registered voter set

registered_voters.add(voter_name)


print(registered_voters)
#check if voters tries to register twice, display warning
name=voter_name
if name in registered_voters:
    print(f"{name} have already registered  and you cannot registere twice.")
else:
   registered_voters.add(voter_name)  
   print(f"{name} has succesfuly registered. Thanks")

# After registration, display the total number of unique voters.    
print(registered_voters)
print(len(registered_voters)) 



