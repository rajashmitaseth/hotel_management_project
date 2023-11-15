from dbconnection import DBConnection
from models.layoutmodel import Layout


def add(layout:Layout, db:DBConnection):
    cursor = db.getcursor()
    cursor.execute(f"insert into layouts(Description)")
    db.save()