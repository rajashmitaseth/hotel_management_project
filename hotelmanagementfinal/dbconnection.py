import mysql.connector

class DBConnection:
    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(user = "root", password = "1234", host = "localhost", database = "hoteldb")
        except mysql.connector.Error as err:
            print(err)

    def close(self):
        self.cnx.close()
    
    def getconnection(self):
        return self.cnx
    
    def getcursor(self):
        return self.cnx.cursor()

    def save(self):
        self.cnx.commit()
    
dbcnx = DBConnection()