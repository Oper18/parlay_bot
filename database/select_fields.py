# config:utf-8

import sqlite3

nameDB = 'testDB'

#Choose users list from DB
def SelectUsers():
    connect = sqlite3.connect(nameDB)
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    connect.close()
    # if len(users) != 0:
    #     for i in range(len(users)):
    #         users[i] = users[i][1:]
    return users

#Choose parlaies list from DB
def SelectParlay():
    connect = sqlite3.connect(nameDB)
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM parlay")
    parlaies = cursor.fetchall()
    connect.close()
    if len(parlaies) != 0:
        for i in range(len(parlaies)):
            parlaies[i] = parlaies[i][1:]
    return parlaies

#Choose lotteries list from DB
def SelectLotts():
    connect = sqlite3.connect(nameDB)
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM lott")
    lotts = cursor.fetchall()
    connect.close()
    # if len(lotts) != 0:
    #     for i in range(len(lotts)):
    #         lotts[i] = lotts[i][1:]
    return lotts