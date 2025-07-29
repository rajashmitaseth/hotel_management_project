from dbconnection import dbcnx
from models.paymentmodel import Payment

def add_payment(payment:Payment):
    cursor = dbcnx.getcursor()
    cursor.execute(f"insert into payments(ReservationID, PaymentDate, AmountPaid, ModeOfPayment) values ({payment.ReservationID}, {payment.PaymentDate}, {payment.AmountPaid}, '{payment.ModeOfPayment}')")
    dbcnx.save()

def show_payments():
    cursor = dbcnx.getcursor()
    cursor.execute('select * from payments order by PaymentID desc')
    all_payments_raw = cursor.fetchall()
    all_payments = []
    for payment in all_payments_raw:
        all_payments.append(payment)
    return all_payments

def show_next_ai():
    cursor = dbcnx.getcursor()
    cursor.execute("select auto_increment from information_schema.tables where table_schema = 'hoteldb' and table_name = 'payments'")
    next_ai = cursor.fetchone()[0]
    return next_ai

def delete_payment(paymentid):
    cursor = dbcnx.getcursor()
    cursor.execute(f'delete from payments where PaymentID = {paymentid}')
    dbcnx.save()

def search_payment(criteria):
    cursor = dbcnx.getcursor()
    cursor.execute(f'select * from payments where {criteria} order by ReservationID desc')
    return cursor.fetchall()