import pandas

df = pandas.read_csv("hotels.csv")

class Hotel:
    def __init__(self, id):
        pass
    def book(self):
        pass
    def available(self):
        pass

class TicketReservation:
    def __init__(self, name, hotel):
        pass
    def generate(self):
        pass

print(df)
id = input("Enter the id of the hotel: ")
hotel = Hotel(id)
if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = TicketReservation(name, hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel is not available.")
