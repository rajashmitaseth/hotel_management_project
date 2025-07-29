import tkinter as tk
from tkinter import ttk
from datetime import datetime
import tkcalendar
import subprocess
from models.paymentmodel import Payment
import controllers.reservationcontroller as reservationcontroller
import controllers.reservation_roomcontroller as reservation_roomcontroller
import controllers.paymentcontroller as paymentcontroller
from reservation import Reservation_Tab
import pytz

global blue, orange, cream, ist, adorage
ist = pytz.timezone('Asia/Kolkata')
orange = '#070721'
creme = '#EFC88B'
blue = '#CF5C36'
adorage = 'Adorage'

class Payment_Tab(tk.Frame):
    def __init__(self, notebook):
        super().__init__()
        global payments_table, payment_reservation_table, reservationid_label_var, payments_bill, quantity, current_quantity, item, item_chosen, current_price, amount_payable, add_button, delete_button, mode_chosen, payment_date, mode, payments_search_entry
        self.master = notebook
        self.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17), weight = 1, uniform = 'a')
        self.columnconfigure((0,1,2), weight = 1, uniform = 'a')
        payments_input_frame = tk.Frame(self, background = orange)
        payments_input_frame.grid(row = 0, rowspan = 18, column = 0, sticky = 'nsew')
        payments_input_frame.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19), weight = 1, uniform = 'a')
        payments_input_frame.columnconfigure((0,1,2), weight = 1, uniform = 'a')
        payments_display_frame = tk.Frame(self, background = blue)
        payments_display_frame.grid(row = 0, rowspan = 18, column = 1, columnspan = 2, sticky = 'nsew')
        tk.Label(payments_input_frame, background = orange, font = (adorage, 14), fg = creme, text = "Reservation ID:").grid(row = 2, column = 0, sticky = 'e')
        reservationid_label_var = tk.StringVar()
        reservationid_label_var.set("(double click on reservation)")
        reservationid_label = tk.Label(payments_input_frame, background = orange, foreground = creme, font = (adorage, 14), textvariable = reservationid_label_var)
        reservationid_label.grid(row = 2, column = 1, columnspan = 2, sticky = 'nsew', padx = 10, pady = 5, ipadx = 10)
        tk.Label(payments_input_frame, background = orange, font = (adorage, 14), fg = creme, text = "Payment Date:").grid(row = 3, column = 0, sticky = 'e')
        payment_date = tkcalendar.DateEntry(payments_input_frame, selectmode = 'day', background = creme, foreground = orange, font = (adorage, 12))
        payment_date.grid(row = 3, column = 1, columnspan = 2, sticky = 'nsew', padx = 10, pady = 5, ipadx = 10)
        payment_date['state'] = 'disabled'
        payment_date.set_date(datetime.now(ist).strftime("%x"))
        tk.Label(payments_input_frame, background = orange, font = (adorage, 14), foreground = creme, text = "-------------------------------------------------------------------------------------").grid(row = 4, column = 0, columnspan = 3, sticky = 'nsew', pady = 10)
        tk.Label(payments_input_frame, background = orange, font = (adorage, 14), fg = creme, text = "Item: ").grid(row = 5, column = 0, sticky = 'e')
        item_chosen = tk.StringVar()
        item = ttk.Combobox(payments_input_frame, font = (adorage, 14), textvariable = item_chosen, values = ["Lunch (Veg, Serves 1)", "Lunch (Non-Veg, Serves 1)", "Dinner (Veg, Serves 1)", "Dinner (Non-Veg, Serves 1)", "Tea", "Coffee", "Cold Drinks (1L)", "Hot Drinks", "Packaged Water (1L)", "Snacks", "Parking", "Gym", "Laundry"], state = 'readonly')  # ["Lunch (Veg)" = 500, "Lunch (Non-Veg)" = 600, "Dinner (Veg)" = 500, "Dinner (Non-Veg)" = 600, "Tea" = 6, "Coffee" = 7, "Cold Drinks (1L)" = 50, "Hot Drinks" = 1500, "Packaged Water (1L)" = 20, "Snacks" = 70, "Parking (per day)" = 20, "Gym" = 100, "Laundry" = 200]
        item.grid(row = 5, column = 1, columnspan = 2, sticky = 'nsew', padx = 10, pady = 5, ipadx = 10)
        item.current(0)
        tk.Label(payments_input_frame, background = orange, font = (adorage, 14), fg = creme, text = "Quantity: ").grid(row = 6, column = 0, sticky = 'e')
        current_quantity = tk.IntVar()
        current_quantity.set(1)
        quantity = ttk.Spinbox(payments_input_frame, background = creme, font = (adorage, 14), foreground = blue, from_ = 1, to = 9, state = 'readonly', textvariable = current_quantity)
        quantity.grid(row = 6, column = 1, columnspan = 2, sticky = 'nsew', padx = 10, pady = 5, ipadx = 10)
        tk.Label(payments_input_frame, background = orange, font = (adorage, 14), fg = creme, text = "Price: ").grid(row = 7, column = 0, sticky = 'e')
        current_price = tk.StringVar()
        price = tk.Label(payments_input_frame, background = orange, font = (adorage, 14), fg = creme, textvariable = current_price)
        price.grid(row = 7, column = 1, columnspan = 2, sticky = 'nsew', padx = 10, pady = 5, ipadx = 10)
        current_quantity.trace('w', self.get_price)
        item_chosen.trace('w', self.get_price)
        self.get_price()
        add_button = tk.Button(payments_input_frame, background = blue, font = (adorage, 14), foreground = creme, text = "Add Item", command = self.add_item)
        add_button.grid(row = 8, rowspan = 1, column = 2, sticky = 'nsew', padx = 10, pady = 2)
        delete_button = tk.Button(payments_input_frame, background = blue, font = (adorage, 14), foreground = creme, text = "Delete Item", command = self.delete_item)
        delete_button.grid(row = 8, rowspan = 1, column = 1, sticky = 'nsew', padx = 10, pady = 2)
        tk.Label(payments_input_frame, background = orange, font = (adorage, 14), foreground = creme, text = "-------------------------------------------------------------------------------------").grid(row = 9, column = 0, columnspan = 3, sticky = 'nsew', pady = 10)
        amount_payable = tk.StringVar()
        tk.Label(payments_input_frame, background = orange, font = (adorage, 14), fg = creme, text = "Amount Payable").grid(row = 10, column = 0, sticky = 'e')
        tk.Label(payments_input_frame, background = orange, font = (adorage, 14), fg = creme, textvariable = amount_payable).grid(row = 10, column = 1, columnspan = 2, sticky = 'nsew')
        tk.Label(payments_input_frame, background = orange, font = (adorage, 14), fg = creme, text = "Mode of Payment:").grid(row = 11, column = 0, sticky = 'e')
        mode_chosen = tk.StringVar()
        mode_chosen.set(0)
        mode = ttk.Combobox(payments_input_frame, font = (adorage, 14), textvariable = mode_chosen, values = ["Cash", "Net Banking", "Credit Card", "Debit Card", "Cheque", "UPI"], state = 'readonly')
        mode.grid(row = 11, column = 1, columnspan = 2, sticky = 'nsew', padx = 10, pady = 5, ipadx = 10)
        mode.current(0)
        tk.Button(payments_input_frame, background = blue, font = (adorage, 24), foreground = creme, text = "Get Bill", command = self.get_bill).grid(row = 16, rowspan = 2, column = 1, sticky = 'nsew', padx = 10, pady = 10)
        tk.Button(payments_input_frame, background = blue, font = (adorage, 24), foreground = creme, text = "Refresh", command = self.refresh_payments).grid(row = 18, rowspan = 2, column = 2, sticky = 'nsew', padx = 10, pady = 10)
        tk.Button(payments_input_frame, background = blue, font = (adorage, 24), foreground = creme, text = "Add", command = self.create_payment).grid(row = 18, rowspan = 2, column = 1, sticky = 'nsew', padx = 10, pady = 10)
        tk.Button(payments_input_frame, background = blue, font = (adorage, 24), foreground = creme, text = "Delete", command = self.delete_payment).grid(row = 18, rowspan = 2, column = 0, sticky = 'nsew', padx = 10, pady = 10)
        payments_display_frame.rowconfigure((0), weight = 1)
        payments_display_frame.rowconfigure((1, 2), weight = 10)
        payments_display_frame.columnconfigure((0, 1), weight = 1, uniform = 'a')
        payments_search_frame = tk.Frame(payments_display_frame, background = creme)
        payments_search_frame.grid(row = 0, column = 1, sticky = 'nsew')
        payments_search_frame.rowconfigure((0), weight = 1)
        payments_search_frame.columnconfigure((0), weight = 3)
        payments_search_frame.columnconfigure((1), weight = 1)
        default_text = tk.StringVar()
        default_text.set("Search query")
        payments_search_entry = tk.Entry(payments_search_frame, font = (adorage, 14), foreground = orange, textvariable = default_text)
        payments_search_entry.grid(row = 0, column = 0, sticky = 'ew', padx = 10)
        payments_search_button = tk.Button(payments_search_frame, font = (adorage, 14), text = "Search", background = blue, foreground = creme, command = self.search_payment)
        payments_search_button.grid(row = 0, column = 1, sticky = 'ew', padx = 5)
        payments_bill_frame = tk.Frame(payments_display_frame, background = blue)
        payments_bill_frame.grid(row = 0, rowspan = 3, column = 0, sticky = 'nsew')
        payments_bill = tk.Listbox(payments_bill_frame, font = ('DejaVu Sans Mono', 14), justify = 'center', selectmode = 'browse')
        payments_bill.place(relheight = 1, relwidth = 1)
        bill_date_time = datetime.now(ist).strftime("%a %x %X")
        payments_bill.insert(0,  "")
        payments_bill.insert(1,  "SYLAS HOTEL")
        payments_bill.insert(2,  "Adress")
        payments_bill.insert(3,  "Contact No.: +911234567890")
        payments_bill.insert(4,  "E-mail: contact.sylashotel@gmail.com")
        payments_bill.insert(5,  "----------------------------------------")
        payments_bill.insert(6,  "RECEIPT")
        payments_bill.insert(7,  bill_date_time)
        payments_bill.insert(8,  "PaymentID:")
        payments_bill.insert(9,  "ReservationID:")
        payments_bill.insert(10, "----------------------------------------")
        payments_bill.insert(11, "Qty   Item                    Price (Rs.)")
        payments_bill.insert(12, "1   Free Wifi                       0")
        payments_table_frame = tk.Frame(payments_display_frame, background = creme)
        payments_table_frame.grid(row = 1, column = 1, sticky = 'nsew')
        payments_table = ttk.Treeview(payments_table_frame, selectmode = 'browse', columns = [0,1,2,3,4], show = 'headings')
        payments_table.place(relheight = 1, relwidth = 1)
        payments_table_scrollbarv = tk.Scrollbar(payments_table_frame, orient = 'vertical', command = payments_table.yview)
        payments_table_scrollbarv.pack(side = 'right', fill = 'y')
        payments_table.config(yscrollcommand = payments_table_scrollbarv.set)
        payments_table_scrollbarh = tk.Scrollbar(payments_table_frame, orient = 'horizontal', command = payments_table.xview)
        payments_table_scrollbarh.pack(side = 'bottom', fill = 'x')
        payments_table.config(xscrollcommand = payments_table_scrollbarh.set)
        payments_table.heading(column = 0, anchor = 'w', text = "PaymentID")
        payments_table.heading(column = 1, anchor = 'w', text = "ReservationID")
        payments_table.heading(column = 2, anchor = 'w', text = "PaymentDate")
        payments_table.heading(column = 3, anchor = 'w', text = "AmountPayable")
        payments_table.heading(column = 4, anchor = 'w', text = "ModeOfPayment")
        self.get_payments()  
        payment_reservation_table_frame = tk.Frame(payments_display_frame, background = creme)
        payment_reservation_table_frame.grid(row = 2, column = 1, sticky = 'nsew')
        payment_reservation_table = ttk.Treeview(payment_reservation_table_frame, selectmode = 'browse', columns = [0,1,2,3,4,5], show = 'headings')
        payment_reservation_table.place(relheight = 1, relwidth = 1)
        payment_reservation_table_scrollbarv = tk.Scrollbar(payment_reservation_table_frame, orient = 'vertical', command = payment_reservation_table.yview)
        payment_reservation_table_scrollbarv.pack(side = 'right', fill = 'y')
        payment_reservation_table.config(yscrollcommand = payment_reservation_table_scrollbarv.set)
        payment_reservation_table_scrollbarh = tk.Scrollbar(payment_reservation_table_frame, orient = 'horizontal', command = payment_reservation_table.xview)
        payment_reservation_table_scrollbarh.pack(side = 'bottom', fill = 'x')
        payment_reservation_table.config(xscrollcommand = payment_reservation_table_scrollbarh.set)
        payment_reservation_table.heading(column = 0, anchor = 'w', text = "ReservationID")
        payment_reservation_table.heading(column = 1, anchor = 'w', text = "ReservationDate")
        payment_reservation_table.heading(column = 2, anchor = 'w', text = "CheckIn")
        payment_reservation_table.heading(column = 3, anchor = 'w', text = "CheckOut")
        payment_reservation_table.heading(column = 4, anchor = 'w', text = "People")
        payment_reservation_table.heading(column = 5, anchor = 'w', text = "Rooms")
        Reservation_Tab.get_reservations(self, payment_reservation_table)
        payment_reservation_table.selection_set(payment_reservation_table.get_children()[-1])
        self.choose_reservationid()
        payment_reservation_table.bind("<ButtonRelease-1>", self.choose_reservationid)

    def search_payment(self):
        search_criteria = payments_search_entry.get()
        search_results_raw = paymentcontroller.search_payment(search_criteria)
        search_results = []
        for search_result in search_results_raw:
            search_results.append(search_result)
        for payment in payments_table.get_children():
            payments_table.delete(payment)
        for result in search_results:
            payments_table.insert(parent = '', index = 0, values = result)

    def get_payments(self):
        all_payments_data = paymentcontroller.show_payments()
        for payment_data in all_payments_data:
            payments_table.insert(parent = '', index = 0, values = payment_data)

    def choose_reservationid(self, *args):
        add_button['state'] = 'active'
        delete_button['state'] = 'active'
        payment_date.set_date(datetime.now(ist).strftime("%x"))
        mode['state'] = 'active'
        payments_bill.delete(13, 'end')
        reservationid = int()
        for record in payment_reservation_table.selection():
            reservationid = payment_reservation_table.item(record)['values'][0]
        reservationid_label_var.set(reservationid)
        payments_bill.delete(7)
        payments_bill.insert(7, datetime.now(ist).strftime("%a %x %X"))
        paymentid = paymentcontroller.show_next_ai()
        payments_bill.delete(8)
        payments_bill.insert(8, "PaymnetID: " + str(paymentid))
        payments_bill.delete(9)
        payments_bill.insert(9, "ReservationID: " + str(reservationid))
        days = reservationcontroller.get_days(reservationid)
        payments_bill.delete(13)
        payments_bill.insert(13, f"{days}   Complimentary Breakfast         0")
        if item_chosen.get() in ["Parking", "Gym"]:
            current_quantity.set(reservationcontroller.get_days(reservationid))
        room_details_for_all = reservation_roomcontroller.get_room_details(reservationid)
        for i in range(len(room_details_for_all)):
            room_item = f"{room_details_for_all[i][3]}-" + f"{room_details_for_all[i][2]}-" + f"{room_details_for_all[i][4]}-" + f"{room_details_for_all[i][1]}"
            total_room_price = room_details_for_all[i][5] * days
            spaces = 33 - len(room_item) - len(str(total_room_price))
            space = spaces*" "
            payments_bill.insert('end', f"{days}   {room_item}" + space + f"{total_room_price}")        
        self.get_amount_payable()
        payments_bill.insert('end', "----------------------------------------")

    def get_price(*args):
        item_chosen.get()
        item_rates = [500, 600, 500, 600, 6, 7, 50, 1500, 20, 70, 20, 100, 200]
        item_rate = item_rates[item.current()]
        item_price = int(item_rate * current_quantity.get())
        current_price.set(item_price)

    def add_item(self):
        payments_bill.delete('end')
        item = item_chosen.get()
        quantity = current_quantity.get()
        price = current_price.get()
        spaces = 33 - len(item) - len(str(price))
        space = spaces*" "
        payments_bill.insert('end', f"{quantity}   {item}" + space + f"{price}")
        self.get_amount_payable()
        payments_bill.insert('end', "----------------------------------------")

    def delete_item(self):
        if payments_bill.index(payments_bill.curselection()[0]) <= 12:
            print("Can't delete that.")
        else:
            payments_bill.delete(payments_bill.curselection()[0])

    def get_amount_payable(self):
        items = payments_bill.get(13, 'end')
        total = 0
        for one_item in items:
            reversed_price = str()
            for b in range(-1, -(len(one_item)+1), -1):
                if one_item[b].isspace():
                    break
                else:
                    reversed_price += one_item[b]
            price = int(reversed_price[::-1])
            total += price
        amount_payable.set(total)

    def get_bill(self):
        add_button['state'] = 'disabled'
        delete_button['state'] = 'disabled'
        mode['state'] = 'disabled'
        total = amount_payable.get()
        spaces = 40 - 6 - len(str(total))
        space = spaces*" "
        payments_bill.insert('end', "Total:" + space + str(total))
        mode_for_bill = mode_chosen.get()
        spaces2 = 40 - 16 - len(str(mode_for_bill))
        space2 = spaces2*" "
        payments_bill.insert('end', "Mode of Payment:" + space2 + str(mode_for_bill))
        payments_bill.insert('end', "----------------------------------------")
        payments_bill.insert('end', "Thank you for choosing us.")
        payments_bill.insert('end', "Comfort with a touch of luxury.")
        payments_bill.insert('end', " ")

    def create_payment(self):
        reservationid = reservationid_label_var.get()
        paymentdate = datetime.now(ist).strftime("%Y%m%d")
        amount_paid = amount_payable.get()
        mode_of_payment = mode_chosen.get()
        payment = Payment(ReservationID = reservationid, PaymentDate = paymentdate, AmountPaid = amount_paid, ModeOfPayment = mode_of_payment)
        paymentcontroller.add_payment(payment)
        self.refresh_payments()
        self.save_bill()

    def get_paymentid(self):
        for record in payments_table.selection():
            selected_paymentid = payments_table.item(record)['values'][0]
        return selected_paymentid

    def delete_payment(self):
        paymentid = self.get_paymentid()
        paymentcontroller.delete_payment(paymentid)
        self.refresh_payments()

    def refresh_payments(self):
        for payment in payments_table.get_children():
            payments_table.delete(payment)
        self.get_payments()
        for reservation in payment_reservation_table.get_children():
            payment_reservation_table.delete(reservation)
        Reservation_Tab.get_reservations(self, payment_reservation_table)

    def save_bill(self):
        lines = str()
        for line in payments_bill.get(0,'end'):
            lines += line + '\n'
        with open(rf"bills\bill_payment_id_{paymentcontroller.show_next_ai()-1}.txt", 'w') as f:
            f.write(''.join(lines))
            f.write('\n')
        subprocess.Popen(["notepad.exe", rf"bills\bill_payment_id_{paymentcontroller.show_next_ai()-1}.txt"])