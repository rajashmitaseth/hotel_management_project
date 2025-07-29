import datetime

class Payment:
    def __init__(self, ReservationID:int, PaymentDate:datetime.datetime,  AmountPaid:int, ModeOfPayment:str, PaymentID:int=None):
        self.ReservationID = ReservationID
        self.PaymentID = PaymentID
        self.PaymentDate = PaymentDate
        self.AmountPaid = AmountPaid
        self.ModeOfPayment = ModeOfPayment