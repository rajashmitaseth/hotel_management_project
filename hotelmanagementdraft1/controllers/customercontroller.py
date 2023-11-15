from models.customermodel import Customer



        

def register(data:{'FirstName': "", 'LastName': "", 'DateOfBirth': "", 'ContactNumber': "", 'Email': "", 'Address': "", 'Identification': "", 'IdentificationNumber': ""}):
    cus = Customer(data['FirstName'], data['LastName'], data['DateOfBirth'], data['ContactNumber'], data['Email'], data['Address'], data['Identification'], data['IdentificationNumber'])
    cursor = cnx.getcursor()
    result = cursor.execute(f"insert into customers(FirstName, LastName, DateOfBirth, ContactNumber, Email, Address, Identification, IdentificationNumber) values(
                            '{self.FirstName}', 
                            '{self.LastName}', 
                            '{self.DateOfBirth}', 
                            '{self.ContactNumber}', 
                            '{self.Email}', 
                            '{self.Address}', 
                            '{self.Identification}', 
                            '{self.IdentificationNumber}')")
    cnx.getconnection().commit()
    print(result)
