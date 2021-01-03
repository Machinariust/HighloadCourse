import random
import time
import sys
from chequeparser import *

num_files = 20

image_files = ['testcheque' + t + '.png' for t in ['', '2', '3', '4', '5']]
random_order_image_files = []

for i in range(num_files):
    random_order_image_files.append(random.choice(image_files))

print("we will parse " + str(num_files) + " cheques")
sys.stdout.flush()
   
a = time.perf_counter()
for randimagefile in random_order_image_files:
    parse_cheque("C:\\Program Files\\Tesseract-OCR\\Tesseract.exe", randimagefile)
b = time.perf_counter()

print(str(num_files) + " cheques, time = " + str(b-a) + " sec")
print("average " + str((b-a)/num_files) + " sec for one")
    

    

