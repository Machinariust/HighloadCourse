from PIL import Image
from imageparser import *

def parse_cheque(tcmd, file):
    return parse_cheque_as_image(tcmd, Image.open(file))

def parse_cheque_as_image(tcmd, img):
    text = parse_image_as_image(tcmd, img)
    
    lines = [s.strip() for s in text.split('\n')]
    
    products = []
    is_product_line = False
    date = '2000-01-01'
    
    for line in lines:
        if (line.startswith("Total:")):
            is_product_line = False
    
        if (is_product_line) and (len(line) > 0):
            
            pr_descr = [s.strip() for s in line.split(',')]
            
            #print(line)
            
            if len(pr_descr) >= 4:
                #pr_id = pr_descr[0]
                pr_name = pr_descr[1]
                pr_quantity = pr_descr[2]
                pr_cost = pr_descr[3]
                products.append([pr_name, float(pr_quantity), float(pr_cost)])
            
        
        if (line.startswith("Cashier: ")):
            is_product_line = True
            
        if (line.startswith("Datetime: ")):
            #Datetime: 10:07:34 12/19/2020
            #must be as 2020-12-19
            d_m = line[19:21]
            d_d = line[22:24]
            d_y = line[25:29]
            date = d_y + "-" + d_m + "-" + d_d
            
    return [[x[0], x[2], date, x[1]] for x in products]
            
            
            
            
    
            
    
    
    
    