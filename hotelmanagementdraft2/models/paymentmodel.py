import datetime


class Payment:
    def __init__(self, PaymentDate:datetime.datetime, AmountPaid:int, ModeOfPayment:str, ReservationID:int, PaymentID:int=None):
        self.PaymentID = PaymentID
        self.PaymentDate = PaymentDate
        self.AmountPaid = AmountPaid
        self.ModeOfPayment = ModeOfPayment
        self.ReservationID = ReservationID