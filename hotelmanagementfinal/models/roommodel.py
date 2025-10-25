class Room:
    def __init__(self, Occupancy:int, Bed:str, Layout:str, Amenity:str, RoomRate:int, HousekeepingCharge:int, RoomNumber:int=None, Record:tuple=None):
        self.RoomNumber = RoomNumber
        self.Occupancy = Occupancy
        self.Bed = Bed
        self.Layout = Layout
        self.Amenity = Amenity
        self.RoomRate = RoomRate
        self.HousekeepingCharge = HousekeepingCharge    