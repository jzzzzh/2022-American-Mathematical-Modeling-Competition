import random
import numpy as np
import random as rand
import matplotlib.pyplot as plt
import math
import csv
commission = 0.0
bitcoin = []
gold = []
bitcoinpred = []
goldpred = []
mypred2 = []
money = [1000, 0, 0]
m = 0
n = 0


def read():
    with open('mypred2.csv') as f:
        f_csv = csv.reader(f)
        list_f_csv = list(f_csv)
        for row in list_f_csv[1:]:
            x = []
            x.append(row[7])
            x.append(row[8])
            x.append(row[9])
            x.append(row[10])
            x.append(row[11])
            x.append(row[12])
            mypred2.append(x)
    with open('mypred.csv') as f:
        f_csv = csv.reader(f)
        list_f_csv = list(f_csv)
        for row in list_f_csv[1:]:
            x = []
            x.append(row[1])
            x.append(row[2])
            bitcoin.append(x)
            y = []
            y.append(row[1])
            y.append(row[3])
            y.append(row[6])
            gold.append(y)
            bitcoinpred.append(row[4])
            goldpred.append(row[5])


def buy_bitcoin(x, n, bitcoinCommission):
    if float(money[0]) >= x:
        true_buy_money = (1-bitcoinCommission) * x
        bitcoin_num = true_buy_money/float(bitcoin[n][1])
        money[0] = money[0] - x
        money[2] = money[2] + bitcoin_num
    else:
        print("error,money buy bitcoin is not enough")


def sell_bitcoin(y, n, bitcoinCommission):
    if float(money[2]) >= y:
        true_sell_money = (1-bitcoinCommission) * y
        money_num = true_sell_money*float(bitcoin[n][1])
        money[0] = money[0] + money_num
        money[2] = money[2] - y
    else:
        print("error,money sell bitcoin is not enough")


def sell_gold(y, m, goldCommission):
    if float(money[1]) >= y:
        true_sell_money = (1-goldCommission) * y
        money_num = true_sell_money * float(gold[n][1])
        money[0] = money[0] + money_num
        money[1] = money[1] - y
    else:
        print("error,money sell gold is not enough")


def buy_gold(x, m, goldCommission):
    if float(money[0]) >= x:
        true_buy_money = (1-goldCommission) * x
        gold_num = true_buy_money/float(gold[n][1])
        money[0] = money[0] - x
        money[1] = money[1] + gold_num
    else:
        print("error,money buy gold is not enough")


def showWholeMoney(m, n):
    # money is the whole money, m is the gold day, n is the bitcoin day,
    print(money)
    whole_money = money[0] + money[1] * \
        float(gold[n][1]) + money[2]*float(bitcoin[n][1])
    print('$  ' + str(whole_money))
    return whole_money


def getGoldlist(i, money, listPast, listFuture, recentMoney):
    list = []
    dollarnum = float(money[0])
    goldnum = float(money[1])
    BTCnum = float(money[2])
    recMon = float(recentMoney)
    preMon = float(listFuture)
    list.append(dollarnum)
    list.append(goldnum)
    list.append(BTCnum)
    list.append(recMon)
    list.append(preMon)
    list.append(float(mypred2[i][1]))
    list.append(float(mypred2[i][2]) - float(mypred2[i][4]))
    list1 = []
    list2 = []
    list3 = []
    list10 = []
    list20 = []
    list30 = []
    list4 = []
    list40 = []
    max = 0.0
    sum = 0.0
    min = 999999.99
    mnum = -1
    nnum = -1
    i = 0
    for a in listPast:
        i += 1
        e = float(a[1])
        sum += e
        if e > max:
            max = e
            mnum = i
        if e < min:
            min = e
            nnum = i
        list1.append(e)
    differtime = mnum - nnum
    list.append(max)
    list.append(min)
    list.append(sum / 40.0)
    for a in list1:
        list10.append(((float(a) / max) - 0.5) * 2)
    max = 0.0
    i = 0
    for a in listPast[1:]:
        i += 1
        b = listPast[i - 1]
        r = float(a[1]) - float(b[1])
        if r > max:
            max = r
        list2.append(r)
    i = 1
    max = 0.0
    for a in listPast[2:]:
        i += 1
        b = listPast[i - 2]
        t = float(a[1]) - float(b[1])
        if t > max:
            max = t
        list3.append(t)
    i = 9
    max = 0.0
    for a in listPast[10:]:
        i += 1
        b = listPast[i - 10]
        t = float(a[1]) - float(b[1])
        if t > max:
            max = t
        list4.append(t)
    list.append(list10)
    list.append(list2)
    list.append(list3)
    list.append(list4)
    list.append(differtime)
    list.append(i)
    return list


def getBTClist(i, money, listPast, listFuture, recentMoney):
    list = []
    dollarnum = float(money[0])
    goldnum = float(money[1])
    BTCnum = float(money[2])
    recMon = float(recentMoney)
    preMon = float(listFuture)
    list.append(dollarnum)
    list.append(goldnum)
    list.append(BTCnum)
    list.append(recMon)
    list.append(preMon)
    list.append(float(mypred2[i][0]))
    list.append(float(mypred2[i][3])-float(mypred2[i][5]))
    list1 = []
    list2 = []
    list3 = []
    list10 = []
    list20 = []
    list30 = []
    list4 = []
    list40 = []
    max = 0.0
    sum = 0.0
    min = 999999.99
    mnum = -1
    nnum = -1
    i = 0
    for a in listPast:
        i += 1
        e = float(a[1])
        sum += e
        if e > max:
            max = e
            mnum = i
        if e < min:
            min = e
            nnum = i
        list1.append(e)
        differtime = mnum - nnum
    list.append(max)
    list.append(min)
    list.append(sum/40.0)
    max = 0.0
    i = 0
    for a in listPast[1:]:
        i += 1
        b = listPast[i-1]
        r = float(a[1])-float(b[1])
        if r > max:
            max = r
        list2.append(r)
    max = 0.0
    i = 1
    for a in listPast[2:]:
        i += 1
        b = listPast[i-2]
        t = float(a[1])-float(b[1])
        if t > max:
            max = t
        list3.append(t)
    i = 9
    max = 0.0
    for a in listPast[10:]:
        i += 1
        b = listPast[i - 10]
        t = float(a[1]) - float(b[1])
        if t > max:
            max = t
        list4.append(t)
    list.append(list10)
    list.append(list2)
    list.append(list3)
    list.append(list4)
    list.append(differtime)
    list.append(i)
    return list


def getBTCback(list, Glist):
    num = 1
    numList = [3, 2, 7, 1, 7, 1, 2, 8, 9, 3, 1, 6]
    nusum = 0
    buywhat = 0.0
    sellwhat = 0.0
    flag = True
    for nu in numList:
        nusum += nu
    if(list[3] < list[9]):
        buywhat = buywhat + numList[0]/nusum
    elif(list[3] > list[9]):
        sellwhat = sellwhat + numList[0]/nusum
    if (list[5] > 0):
        buywhat = buywhat + numList[1] / nusum
    elif(list[5] < 0):
        sellwhat = sellwhat + numList[1] / nusum
    if (list[6] > 3 and list[6] < 6):
        buywhat = buywhat + numList[2] / nusum
    elif(list[6] < -3 and list[6] > -6):
        sellwhat = sellwhat + numList[2] / nusum
    if (list[6] <= -6):
        buywhat = buywhat + numList[3] / nusum
    elif(list[6] >= 6):
        sellwhat = sellwhat + numList[3] / nusum
    if (list[13][29] > 0 and list[14] > 0):
        buywhat = buywhat + numList[4] / nusum
    elif(list[13][29] < 0 and list[14] < 0):
        sellwhat = sellwhat + numList[4] / nusum
    if (Glist[3] > list[9]):
        buywhat = buywhat + numList[5] / nusum
    elif(Glist[3] < list[9]):
        sellwhat = sellwhat + numList[5] / nusum
    if (Glist[5] > 0):
        buywhat = buywhat + numList[6] / nusum
    elif(Glist[5] < 0):
        sellwhat = sellwhat + numList[6] / nusum
    if (Glist[6] < -3 and Glist[6] > -6):
        buywhat = buywhat + numList[7] / nusum
    elif(Glist[6] > 3 and Glist[6] < 6):
        sellwhat = sellwhat + numList[7] / nusum
    if (Glist[6] >= 6):
        buywhat = buywhat + numList[8] / nusum
    elif(Glist[6] <= -6):
        sellwhat = sellwhat + numList[8] / nusum
    if (Glist[13][29] < 0 and list[14] < 0):
        buywhat = buywhat + numList[9] / nusum
    elif(Glist[13][29] > 0 and list[14] > 0):
        sellwhat = sellwhat + numList[9] / nusum
    if (list[5]/list[3] > 0.08):
        buywhat = buywhat + numList[10] / nusum
    elif(list[5]/list[3] < -0.08):
        sellwhat = sellwhat + numList[10] / nusum
    if (Glist[5]/Glist[3] < -0.08):
        buywhat = buywhat + numList[11] / nusum
    elif(Glist[5]/Glist[3] > 0.08):
        sellwhat = sellwhat + numList[11] / nusum
    ratelist = [-0.8, -0.5, 0.8, 0.5, 0.01]
    if(sellwhat > 0.5):
        num = ratelist[0]
        flag = True
    elif(sellwhat > 0.3):
        num = ratelist[1]
    elif buywhat > 0.5:
        num = ratelist[2]
    elif buywhat > 0.3:
        num = ratelist[3]
    else:
        num = ratelist[-1]
    if(flag == True):
        if(list[15] == 40):
            num = 0.7
            flag = False
        else:
            if(num > 0):
                num = 0.6
                flag = False
    return num


def getGoldback(list, Glist):
    num = 0.0
    numList = [6, 5, 7, 1, 1, 2, 4, 8, 4, 4, 2, 8]
    flag = True
    nusum = 0
    buywhat = 0.0
    sellwhat = 0.0
    for nu in numList:
        nusum += nu
    if (list[3] < list[9]):
        buywhat = buywhat + numList[0] / nusum
    elif (list[3] > list[9]):
        sellwhat = sellwhat + numList[0] / nusum
    if (list[5] > 0):
        buywhat = buywhat + numList[1] / nusum
    elif (list[5] < 0):
        sellwhat = sellwhat + numList[1] / nusum
    if (list[6] > 3 and list[6] < 6):
        buywhat = buywhat + numList[2] / nusum
    elif (list[6] < -3 and list[6] > -6):
        sellwhat = sellwhat + numList[2] / nusum
    if (list[6] <= -6):
        buywhat = buywhat + numList[3] / nusum
    elif (list[6] >= 6):
        sellwhat = sellwhat + numList[3] / nusum
    if (list[13][29] > 0 and list[14] > 0):
        buywhat = buywhat + numList[4] / nusum
    elif (list[13][29] < 0 and list[14] < 0):
        sellwhat = sellwhat + numList[4] / nusum
    if (Glist[3] > list[9]):
        buywhat = buywhat + numList[5] / nusum
    elif (Glist[3] < list[9]):
        sellwhat = sellwhat + numList[5] / nusum
    if (Glist[5] > 0):
        buywhat = buywhat + numList[6] / nusum
    elif (Glist[5] < 0):
        sellwhat = sellwhat + numList[6] / nusum
    if (Glist[6] < -3 and Glist[6] > -6):
        buywhat = buywhat + numList[7] / nusum
    elif (Glist[6] > 3 and Glist[6] < 6):
        sellwhat = sellwhat + numList[7] / nusum
    if (Glist[6] >= 6):
        buywhat = buywhat + numList[8] / nusum
    elif (Glist[6] <= -6):
        sellwhat = sellwhat + numList[8] / nusum
    if (Glist[13][29] < 0 and list[14] < 0):
        buywhat = buywhat + numList[9] / nusum
    elif (Glist[13][29] > 0 and list[14] > 0):
        sellwhat = sellwhat + numList[9] / nusum
    if (list[5] / list[3] > 0.08):
        buywhat = buywhat + numList[10] / nusum
    elif (list[5] / list[3] < -0.08):
        sellwhat = sellwhat + numList[10] / nusum
    if (Glist[5] / Glist[3] < -0.08):
        buywhat = buywhat + numList[11] / nusum
    elif (Glist[5] / Glist[3] > 0.08):
        sellwhat = sellwhat + numList[11] / nusum
    ratelist = [-0.9, -0.5, 0.9, 0.5, 0.00]
    if (sellwhat > 0.5):
        num = ratelist[0]
    elif (sellwhat > 0.3):
        num = ratelist[1]
    elif buywhat > 0.5:
        num = ratelist[2]
    elif buywhat > 0.3:
        num = ratelist[3]
    else:
        num = ratelist[-1]
    if (flag == True):
        if (list[15] == 40):
            num = 0.4
            flag = False
        else:
            if (num > 0):
                num = 0.6
                flag = False
    return num


def buyHowManyB(i, money, listPast, listFuture, recentMoney, Glistpast, GlistFuture, GrecentMony, goldCommission):
    manylist = getBTClist(i, money, listPast, listFuture, recentMoney)
    Gmanylist = getGoldlist(i, money, Glistpast, GlistFuture, GrecentMony)
    many = getBTCback(manylist, Gmanylist)
    x = random.randint(1, (25 - int(math.fabs(many))*10)
                       * int(bitcoinCommission * 100))
    if math.fabs(many) < 0.4 and x > 1:
        many = 0
    else:
        many = many
    return many


def buyHowManyG(i, money, Blistpast, BlistFuture, BrecentMoney, listPast, listFuture, recentMoney, goldCommission):
    manylist = getGoldlist(i, money, listPast, listFuture, recentMoney)
    Bmanylist = getBTClist(i, money, Blistpast, BlistFuture, BrecentMoney)
    many = getGoldback(Bmanylist, manylist)
    x = random.randint(1, (25 - int(math.fabs(many))*10)
                       * int(goldCommission * 100))
    if math.fabs(many) < 0.4 and x > 1:
        many = 0
    else:
        many = many
    return many


if __name__ == "__main__":
    max = 0
    read()
    bitcoinCommission = 0.02
    goldCommission = 0.01
    test_time = 1825
    USdollarlist = []
    for i in range(0, test_time):
        print("bitcoin = $" + str(bitcoin[n][1]))
        if(i >= 40):
            BTHlistpast = bitcoin[i-40:i]
            BTHlistpred = bitcoinpred[i+1]
            BTHdallor = bitcoin[n][1]
            GOLDlistpast = gold[i - 40:i]
            GOLDlistpred = goldpred[i + 1]
            GOLDdallor = gold[i][1]
            buyHowManyBTCnum = buyHowManyB(
                i, money, BTHlistpast, BTHlistpred, BTHdallor, GOLDlistpast, GOLDlistpred, GOLDdallor, bitcoinCommission)
            buyHowManyGOLD = 0
            if gold[i][2] == 'TRUE':
                print("gold = $" + str(gold[i][1]))
                buyHowManyGOLDnum = buyHowManyG(
                    i, money, BTHlistpast, BTHlistpred, BTHdallor, GOLDlistpast, GOLDlistpred, GOLDdallor, goldCommission)
        else:
            buyHowManyGOLDnum = 0
            buyHowManyBTCnum = 0
        if buyHowManyGOLDnum == 0 and buyHowManyBTCnum == 0:
            # if buyHowManyGOLDnum >= 0:
            what_to_do = 1
        elif buyHowManyBTCnum == 0 and buyHowManyGOLDnum > 0:
            what_to_do = 2
        elif buyHowManyBTCnum > 0 and buyHowManyGOLDnum == 0:
            what_to_do = 3
        elif buyHowManyBTCnum > 0 and buyHowManyGOLDnum > 0:
            what_to_do = 4
        elif buyHowManyBTCnum == 0 and buyHowManyGOLDnum < 0:
            what_to_do = 5
        elif buyHowManyBTCnum < 0 and buyHowManyGOLDnum == 0:
            what_to_do = 6
        elif buyHowManyBTCnum < 0 and buyHowManyGOLDnum < 0:
            what_to_do = 7
        elif buyHowManyBTCnum < 0 and buyHowManyGOLDnum > 0:
            what_to_do = 8
        elif buyHowManyBTCnum > 0 and buyHowManyGOLDnum < 0:
            what_to_do = 9
        print(what_to_do)
        if what_to_do == 1:
            print("No buy No sell")
        elif what_to_do == 2:
            if gold[i][2] == 'TRUE':
                x = math.fabs(buyHowManyGOLDnum)*money[0]
                buy_gold(x, i, goldCommission)
                commission = commission+0.01*x
                print("buy gold")
            else:
                print("No buy No sell")
        elif what_to_do == 3:
            x = math.fabs(buyHowManyBTCnum)*money[0]
            buy_bitcoin(x, n, bitcoinCommission)
            commission = commission + 0.02 * x
            print("buy bitcoin")
        elif what_to_do == 4:
            x = math.fabs(buyHowManyGOLDnum)*money[0]
            buy_bitcoin(x, n, bitcoinCommission)
            commission = commission + 0.02 * x
            if gold[i][2] == 'TRUE':
                x = math.fabs(buyHowManyBTCnum)*money[0]
                buy_gold(x, i, goldCommission)
                commission = commission + 0.01 * x
                print("buy both")
            else:
                print("buy bitcoin")
        elif what_to_do == 5:
            if gold[i][2] == 'TRUE':
                y = math.fabs(buyHowManyGOLDnum)*money[1]
                commission = commission + 0.01 * y
                sell_gold(y, i, goldCommission)
                print("sell gold")
            else:
                print("No buy No sell")
        elif what_to_do == 6:
            y = math.fabs(buyHowManyBTCnum)*money[2]
            commission = commission + 0.02 * y
            sell_bitcoin(y, n, bitcoinCommission)
            print("sell bitcoin")
        elif what_to_do == 7:
            y = math.fabs(buyHowManyBTCnum)*money[2]
            commission = commission + 0.02 * y
            sell_bitcoin(y, n, bitcoinCommission)
            if gold[i][2] == 'TRUE':
                y = math.fabs(buyHowManyGOLDnum)*money[1]
                commission = commission + 0.01 * y
                sell_gold(y, i, goldCommission)
                print("sell both")
            else:
                print("sell bitcoin")
        elif what_to_do == 8:
            y = math.fabs(buyHowManyBTCnum)*money[2]
            sell_bitcoin(y, n, bitcoinCommission)
            commission = commission + 0.02 * y
            if gold[i][2] == 'TRUE':
                x = math.fabs(buyHowManyGOLDnum)*money[0]
                commission = commission + 0.01 * x
                buy_gold(x, i, goldCommission)
                print("buy gold and sell BTC")
            else:
                print("sell BTC")
        elif what_to_do == 9:
            if gold[i][2] == 'TRUE':
                x = math.fabs(buyHowManyGOLDnum)*money[1]
                commission = commission + 0.01 * x
                sell_gold(x, i, goldCommission)
                print("buy BTC and sell GOLD")
            else:
                print("buy BTC")
            y = math.fabs(buyHowManyBTCnum)*money[0]
            commission = commission + 0.02 * y
            buy_bitcoin(y, n, bitcoinCommission)
        if gold[i][2] == 'TRUE':
            m = m+1
        n = n+1
        print(str(n)+'days')
        USdollar = showWholeMoney(m, n)
        USdollarlist.append(USdollar)
        if max < USdollar:
            max = USdollar
    plt.plot(USdollarlist, color="green")
    plt.show()
    print('commission=' + str(commission))
