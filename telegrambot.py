from PIL import Image
import telebot
import sys
from io import BytesIO

from imageparser import *
from chequeparser import *

import database
import datetime

bot = telebot.TeleBot('<token>')
tesseract_exe = "C:\\Program Files\\Tesseract-OCR\\Tesseract.exe"
db = database.Database('cheque - Copy.db')

#@bot.message_handler(commands=['start'])
#def start_message(message):
#    client_name = message.from_user.id
#    
#    bot.send_message(message.chat.id, 'Hi, you have written /start')
#    bot.send_message(message.chat.id, 'And I can register you as Clients.Name = ' + str(client_name))

#(date in 2006-03-28)
#report formats:
#  /report d_start d_end
#  /report week
#  /report w
#  /report monts
#  /report m
@bot.message_handler(commands=['report'])
def report_message(message):
    client_name = str(message.from_user.id)
    
    lexems = [s.strip() for s in message.text.split(' ')]
    
    #(date in 2006-03-28)
    d_today = datetime.date.today().strftime("%Y-%m-%d") 
    d_week = (datetime.date.today() - datetime.timedelta(days=7)).strftime("%Y-%m-%d") 
    d_month = (datetime.date.today() - datetime.timedelta(days=30)).strftime("%Y-%m-%d") 
    
    d_start = None
    d_end = None
    
    if (len(lexems) >= 2):
        if (lexems[1].lower() == "week") or (lexems[1].lower() == "w"):
            d_start = d_week
            d_end = d_today
        elif (lexems[1].lower() == "month") or (lexems[1].lower() == "m"):
            d_start = d_month
            d_end = d_today
        elif (len(lexems) >= 3):
            d_start = lexems[1]
            d_end = lexems[2]  
        
    try:
        dd_start = datetime.date(int(d_start[:4]), int(d_start[5:7]), int(d_start[8:10]))
        dd_end = datetime.date(int(d_end[:4]), int(d_end[5:7]), int(d_end[8:10]))
        
        if (dd_end < dd_start):
            dd_start, dd_end = dd_end, dd_start
        
        rep = db.report_str(client_name, dd_start, dd_end)
        
        
        if (len(rep.strip()) > 0):
            bot.send_message(message.chat.id, "Report for: " + dd_start.strftime("%Y-%m-%d") + " -- " +
                                                           dd_end.strftime("%Y-%m-%d") + ":\n" + rep)
        else:
            bot.send_message(message.chat.id, "Report for: " + dd_start.strftime("%Y-%m-%d") + " -- " +
                                                           dd_end.strftime("%Y-%m-%d") + ": <Nothing>")
    except:
        bot.send_message(message.chat.id, "report: Illegal format!")
    

@bot.message_handler(content_types=['photo'])
def photo_message(message):
    ph = message.photo[0]
    
    try:
        file_info = bot.get_file(ph.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        img = Image.open(BytesIO(downloaded_file))
    
        products = parse_cheque_as_image(tesseract_exe, img)
            
        bot.send_message(message.chat.id, "Photo has been succesfully parsed!")
            
        if (len(products) > 0):
            db.insert_purchases(str(message.from_user.id), products)

        bot.send_message(message.chat.id, "Data from photo has been succesfully added into database!")
    except:
        bot.send_message(message.chat.id, "Oops! Error :(")
    
bot.polling()
