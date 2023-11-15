from dbconnection import DBConnection
from models.bedmodel import Bed


def add(bed:Bed, db:DBConnection):
    cursor = db.getcursor()
    cursor.execute(f"insert into beds(Description)")
    db.save()