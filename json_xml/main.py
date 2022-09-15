import json
class Hotel(object):
    def __init__(self, name, category, phone):
        self.name = name
        self.category = category
        self.phone = phone

class Room(object):
    def __init__(self, hotel, room_number, category, price):
        self.hotel = hotel
        self.room_number = room_number
        self.category = category
        self.price = price

class  Bed(object):
    def __init__(self, room, info, price):
        self.price = price
        self.room = room
        self.info = info

class Client(object):
    def __init__(self, name, gender, birth_date, phone):
        self.name = name
        self.gender = gender
        self.birth_date = birth_date
        self.phone = phone

class Booking(object):
    def __init__(self, client, room, beds, arrival_date, staying_date, summ):
        self.client = client
        self.room = room
        self.beds = beds
        self.arrival_date = arrival_date
        self.staying_date = staying_date
        self.summ = summ

class DataBase(object):
    def __init__(self, bookings):
        self.bookings = bookings

hotel1 = Hotel('Grand Hotel', '**', '+11111111111')
room1 = Room(hotel1, '1', 'econom', 1000)
bed1 = Bed(room1, '1', 500)
bed2 = Bed(room1, '2', 500)
client1 = Client('Kamil', 'M', '01.01.2000', '+22222222222')
booking1 = Booking(client1, room1, [bed1, bed2], '10.09.2022', '11.09.2022', 2000)

hotel2 = Hotel('Grand Palace', '*****', '+33333333333')
room2 = Room(hotel2, '101', 'econom', 5000)
bed3 = Bed(room2, '', 5000)
client2 = Client('Azat', 'M', '01.01.2000', '+44444444444')
booking2 = Booking(client2, room2, [bed3], '10.09.2022', '11.09.2022', 15000)

database = DataBase([booking1, booking2])
r = json.dumps(database, default=lambda x: x.__dict__, ensure_ascii=True, indent=True)
print(r)
