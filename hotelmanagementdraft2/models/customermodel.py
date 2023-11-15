import datetime

class Customer:
    def __init__(self, FirstName:str, LastName:str, DateOfBirth:datetime.datetime, ContactNumber:int, Email:str, Address:str, Identification:str, IdentificationNumber:int, CustomerID:int=None):
        self.CustomerID = CustomerID
        self.FirstName = FirstName
        self.LastName = LastName
        self.DateOfBirth = DateOfBirth
        self.ContactNumber = ContactNumber
        self.Email = Email
        self.Address = Address
        self.Identification = Identification
        self.IdentificationNumber = IdentificationNumber