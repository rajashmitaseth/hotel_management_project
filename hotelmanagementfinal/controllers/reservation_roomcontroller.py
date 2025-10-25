from hotelmanagementfinal.dbconnection import dbcnx
from models.reservations_roomsmodel import Reservation_Room

def add(reservation_room:Reservation_Room):
    cursor = dbcnx.getcursor()
    cursor.execute(f"insert into reservations_rooms(ReservationID, RoomNumber) values({reservation_room.ReservationID}, {reservation_room.RoomNumber})")
    dbcnx.save()

def show_reservations_rooms():
    cursor = dbcnx.getcursor()
    cursor.execute('select * from reservations_rooms')
    all_reservations_rooms_raw = cursor.fetchall()
    all_reservations_rooms = []
    for reservation_room in all_reservations_rooms_raw:
        all_reservations_rooms.append(reservation_room)
    return all_reservations_rooms

def get_room_details(reservationid):
    cursor = dbcnx.getcursor()
    cursor.execute(f'select rooms.* from reservations_rooms inner join reservations on reservations_rooms.ReservationID = reservations.ReservationID inner join rooms on reservations_rooms.RoomNumber = rooms.RoomNumber where reservations.ReservationID = {reservationid}')
    return cursor.fetchall()

def get_arrivals(today):
    cursor = dbcnx.getcursor()
    cursor.execute(f"select reservations.ReservationID, rooms.RoomNUmber from reservations_rooms inner join reservations on reservations_rooms.ReservationID = reservations.ReservationID inner join rooms on reservations_rooms.RoomNumber = rooms.RoomNumber where reservations.CheckIn = {today} order by reservations.ReservationID desc")
    return cursor.fetchall()

def get_departures(today):
    cursor = dbcnx.getcursor()
    cursor.execute(f"select reservations.ReservationID, rooms.RoomNUmber from reservations_rooms inner join reservations on reservations_rooms.ReservationID = reservations.ReservationID inner join rooms on reservations_rooms.RoomNumber = rooms.RoomNumber where reservations.CheckOut = {today} order by reservations.ReservationID desc")
    return cursor.fetchall()

def get_inhouse(today):
    cursor = dbcnx.getcursor()
    cursor.execute(f"select reservations.ReservationID, rooms.RoomNUmber from reservations_rooms inner join reservations on reservations_rooms.ReservationID = reservations.ReservationID inner join rooms on reservations_rooms.RoomNumber = rooms.RoomNumber where {today} between reservations.CheckIn and reservations.CheckOut order by reservations.ReservationID desc")
    return cursor.fetchall()