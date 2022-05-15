import sqlite3

JSON = 'rezultati.json'

DB = sqlite3.connect('top.db')
SQL = DB.cursor()

with open(JSON, 'r', encoding="UTF-8") as f:
  dati = f.read()
  datiJson = json.load(dati)

for dati n datiJson:
  SQL.execute("INSERT INTO rezultati (vards, laiks) VALUES (:vards, :laiks )", {'vards': dati['vards'], 'vecums': dati['laiks']})

DB.commit()
SQL.execute("SELECT * FROM rezultati" )
print(SQL.fetchall())
