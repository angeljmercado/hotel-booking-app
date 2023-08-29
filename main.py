import pandas

df = pandas.read_csv("hotels.csv", dtype={"id":str})
df_cards = pandas.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df_cards_security = pandas.read_csv("card_security.csv", dtype=str)

class Hotel:
    def __init__(self, hotel_id_local):
        self.hotel_id_local = hotel_id_local
        self.name = df.loc[df["id"] == self.hotel_id_local, "name"].squeeze()
        self.city = df.loc[df["id"] == self.hotel_id_local, "city"].squeeze()

    def book(self):
        """Books a hotel by changing the available field in the database to no"""
        df.loc[df["id"] == self.hotel_id_local, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Checks the database to see if the selected hotel is available"""
        check_available = df.loc[df["id"] == self.hotel_id_local, "available"].squeeze()
        if check_available == "yes":
            return True
        else:
            return False

class TicketReservation:
    def __init__(self, name_object, hotel_object):
        self.name_object = name_object
        self.hotel_object = hotel_object

    def generate(self):
        content= f"""
        Thank you for your reservation!
        Here is the booking information:
        Name: {self.name_object}
        Hotel: {self.hotel_object.name}
        City: {self.hotel_object.city}"""
        return content

class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, exp, holder_name, cvc):
        card_data = {"number": self.number, "expiration": exp, "holder": holder_name, "cvc": cvc}
        if card_data in df_cards:
            return True
        else:
            return False

class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = df_cards_security.loc[df_cards_security["number"] == self.number, "password"].squeeze()
        if password == given_password:
            return True
        else:
            return False


print(df)
hotel_id = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_id)

if hotel.available():
    credit_card = SecureCreditCard("1234")
    if credit_card.validate("12/26", "JOHN SMITH", "123"):
        if credit_card.authenticate(given_password="mypass"):
            hotel.book()
            name = input("Enter your name: ")
            reservation_ticket = TicketReservation(name, hotel)
            print(reservation_ticket.generate())
        else:
            print("Incorrect password, please try again.")
    else:
        print("There was a problem with the payment method.")
else:
    print("Hotel is not available.")
