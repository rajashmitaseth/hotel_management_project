from dbconnection import DBConnection
from models.paymentmodel import Payment


def add(payment:Payment, db:DBConnection):
    cursor = db.getcursor()
    cursor.execute(f"insert into payments(PaymentDae, AmountPaid, ModeOfPayment, ReservationID)")
    db.save()

