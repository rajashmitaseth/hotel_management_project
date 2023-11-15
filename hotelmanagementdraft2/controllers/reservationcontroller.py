from dbconnection import DBConnection
from models.reservationsmodel import Reservation


def add_new_reservation(reservation:Reservation, db:DBConnection):
    cursor = db.getcursor()
    cursor.execute(f"insert into reservations(ReservationDate, CheckIn, CheckOut, Key, Purpose, CustomerID, PaymentID)")
    db.save()