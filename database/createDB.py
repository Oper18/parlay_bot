# config:utf-8

import sqlite3

nameDB = 'testDB'

connect = sqlite3.connect(nameDB)

cursor = connect.cursor()

try:
    cursor.execute('''CREATE TABLE users (id INTEGER PRRIMARY KEY AUOTINCREMENT, name TEXT NOT NULL, balance REAL NOT NULL)''')

except:
    print('Table was created earlier.')

try:
    cursor.execute('''CREATE TABLE parlay (id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT NOT NULL, summ REAL NOT NULL,
                    result TEXT, user INTEGER NOT NULL, FOREIGN KEY user REFERENCES users (id))''')

except:
    print('Table was created earlier.')

try:
    cursor.execute('''CREATE TABLE lott (id INTEGER PRIMARY KEY AUTOINCREMENT, result TEXT, prize REAL NOT NULL,
                    members INTEGER NOT NULL, winners INTEGERS NOT NULL, losers INTEGERS NOT NULL)''')

except:
    print('Table was created earlier.')

cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
cursor.execute('''PRAGMA table_info(users)''')
tableUsers = cursor.fetchall()
cursor.execute('''PRAGMA table_info(parlay)''')
tableParlay = cursor.fetchall()
cursor.execute('''PRAGMA table_info(lott)''')
tableLott = cursor.fetchall()

print('Tables: %s' % tables)
print('Users: %s' % tableUsers)
print('Parlaies: %s' % tableParlay)
print('Lottery: %s' % tableLott)

connect.commit()
connect.close()