from hotelmanagementfinal.dbconnection import dbcnx
from models.reservationsmodel import Reservation

def add(reservation:Reservation):
    cursor = dbcnx.getcursor()
    cursor.execute(f"insert into reservations(ReservationDate, CheckIn, CheckOut, People, Rooms) values({reservation.ReservationDate},{reservation.CheckIn},{reservation.CheckOut}, {reservation.People}, {reservation.Rooms})")
    dbcnx.save()

def show_reservations():
    cursor = dbcnx.getcursor()
    cursor.execute('select * from reservations order by ReservationID desc')
    all_reservations_raw = cursor.fetchall()
    all_reservations = []
    for reservation in all_reservations_raw:
        all_reservations.append(reservation)
    return all_reservations

def get_last_reservationid():
    cursor = dbcnx.getcursor()
    cursor.execute("select ReservationID from reservations order by ReservationID desc limit 1")
    return cursor.fetchone()

def get_days(reservationid):
    cursor = dbcnx.getcursor()
    cursor.execute(f"select CheckIn, CheckOut from reservations where ReservationID = {reservationid}")
    result = cursor.fetchone()
    checkin = result[0]
    checkout = result[1]
    difference = checkout - checkin
    number_of_days = int(difference.days)
    return number_of_days

def show_next_ai():
    cursor = dbcnx.getcursor()
    cursor.execute("select auto_increment from information_schema.tables where table_schema = 'hoteldb' and table_name = 'reservations'")
    next_ai = cursor.fetchone()[0]
    return next_ai

def delete_reservation(reservationid):
    cursor = dbcnx.getcursor()
    cursor.execute(f'delete from reservations where ReservationID = {reservationid}')
    dbcnx.save()

def search_reservations(search_criteria):
    cursor = dbcnx.getcursor()
    cursor.execute(f'select * from reservations where {search_criteria} order by ReservationID desc')
    return cursor.fetchall()