from PIL import Image
import sys
import time
from io import BytesIO

from imageparser import *
from chequeparser import *

import database
import datetime

db = database.Database('cheque - Copy.db')

a = time.perf_counter()
products = parse_cheque("C:\\Program Files\\Tesseract-OCR\\Tesseract.exe", 'testcheque.png')
b = time.perf_counter()
print("Parsing, time = " + str(b-a) + " sec")

a = time.perf_counter()
db.insert_purchases("Petr", products)
b = time.perf_counter()
print("Adding, time = " + str(b-a) + " sec")

a = time.perf_counter()
print(db.report_str('Petr', datetime.date(2020, 11, 30), datetime.date(2020, 12, 14)))
b = time.perf_counter()
print("Reporting, time = " + str(b-a) + " sec")

