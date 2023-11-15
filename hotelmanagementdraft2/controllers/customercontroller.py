from dbconnection import DBConnection
from models.customermodel import Customer
import datetime


def register(customer:Customer, db:DBConnection):
    cursor = db.getcursor()
    cursor.execute(f"insert into customers(FirstName, LastName, DateOfBirth, ContactNumber, Email, Address, Identification, IdentificationNumber) values('{customer.FirstName}','{customer.LastName}','2010-01-01','{customer.ContactNumber}', '{customer.Email}', '{customer.Address}', '{customer.Identification}', '{customer.IdentificationNumber}')")
    db.save()


def get_customers(db: DBConnection) -> list[Customer]:
    cursor = db.getcursor()
    cursor.execute("select * from customers")
    result = cursor.fetchall()
    customerlist = []
    for row in result:
        customerlist.append(Customer(CustomerID= row[0], FirstName= row[1], LastName= row[2], DateOfBirth= datetime.datetime.now(), ContactNumber= row[4], Email= row[5], Address= row[6], Identification= row[7], IdentificationNumber= row[8]))
    return customerlist

