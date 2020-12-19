import database
import datetime

from imageparser import *
from chequeparser import *

db = database.Database('cheque - Copy.db')

db.add_client('Ivan')
db.add_client('Piotr')
db.add_client('Ingvar')

print('------------------------')
print(db.get_client_id('Ivan'))
print(db.get_client_id('Piotr'))
print(db.get_client_id('Ingvar'))
print(db.get_client_id('Maxim'))
print('------------------------')
print(db.get_client_id_if_no_insert('Ivan'))
print(db.get_client_id_if_no_insert('Piotr'))
print(db.get_client_id_if_no_insert('Ingvar'))
print(db.get_client_id_if_no_insert('Maxim'))
print(db.get_client_id_if_no_insert('Alexey'))
print('------------------------')
print(db.get_client_id('Ivan'))
print(db.get_client_id('Piotr'))
print(db.get_client_id('Ingvar'))
print(db.get_client_id('Maxim'))
print(db.get_client_id('Alexey'))

print('get_client_id has been tested!')

#2020-03-28
db.insert_purchases('Ivan', [['TestProduct', 100.4, '2020-11-29', 1], ['UnTestProduct', 5.48, '2020-12-01', 2]])
db.insert_purchases('Georgiy', [['SuperAuto', 99.9, '2020-11-14', 3], ['NiceNiceNiceUltraVeryNiceAuto', 9999.99, '2020-12-10', 1.5]])

print('insert_purchases has been tested!')

print(">>> db.report_str('Ivan', datetime.date(2020, 11, 28), datetime.date(2020, 12, 14)):")
print(db.report_str('Ivan', datetime.date(2020, 11, 28), datetime.date(2020, 12, 14)))

print(">>> db.report_str('Ivan', datetime.date(2020, 11, 30), datetime.date(2020, 12, 14)):")
print(db.report_str('Ivan', datetime.date(2020, 11, 30), datetime.date(2020, 12, 14)))

print(">>> db.report_str('Ivan', datetime.date(2020, 10, 20), datetime.date(2020, 10, 30)):")
print(db.report_str('Ivan', datetime.date(2020, 10, 20), datetime.date(2020, 10, 30)))

print(">>> db.report_str('Georgiy', datetime.date(2020, 11, 30), datetime.date(2020, 12, 10)):")
print(db.report_str('Georgiy', datetime.date(2020, 11, 30), datetime.date(2020, 12, 10)))

print(">>> parse_image test:")
print(parse_image("C:\\Program Files\\Tesseract-OCR\\Tesseract.exe", "testcheque.png"))

print(">>> parse_cheque test:")
print(parse_cheque("C:\\Program Files\\Tesseract-OCR\\Tesseract.exe", "testcheque.png"))

