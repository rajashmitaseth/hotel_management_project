from dbconnection import DBConnection
from models.occupancymodel import Occupancy


def add(occupancy:Occupancy, db:DBConnection):
    cursor = db.getcursor()
    cursor.execute(f"insert into occupancy(Description)")
    db.save