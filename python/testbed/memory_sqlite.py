
import sqlite3

conn = sqlite3.connect(':memory:')
print "Opened database successfully"

conn.execute('''CREATE TABLE COMPANY
        (ID INT PRIMARY KEY NOT NULL,
        NAME   TEXT   NOT NULL,
        AGE    INT    NOT NULL,
        ADDRESS CHAR(5),
        SLARY   REAL);''')

print "Table created sunccessfully"
conn.close()
