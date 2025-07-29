import datetime

class Reservation:
    def __init__(self, ReservationDate:datetime.datetime, CheckIn:datetime.datetime, CheckOut:datetime.datetime, People:int, Rooms:int, ReservationsID:int=None):
        self.ReservationID = ReservationsID
        self.ReservationDate = ReservationDate
        self.CheckIn = CheckIn
        self.CheckOut = CheckOut
        self.People = People
        self.Rooms = Rooms