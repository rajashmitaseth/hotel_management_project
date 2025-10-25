import tkinter as tk
from tkinter import ttk
import pytz
from dashboard import Dashboard_Tab
from reservation import Reservation_Tab
from room import Room_Tab
from payment import Payment_Tab

global blue, orange, cream, ist, adorage
ist = pytz.timezone('Asia/Kolkata')
blue = '#070721'
creme = '#EFC88B'
orange = '#CF5C36'
adorage = 'Adorage'

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        global notebook
        self.title("Sylas Hotel")
        self.iconbitmap(default="hotelmanagementfinal/logo.ico")
        screen_height = self.winfo_screenheight()
        screen_width = self.winfo_screenwidth()
        window_width = 1600
        window_height = 900
        window_position_left = screen_width//2 - window_width//2
        window_position_top = screen_height//2 - window_height//2
        self.geometry(f'{window_width}x{window_height}+{window_position_left}+{window_position_top}')
        self.minsize(900, 500)
        notebook = ttk.Notebook(self)
        notebook.add(Dashboard_Tab(notebook), text = "Dashboard")
        notebook.add(Reservation_Tab(notebook), text = "Reservations")
        notebook.add(Payment_Tab(notebook), text = "Payments")
        notebook.add(Room_Tab(notebook), text = "Rooms")
        notebook.pack(expand = 1, fill = 'both')

if __name__ == "__main__":
    App().mainloop()