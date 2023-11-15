import mysql.connector

class DBConnection:
    def __init__(self):
        # self.cnx = mysql.connector.connect(user = "root", password = "rseth2.MYSQL", host = "localhost", database = "hoteldb")
        try:
            self.cnx = mysql.connector.connect(user = "root", password = "rseth2.MYSQL", host = "localhost", database = "hoteldb")
        except mysql.connector.Error as err:
            print(err)

    def close(self):
        self.cnx.close()
    
    def getconnection(self):
        return self.cnx
    
    def getcursor(self):
        return self.cnx.cursor()
    