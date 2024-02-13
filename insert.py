import sqlite3

conn = sqlite3.connect('afternoon.db')
print("opened database successfully")

conn.execute("INSERT INTO EMPLOYEES VALUES (1,'FAITH KARIMI',34,34000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (2,'JOHNSON SAKAJA',36,34000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (3,'BENNY AKARAGWA',25,350000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (4,'BEATRICE NANDWA',43,454000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (5,'DANIEL LOWUASA',56,200000.00)")

conn.commit()
print("employees inserted successfully")
conn.close()