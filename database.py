import sqlite3
import datetime

class Database:
    
    def __init__(self, filename):
        self.connection = sqlite3.connect(filename, check_same_thread=False)
        self.cursor = self.connection.cursor()
        
    def add_client(self, client_name):
        to_insert = [(client_name,)]
        self.cursor.executemany("INSERT INTO Clients(Name) VALUES (?)", to_insert)
        self.connection.commit()
        
    def get_client_id(self, client_name):
        rows = list(self.cursor.execute('SELECT * FROM Clients WHERE Name=?', (client_name,)))
        if (len(rows) == 0):
            return 0
        else:
            return rows[0][0]
    
    def get_client_id_if_no_insert(self, client_name):
        id = self.get_client_id(client_name)
        if (id == 0):
            self.add_client(client_name)
            id = self.get_client_id(client_name)
        return id
    
    def insert_purchases(self, client_name, purchares):
        client_id = self.get_client_id_if_no_insert(client_name)
        
        #purchares -> [Product, Price, Date, Quantity] (date in 2006-03-28)
        to_insert = [tuple([client_id] + row) for row in purchares]
        
        self.cursor.executemany("INSERT INTO Purchases(ClientId, Product, Price, Date, Quantity) VALUES (?,?,?,?,?)", to_insert)
        
        #for ins in to_insert:
        #   self.cursor.executemany("INSERT INTO Purchases(ClientId, Product, Price, Date, Quantity) VALUES (?)", (ins,))
        
        self.connection.commit()
        
    def report(self, client_name, date_start, date_end):
        client_id = self.get_client_id_if_no_insert(client_name)
        
        #if (date_end > date_start):
        #    date_start, date_end = date_end, date_start
        
        query = self.cursor.execute("SELECT Product, Price, Date, Quantity FROM Purchases WHERE ClientId=?", (client_id,))
        rows = list(query)
        results = []
        
        for row in rows:
            #date in 2006-03-28 -> yyyy-mm-dd
            date_str = row[2]
            date = datetime.date(int(date_str[:4]), int(date_str[5:7]), int(date_str[8:10]))
            
            if ((date_start <= date) and (date <= date_end)):
                results.append(row)
            
        return results
        
    def report_str(self, client_name, date_start, date_end):
        rep = self.report(client_name, date_start, date_end)
        
        s = ''
        for r in rep:
            s = s + '\n' + str(r)
            
        return s
            
