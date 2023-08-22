import pandas

df = pandas.read_csv("hotels.csv", dtype={"id":str})

class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Books a hotel by changing the available field in the database to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Checks the database to see if the selected hotel is available"""
        check_available = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if check_available == "yes":
            return True
        else:
            return False

class TicketReservation:
    def __init__(self, name, hotel):
        self.name = name
        self.hotel = hotel

    def generate(self):
        content= f"""
        Thank you for your reservation!
        Here is the booking information:
        Name: {self.name}
        Hotel: {self.hotel.name}"""
        return content


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
