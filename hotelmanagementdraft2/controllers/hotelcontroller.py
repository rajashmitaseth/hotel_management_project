from dbconnection import DBConnection
from models.hotelmodel import Hotel


def add(self, cnx):
        cursor = cnx.getcursor()
        result = cursor.execute(f"insert into hotels(HotelName, Location) values('{self.HotelName}', '{self.Location}')")
        #result = cursor.execute(f"insert into hotels(HotelName, Location) values('hotelinn', 'beach')")
        cnx.getconnection().commit()
        print(result)