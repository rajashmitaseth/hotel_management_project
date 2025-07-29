import tkinter as tk

class ScrollableImage(tk.Frame):
    def __init__(self, master=None, **kw):
        self.image = kw.pop('image', None)
        sw = kw.pop('scrollbarwidth', 10)
        super(ScrollableImage, self).__init__(master=master, **kw)
        self.cnvs = tk.Canvas(self, highlightthickness=0, **kw)
        self.cnvs.create_image(0, 0, anchor='nw', image=self.image)
        self.v_scroll = tk.Scrollbar(self, orient='vertical', width=sw)
        self.cnvs.grid(row=0, column=0,  sticky='nsew')