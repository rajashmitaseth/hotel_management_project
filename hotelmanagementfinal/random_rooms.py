import random
from models.roommodel import Room
import controllers.roomcontroller as roomcontroller
from hotelmanagementfinal.dbconnection import dbcnx

def create_random_rooms():
    cursor = dbcnx.getcursor()
    cursor.execute("alter table rooms auto_increment = 1")
    for i in range(50):
        o = random.randint(1,8)
        ib = ["Single", "Twin", "Double", "Double-Twin", "Double-Double", "Queen", "King"]
        il = ["Standard", "Deluxe", "Executive", "Standard-Conn", "Deluxe-Conn", "Executive-Conn", "Junior-Suite", "Master-Suite", "Presidential-Suite", "Penthouse-Suite", "Apartment-Suite",  "Villa-Suite"]
        ia = ["Pool", "Jacuzzi", "Balcony", "Terrace", "Garden"]
        br = [500, 700, 900, 1300, 1700, 1200, 1400]
        lr = [1000, 2000, 3000, 2000, 4000, 6000, 3000, 5000, 7000, 9000, 11000, 13000]
        ar = [1000, 1000, 700, 900, 1300]
        b = random.randint(0, len(ib)-1)
        a = random.randint(0, len(ia)-1)
        l = random.randint(0, len(il)-1)
        r = int(br[b] + lr[l] + ar[a])
        hr = r * (30/100)
        rr = r + hr
        room = Room(Occupancy = o, Bed = ib[b], Layout = il[l], Amenity = ia[a], RoomRate = rr, HousekeepingCharge = hr)
        roomcontroller.addroom(room)

create_random_rooms()