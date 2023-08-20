import pandas

df = pandas.read_csv("hotels.csv")

class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        pass

    def book(self):
        pass

    def available(self):
        """Checks the database to see if the selected hotel is available"""
        check_available = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if check_available == "yes":
            return True
        else:
            return False

class TicketReservation:
    def __init__(self, name, hotel):
        pass
    def generate(self):
        pass

print(df)
hotel_id = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_id)
if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = TicketReservation(name, hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel is not available.")
