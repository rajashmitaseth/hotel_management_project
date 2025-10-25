import tkinter as tk
from tkinter import ttk
from hotelmanagementfinal.dbconnection import dbcnx
from models.roommodel import Room
import controllers.roomcontroller as roomcontroller

import random

global blue, creme, orange, adorage
orange = '#070721'
creme = '#EFC88B'
blue = '#CF5C36'
adorage = 'Adorage'

class Room_Tab(tk.Frame):
    def __init__(self, notebook):
        super().__init__()
        global rooms_table, bed_chosen, layout_chosen, amenity_chosen, housekeeping_charge, room_rate_display, bed, layout, amenity, occupancy, room_rate_label, housekeeping_charge_label, rooms_search_entry
        self.master = notebook
        self.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17), weight = 1, uniform = 'a')
        self.columnconfigure((0,1,2), weight = 1, uniform = 'a')
        rooms_input_frame = tk.Frame(self, background = orange)
        rooms_input_frame.grid(row = 0, rowspan = 18, column = 0, sticky = 'nsew')
        rooms_input_frame.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19), weight = 1, uniform = 'a')
        rooms_input_frame.columnconfigure((0,1,2), weight = 1, uniform = 'a')
        rooms_display_frame = tk.Frame(self, background = blue)
        rooms_display_frame.grid(row = 0, rowspan = 18, column = 1, columnspan = 2, sticky = 'nsew')
        tk.Label(rooms_input_frame, background = orange, font = (adorage, 14), fg = creme, text = "Occupancy:").grid(row = 2, column = 0, sticky = 'e')
        occupancy = ttk.Spinbox(rooms_input_frame, background = creme, font = (adorage, 14), foreground = blue, from_ = 1, to = 8, state = 'readonly')
        occupancy.grid(row = 2, column = 1, columnspan = 2, sticky = 'nsew', padx = 10, pady = 5, ipadx = 10)
        tk.Label(rooms_input_frame, background = orange, font = (adorage, 14), fg = creme, text = "Bed:").grid(row = 3, column = 0, sticky = 'e')
        bed_chosen = tk.StringVar()
        bed = ttk.Combobox(rooms_input_frame, font = (adorage, 14), textvariable = bed_chosen, values = ["Single", "Twin", "Double", "Double-Twin", "Double-Double", "Queen", "King"], state = 'readonly')   # ["Single" = 500,"Twin" = 700, "Double" = 900, "Double-Twin" = 1300, "Double-Double" = 1700, "Queen" = 1200, "King" = 1400]
        bed.grid(row = 3, column = 1, columnspan = 2, sticky = 'nsew', padx = 10, pady = 5, ipadx = 10)
        bed.current(0)
        tk.Label(rooms_input_frame, background = orange, font = (adorage, 14), fg = creme, text = "Layout:").grid(row = 4, column = 0, sticky = 'e')
        layout_chosen = tk.StringVar()
        layout = ttk.Combobox(rooms_input_frame, font = (adorage, 14), textvariable = layout_chosen, values = ["Standard", "Deluxe", "Executive", "Standard-Conn", "Deluxe-Conn", "Executive-Conn", "Junior-Suite", "Master-Suite", "Presidential-Suite", "Penthouse-Suite", "Apartment-Suite",  "Villa-Suite"], state = 'readonly')  # ["Standard" = 1000, "Deluxe" = 2000, "Executive" = 3000, "Standard-Connecting" = 2000, "Deluxe-Connecting" = 4000, "Executive-Connecting" = 6000, "Junior-Suite" = 3000, "Master-Suite" = 5000, "Presidential-Suite" = 7000, "Penthouse-Suite" = 9000, "Apartment-Suite" = 11000, "Villa-Suite" = 13000]
        layout.grid(row = 4, column = 1, columnspan = 2, sticky = 'nsew', padx = 10, pady = 5, ipadx = 10)
        layout.current(0)
        tk.Label(rooms_input_frame, background = orange, font = (adorage, 14), fg = creme, text = "Amenity:").grid(row = 5, column = 0, sticky = 'e')
        amenity_chosen = tk.StringVar()
        amenity = ttk.Combobox(rooms_input_frame, font = (adorage, 14), textvariable = amenity_chosen, values = ["Pool", "Jacuzzi", "Balcony", "Terrace", "Garden"], state = 'readonly')    # ["Pool" = 1000, "Jacuzzi" = 1000, "Balcony" = 700, "Terrace" = 900, "Garden" = 1300]
        amenity.grid(row = 5, column = 1, columnspan = 2, sticky = 'nsew', padx = 10, pady = 5, ipadx = 10)
        amenity.current(0)
        tk.Label(rooms_input_frame, justify = 'right', background = orange, font = (adorage, 14), fg = creme, text = "Housekeeping\nCharge (in Rs.):").grid(row = 16, column = 0, sticky = 'e')   # 30% of room rate
        housekeeping_charge = tk.StringVar()
        housekeeping_charge_label = tk.Label(rooms_input_frame, background = orange, font = (adorage, 14), fg = creme, textvariable = housekeeping_charge)
        housekeeping_charge_label.grid(row = 16, column = 1, columnspan = 2, sticky = 'nsew', padx = 10, pady = 5, ipadx = 10)
        bed_chosen.trace('w', self.calculate_room_rate)
        layout_chosen.trace('w', self.calculate_room_rate)
        amenity_chosen.trace('w', self.calculate_room_rate)
        tk.Label(rooms_input_frame, background = orange, font = (adorage, 14), fg = creme, text = "Room Rate (in Rs.): ").grid(row = 17, column = 0, sticky = 'e')
        room_rate_display = tk.StringVar()
        room_rate_label = tk.Label(rooms_input_frame, background = orange, font = (adorage, 14), fg = creme, textvariable = room_rate_display)
        room_rate_label.grid(row = 17, column = 1, columnspan = 2, sticky = 'nsew', padx = 10, pady = 5, ipadx = 10)
        tk.Button(rooms_input_frame, background = blue, font = (adorage, 24), foreground = creme, text = "Show All", command = self.refresh_rooms).grid(row = 18, rowspan = 2, column = 2, sticky = 'nsew', padx = 10, pady = 10)
        tk.Button(rooms_input_frame, background = blue, font = (adorage, 24), foreground = creme, text = "Add", command = self.create_room).grid(row = 18, rowspan = 2, column = 1, sticky = 'nsew', padx = 10, pady = 10)
        tk.Button(rooms_input_frame, background = blue, font = (adorage, 24), foreground = creme, text = "Delete", command = self.delete_rooms).grid(row = 18, rowspan = 2, column = 0, sticky = 'nsew', padx = 10, pady = 10)
        rooms_display_frame.rowconfigure((0), weight = 1)
        rooms_display_frame.rowconfigure((1), weight = 20)
        rooms_display_frame.columnconfigure((0), weight = 1)
        rooms_search_frame = tk.Frame(rooms_display_frame, background = creme)
        rooms_search_frame.grid(row = 0, column = 0, sticky = 'nsew')
        rooms_search_frame.rowconfigure((0), weight = 1)
        rooms_search_frame.columnconfigure((0), weight = 5)
        rooms_search_frame.columnconfigure((1), weight = 1)
        default_text = tk.StringVar()
        default_text.set("Search query, eg. Occupancy = 3")
        rooms_search_entry = tk.Entry(rooms_search_frame, font = (adorage, 14), foreground = orange, textvariable = default_text)
        rooms_search_entry.grid(row = 0, column = 0, sticky = 'ew', padx = 10)
        rooms_search_button = tk.Button(rooms_search_frame, font = (adorage, 14), text = "Search", background = blue, foreground = creme, command = self.search_rooms)
        rooms_search_button.grid(row = 0, column = 1, sticky = 'ew', padx = 5)
        room_table_frame = tk.Frame(rooms_display_frame, background = creme)
        room_table_frame.grid(row = 1, column = 0, sticky = 'nsew')
        rooms_table = ttk.Treeview(room_table_frame, selectmode = 'browse', columns = [0,1,2,3,4,5, 6], show = 'headings')
        rooms_table.pack(expand = 1, fill = 'y')
        room_table_scrollbarh = tk.Scrollbar(room_table_frame, orient = 'horizontal', command = rooms_table.xview)
        room_table_scrollbarh.pack(fill = 'x')
        rooms_table.config(xscrollcommand = room_table_scrollbarh.set)
        rooms_table.heading(column = 0, anchor = 'w', text = "RoomID")
        rooms_table.heading(column = 1, anchor = 'w', text = "Occupancy")
        rooms_table.heading(column = 2, anchor = 'w', text = "Bed")
        rooms_table.heading(column = 3, anchor = 'w', text = "Layout")
        rooms_table.heading(column = 4, anchor = 'w', text = "Amenity")
        rooms_table.heading(column = 5, anchor = 'w', text = "RoomRate")
        rooms_table.heading(column = 6, anchor = 'w', text = "HousekeepingCharge")
        self.get_rooms(rooms_table)        

    def create_room(self):
        room = Room(Occupancy = occupancy.get(), Bed = bed_chosen.get(), Layout = layout_chosen.get(), Amenity = amenity_chosen.get(), RoomRate = int(room_rate_label.cget("text")), HousekeepingCharge = int(housekeeping_charge_label.cget("text")))
        roomcontroller.addroom(room)
        self.refresh_rooms()
        
    
    def refresh_rooms(self):
        for room in rooms_table.get_children():
            rooms_table.delete(room)
        self.get_rooms(rooms_table)

    def get_rooms(self, table):
        all_rooms_data = roomcontroller.show_rooms()
        for room_data in all_rooms_data:
            table.insert(parent = '', index = 0, values = room_data)
    
    def get_roomnumber(self, table):
        for record in table.selection():
            selected_roomnumber = table.item(record)['values'][0]
        return selected_roomnumber

    def delete_rooms(self):
        roomnumber = self.get_roomnumber(table = rooms_table)
        roomcontroller.delete_room(roomnumber)
        self.refresh_rooms()

    def search_rooms(self):
        search_criteria = rooms_search_entry.get()
        search_results_raw = roomcontroller.search_rooms(search_criteria)
        search_results = []
        for search_result in search_results_raw:
            search_results.append(search_result)
        for room in rooms_table.get_children():
            rooms_table.delete(room)
        for result in search_results:
            rooms_table.insert(parent = '', index = 0, values = result)

    def calculate_room_rate(*args):
        bed_chosen.get()
        layout_chosen.get()
        amenity_chosen.get()
        bed_rates = [500, 700, 900, 1300, 1700, 1200, 1400]
        bed_rate = bed_rates[bed.current()]
        layout_rates = [1000, 2000, 3000, 2000, 4000, 6000, 3000, 5000, 7000, 9000, 11000, 13000]
        layout_rate = layout_rates[layout.current()]
        amenity_rates = [1000, 1000, 700, 900, 1300]
        amenity_rate = amenity_rates[amenity.current()]
        room_rate_without_housekeeping = int(bed_rate + layout_rate + amenity_rate)
        housekeeping_rate = int(room_rate_without_housekeeping*(15/100))
        housekeeping_charge.set(housekeeping_rate)
        room_rate = int(room_rate_without_housekeeping + housekeeping_rate)
        room_rate_display.set(room_rate)
