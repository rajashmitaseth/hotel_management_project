from dbconnection import DBConnection
from models.amenitymodel import Amenity

def add(amenity:Amenity, db:DBConnection):
    cursor = db.getcursor()
    cursor.execute(f"insert into amenities(Description)")
    db.save()