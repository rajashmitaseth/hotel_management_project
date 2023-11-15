import datetime


class Reservation:
    def __init__(self, ReservationDate:datetime.datetime, CheckIn:datetime.datetime, CheckOut:datetime.datetime, Key:bool, Purpose:str, CustomerID:int, PaymentID:int, ReservationsID:int=None):
        self.ReservationID = ReservationsID
        self.ReservationDate = ReservationDate
        self.CheckIn = CheckIn
        self.CheckOut = CheckOut
        self.Key = Key
        self.Purpose = Purpose
        self.CustomerID = CustomerID
        self.PaymentID = PaymentID