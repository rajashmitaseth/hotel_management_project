from models.hotelmodel import Hotel
from dbconnection import DBConnection
import controllers.customercontroller as cus
from models.customermodel import Customer
import datetime

dbcnx = DBConnection()
# h = Hotel("Hotel1", "seabeach")
# h.savetodb(dbcnx)
# dbcnx.close()
# customer1 = Customer('Ravi', 'Singh', datetime.datetime.now(), 980336587, 'rsingh@gmail.com', 'Behala, Kolkata-66', 'Aadhar Card', 9878)
# customer2 = Customer('Soni', 'Shaw', 0, 56789025, 'sonishaw@yahoo.com', 'Delhi', 'Drivers License', 45677)
#cus.register(customer2, dbcnx)
# customers = cus.get_customers(dbcnx)
# print(customers)