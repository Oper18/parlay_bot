# coding:utf-8

from database import select_fields

#Choose balance for user from DB
def Balance(name):
    users = select_fields.SelectUsers()
    for i in range(len(users)):
        if users[i][1] == name:
            user = users[i][1:]

    balance = user[1]

    return balance

#Choose history of parlaies for currnent user from DB
def UserParlaies(name):
    users = select_fields.SelectUsers()
    parlaies = select_fields.SelectParlay()
    userParlaies = []
    for i in range(len(users)):
        if users[i][1] == name:
            for j in range(len(parlaies)):
                if parlaies[j][4] == users[i][0]:
                    userParlaies.append(parlaies[j][1:4])

    return userParlaies

#Choose lotteries from DB
def Lotteries(num = 0):
    if num == 0:
        lotteries = select_fields.SelectLotts()
        lotteries = lotteries[:][1:]
    else:
        num = (- num)
        lotteries = select_fields.SelectLotts()
        lotteries = lotteries[num][1:]

    return lotteries