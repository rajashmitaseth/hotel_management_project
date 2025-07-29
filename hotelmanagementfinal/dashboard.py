import tkinter as tk
from datetime import datetime
from PIL import ImageTk, Image
from scrollable_image import ScrollableImage
import pytz

global blue, creme, orange, adorage
blue = '#070721'
creme = '#EFC88B'
orange = '#CF5C36'
adorage = 'Adorage'

class Dashboard_Tab(tk.Frame):
    def __init__(self, notebook):
        super().__init__()
        global hello_frame, datetime_label
        self.master = notebook
        hello_frame = tk.Frame(self, background = blue)
        hello_frame.pack(fill = 'x')
        hello_label = tk.Label(hello_frame, text = "Hello User,", font = (adorage, 28), background = blue, fg = orange)
        datetime_label = tk.Label(hello_frame, background = blue, font = (adorage, 28), fg = orange)
        hello_label.pack(side = 'left', padx = 40, pady = 10)
        datetime_label.pack(side = 'right', padx = 10, pady = 10)
        Dashboard_Tab.update_clock()
        body_fame = tk.Frame(self, background = creme)
        body_fame.pack(expand = 1, fill = 'both')
        body_fame.columnconfigure((0,1,2), weight = 1, uniform = 'a')
        body_fame.rowconfigure((0), weight = 1, uniform = 'a')
        img = Image.open("hotel.jpg")
        img = img.resize((1600, 875))
        img = ImageTk.PhotoImage(img)
        img_frame = ScrollableImage(body_fame, image = img, width = 1600, height = 875)
        img_frame.pack(anchor = 'center')
        
    def update_clock():
        ist = pytz.timezone('Asia/Kolkata')
        timestamp = datetime.now(ist)
        date_now = timestamp.strftime("%d %b %Y")
        time_now = timestamp.strftime("%H:%M:%S %p")
        weekday_int = timestamp.weekday()
        weekday_dictionary = {0:"Monday", 1:"Tuseday", 2:"Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday", 6:"Sunday"}
        datetime_label.config(text = time_now + "   " + weekday_dictionary[weekday_int] + ", " + date_now)
        datetime_label.after(1000, Dashboard_Tab.update_clock)