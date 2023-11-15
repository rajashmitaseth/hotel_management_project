class Room:
    def __init__(self, OccupancyID:int, BedID:int, LayoutID:int, AmenitiesID:int, RoomRate:int, HousekeepingCharge:int, RoomNumber:int=None):
        self.RoomNumber = RoomNumber
        self.OccupancyID = OccupancyID
        self.BedID = BedID
        self.LayoutID = LayoutID
        self.AmenitiesID = AmenitiesID
        self.RoomRate = RoomRate
        self.HousekeepingCharge = HousekeepingCharge