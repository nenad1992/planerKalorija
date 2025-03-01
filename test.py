import sqlite3


conn = sqlite3.connect("tablicakalorija.db")
cursor = conn.cursor()

cursor.execute('''
INSERT INTO tablicakalorija (namirnica, proteini, ugljenihidrati, masti)
VALUES ("Jaja", 12.58, 0.77, 9.94)
''')

conn.commit()

cursor.close()
conn.close()