import sqlite3

conn = sqlite3.connect('afternoon.db')
print("Opened database successfully")

conn.execute("INSERT INTO EMPLOYEES VALUES(1,'Faith karimi',34, 340000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES(2,'MAry kavinya',30,580000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES(3,'Esther mueni',33,960000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES(4,'Angela ngunde',35,520000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES(5,'Ndanu charles',37,890000.00)")

conn.commit()
print("EMPLOYEES INSERTED SUCCESSFULLY")
conn.close()
