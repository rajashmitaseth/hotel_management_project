# import sys
# sys.path.append("../hotelmanagement")

# from hotelmanagement.dbconnection import DBConnection

class Hotel:
    def __init__(self, HotelName, Location):
        self.HotelName = HotelName
        self.Location = Location
    
    def savetodb(self, cnx):
        cursor = cnx.getcursor()
        result = cursor.execute(f"insert into hotels(HotelName, Location) values('{self.HotelName}', '{self.Location}')")
        #result = cursor.execute(f"insert into hotels(HotelName, Location) values('hotelinn', 'beach')")
        cnx.getconnection().commit()
        print(result)