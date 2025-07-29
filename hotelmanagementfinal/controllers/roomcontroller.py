from dbconnection import dbcnx
from models.roommodel import Room

def addroom(room:Room):
    cursor = dbcnx.getcursor()
    cursor.execute(f"insert into rooms(Occupancy, Bed, Layout, Amenity, RoomRate, HousekeepingCharge) values({room.Occupancy},'{room.Bed}','{room.Layout}','{room.Amenity}', {room.RoomRate}, {room.HousekeepingCharge})")
    dbcnx.save()

def get_rooms() -> list[Room]:
    cursor = dbcnx.getcursor()
    cursor.execute('select * from rooms')
    all_rooms = cursor.fetchall()
    rooms:list[Room] = []
    for room in all_rooms:
        r = Room(Record = room)
        rooms.append(r)
    return rooms

def show_rooms():
    cursor = dbcnx.getcursor()
    cursor.execute('select * from rooms order by RoomNumber desc')
    all_rooms_raw = cursor.fetchall()
    all_rooms = []
    for room in all_rooms_raw:
        all_rooms.append(room)
    return all_rooms

def delete_room(roomnumber):
    cursor = dbcnx.getcursor()
    cursor.execute(f'delete from rooms where RoomNumber = {roomnumber}')
    dbcnx.save()

def search_rooms(search_criteria):
    cursor = dbcnx.getcursor()
    cursor.execute(f'select * from rooms where {search_criteria} order by RoomNumber desc')
    return cursor.fetchall()