from models.hotelmodel import Hotel
from dbconnection import DBConnection

dbcnx = DBConnection()
h = Hotel("Hotel1", "seabeach")

h.savetodb(dbcnx)
dbcnx.close()