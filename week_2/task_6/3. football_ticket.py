ranges_of_seat = range(1,51)
seat_number = set(ranges_of_seat)
print(seat_number)
#User to book by entering a number
book_seat =int( input("Enter a seat number: "))

# Remove booked seats from the seat
seat_number.remove(book_seat)
# print remaining set
print(seat_number)