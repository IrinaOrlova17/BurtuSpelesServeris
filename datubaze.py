import sqlite3

DB = sqlite3.connect('top.db')
SQL= DB.cursor()

def atslegt():
  DB.close()

def taisitTabulu():
  SQL.execute("""CREATE TABLE IF NOT EXISTS speletaji (
              id INTEGER NOT NULL UNIQUE, 
              vards TEXT,
              laiks INTEGER,
              PRIMARY KEY ("id" AUTOINCREMENT)    
        
           )""")

taisitTabulu()
