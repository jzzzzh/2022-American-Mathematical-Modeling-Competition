# ---
# author: jzh
# date: 2022.02.19
# ---
import random

import numpy as np
import csv
import random as rand
import matplotlib.pyplot as plt
import math
commission = 0.0
bitcoin = []
gold = []
bitcoinpred = []
goldpred = []
mypred2 = []
# money[usd, gold, bitcoin]
money = [1000, 0, 0]

m = 0
n = 0
def read():
    with open('mypred2.csv') as f:
        f_csv = csv.reader(f)
        list_f_csv = list(f_csv)
        for row in list_f_csv[1:]:
            x = []
            #bitcoin differential value	  gold differential value	  gold growth
            # bitcoin growth	 gold descend	bitcoin descend
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
        # print(list_f_csv)
        # date = list_f_csv[1][1]
        # print(date)
        # print(list_f_csv[1][4])
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
    # with open('pred.csv') as f:
    #     f_csv = csv.reader(f)
    #     list_f_csv = list(f_csv)
    #     # print(list_f_csv)
    #     date = list_f_csv[1][3]
    #     print(date)
    #     print(list_f_csv[1][4])
    #     for row in list_f_csv[1:]:
    #         bitcoinpred.append(row[3])
    #         goldpred.append(row[4])
    #     # print(bitcoinpred)
    #     # print(goldpred)
    # with open('BCHAIN-MKPRU.csv') as f:
    #     f_csv = csv.reader(f)
    #     list_f_csv = list(f_csv)
    #     date = list_f_csv[1][0]
    #     for row in list_f_csv[2:]:
    #         bitcoin.append(row)
    # with open('gold_refill.csv') as f:
    #     f_csv = csv.reader(f)
    #     list_f_csv = list(f_csv)
    #     date = list_f_csv[1][0]
    #     for row in list_f_csv[2:]:
    #         gold.append(row)
    # # print(bitcoin)
    # # print(gold)
def buy_bitcoin(x,n):
    #money is the whole money, x is the money buy bitcoin, n is the day
    if float(money[0]) >= x:
        true_buy_money = 0.98 * x
        bitcoin_num = true_buy_money/float(bitcoin[n][1])
        money[0] = money[0] - x
        money[2] = money[2] + bitcoin_num
    else:
        print("error,money buy bitcoin is not enough")
def sell_bitcoin(y,n):
    #money is the whole money, y is the money sell bitcoin, n is the day
    if float(money[2]) >= y:
        true_sell_money = 0.98 * y
        money_num = true_sell_money*float(bitcoin[n][1])
        money[0] = money[0] + money_num
        money[2] = money[2] - y
    else:
        print("error,money sell bitcoin is not enough")
def sell_gold(y, m):
    # money is the whole money, y is the money sell gold, m is the day
    if float(money[1]) >= y:
        true_sell_money = 0.99 * y
        money_num = true_sell_money * float(gold[n][1])
        money[0] = money[0]+ money_num
        money[1] = money[1] - y
    else:
        print("error,money sell gold is not enough")
def buy_gold(x,m):
    #money is the whole money, x is the money buy gold, m is the day
    if float(money[0]) >= x:
        true_buy_money = 0.99 * x
        gold_num = true_buy_money/float(gold[n][1])
        money[0] = money[0] - x
        money[1] = money[1] + gold_num
    else:
        print("error,money buy gold is not enough")
def showWholeMoney(m,n):
    #money is the whole money, m is the gold day, n is the bitcoin day,
    print(money)
    whole_money = money[0] + money[1]*float(gold[n][1]) + money[2]*float(bitcoin[n][1])
    # whole_money = money[0] + money[2]*float(bitcoin[n+1][1])
    # whole_money = money[0] + money[1]*float(gold[m+1][1])
    # print(float(gold[m+1][1]))
    # print(m)
    # print(gold[m+1])
    print('$  ' + str(whole_money))
    return whole_money
def getGoldlist(i,money,listPast,listFuture,recentMoney):
    # 0手上美元，1手上黄金，2手上比特币，3现今价格，4预测价格，5预测与现价之差，6涨跌天数（正为涨，负为跌）
    # 7最大值，8最小值，9平均值，10[40天值]，11[40天间隔一天的值（39个）]，12[40天间隔两天差值（38个）]
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
    max = 0.0
    sum = 0.0
    min = 999999.99
    for a in listPast:
        e = float(a[1])
        sum += e
        if e > max:
            max = e
        if e < min:
            min = e
        list1.append(e)
    list.append(max)
    list.append(min)
    list.append(sum / 40.0)
    for a in list1:
        list10.append(((float(a) / max) - 0.5) * 2)
    max = 0.0
    min = 999999
    i = 0
    for a in listPast[1:]:
        i += 1
        b = listPast[i - 1]
        r = float(a[1]) - float(b[1])
        if r > max:
            max = r
        elif r < min:
            min = r
        list2.append(r)
    #for a in list2:
        #list20.append(((float(a) - min) / (max - min) - 0.5) * 2)
    i = 1
    max = 0.0
    min = 999999
    for a in listPast[2:]:
        i += 1
        b = listPast[i - 2]
        t = float(a[1]) - float(b[1])
        if t > max:
            max = t
        elif t < min:
            min = t
        list3.append(t)
    #for a in list3:
        #list30.append(((float(a) - min) / (max - min) - 0.5) * 2)
    list.append(list10)
    list.append(list2)
    list.append(list3)
    return list
def getBTClist(i,money,listPast,listFuture,recentMoney):
    # 0手上美元，1手上黄金，2手上比特币，3现今价格，4预测价格，5预测与现价之差，6涨跌天数（正为涨，负为跌）
    # 7最大值，8最小值，9平均值，10[40天值]，11[40天间隔一天的值（39个）]，12[40天间隔两天差值（38个）]
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


    list1=[]
    list2=[]
    list3=[]
    list10 = []
    list20 = []
    list30 = []
    max = 0.0
    sum = 0.0
    min = 999999.99
    for a in listPast:
        e=float(a[1])
        sum+=e
        if e > max:
            max = e
        if e < min:
            min = e
        list1.append(e)
    list.append(max)
    list.append(min)
    list.append(sum/40.0)
    for a in list1:
        list10.append(((float(a)/max)-0.5)*2)
    max = 0.0
    min = 99999
    i = 0
    for a in listPast[1:]:
        i+=1
        b = listPast[i-1]
        r=float(a[1])-float(b[1])
        if r > max:
            max = r
        elif r < min:
            min = r
        list2.append(r)
    #for a in list2:
        #list20.append(((float(a) - min) / (max - min) - 0.5) * 2)
    max = 0.0
    i = 1
    for a in listPast[2:]:
        i+=1
        b = listPast[i-2]
        t=float(a[1])-float(b[1])
        if t > max:
            max = t
        elif t < min:
            min = t
        list3.append(t)
    #for a in list3:
        #list30.append(((float(a) - min) / (max - min) - 0.5) * 2)
    list.append(list10)
    list.append(list2)
    list.append(list3)
    return list



def getBTCback(list):
    num = 0.0
    desdays = 0
    for item in list[12]:
        if item > 0:
            desdays = desdays + 1
    if list[6] <= -2:
        num = desdays/len(list[12])*1
    elif list[6] >= 2:
        num =(len(list[12]) - desdays)/len(list[12]) * -1 
    return num
def getGoldback(list):
    num = 0.0
    desdays = 0
    for item in list[12]:
        if item > 0:
            desdays = desdays + 1
    if list[6] <= -2:
        num = desdays/len(list[12])*1
    elif list[6] >= 2:
        num =(len(list[12]) - desdays)/len(list[12]) * -1 
    return num





def buyHowManyB(i,money,listPast,listFuture,recentMoney):
    # print("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
    # print(money)
    # print(listPast)
    # print(listFuture)
    # print(recentMoney)
    # print(type(money))
    # print(type(listPast))
    # print(type(listFuture))
    # print(type(recentMoney))
    # print("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")

    x = random.randint(1,15)
    manylist = getBTClist(i, money, listPast, listFuture, recentMoney)
    many = getBTCback(manylist)
    if math.fabs(many) < 0.6 and x > 1:
    #if x > 1:
        many = 0
    else:
        many = many
#many -1 ~ 1
    return many


def buyHowManyG(i,money,listPast,listFuture,recentMoney):
    # print("ggggggggggggggggggggggggggggggggggggg")
    # print(money)
    # print(listPast)
    # print(listFuture)
    # print(recentMoney)
    # print("gggggggggggggggggggggggggggggggggggggg")
    x = random.randint(1, 15)
    manylist = getGoldlist(i,money,listPast,listFuture,recentMoney)
    many = getGoldback(manylist)
    if math.fabs(many)< 0.7 and x > 1:
        many = 0
    else:
        many = many
    return many



if __name__ == "__main__":
    max = 0
    # bitcoin = []
    # gold = []
    read()
    # # money[usd, gold, bitcoin]
    # money = [1000,0,0]
    #
    # m = 0
    # n = 0
    test_time = 1825
    USdollarlist = []
    for i in range(0,test_time):
        # what_to_do = rand.randint(1, 9)
        # what_to_do = 3
        print("bitcoin = $" + str(bitcoin[n][1]))
        if(i > 40):
            BTHlistpast = bitcoin[i-40:i]
            BTHlistpred = bitcoinpred[i+1]
            BTHdallor = bitcoin[n][1]
            buyHowManyBTCnum = buyHowManyB(i,money,BTHlistpast,BTHlistpred,BTHdallor)
            buyHowManyGOLD = 0
            if gold[i][2] == 'TRUE':
                print("gold = $" + str(gold[i][1]))
                GOLDlistpast = gold[i-40:i]
                GOLDlistpred = goldpred[i+1]
                GOLDdallor = gold[i][1]
                buyHowManyGOLDnum = buyHowManyG(i,money, GOLDlistpast, GOLDlistpred, GOLDdallor)
            # else:
            #     print("sorry")
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

        # what_to_do = 3
        print(what_to_do)
        if what_to_do == 1: #不动
            print("No buy No sell")
        elif what_to_do == 2: #buy gold
            if gold[i][2] == 'TRUE':
                x = math.fabs(buyHowManyGOLDnum)*money[0]
                buy_gold(x, i)
                commission=commission+0.01*x
                print("buy gold")
            else:
                print("No buy No sell")
        elif what_to_do == 3:#buy bitcoin
            x = math.fabs(buyHowManyBTCnum)*money[0]
            # x = 0.5
            buy_bitcoin(x, n)
            commission = commission + 0.02 * x
            print("buy bitcoin")
        elif what_to_do == 4:# buy both
            x = math.fabs(buyHowManyGOLDnum)*money[0]
            buy_bitcoin(x, n)
            commission = commission + 0.02 * x
            if gold[i][2] == 'TRUE':
                x = math.fabs(buyHowManyBTCnum)*money[0]
                buy_gold(x, i)
                commission = commission + 0.01 * x
                print("buy both")
            else:
                print("buy bitcoin")
        elif what_to_do == 5:#sell gold
            if gold[i][2] == 'TRUE':
                y = math.fabs(buyHowManyGOLDnum)*money[1]
                commission = commission + 0.01 * y
                sell_gold(y, i)
                print("sell gold")
            else:
                print("No buy No sell")
        elif what_to_do == 6:#sell bitcoin
            y = math.fabs(buyHowManyBTCnum)*money[2]
            commission = commission + 0.02 * y
            sell_bitcoin(y, n)
            print("sell bitcoin")
        elif what_to_do == 7:#sell both
            y = math.fabs(buyHowManyBTCnum)*money[2]
            commission = commission + 0.02 * y
            sell_bitcoin(y, n)
            if gold[i][2] == 'TRUE':
                y = math.fabs(buyHowManyGOLDnum)*money[1]
                commission = commission + 0.01 * y
                sell_gold(y, i)
                print("sell both")
            else:
                print("sell bitcoin")
        elif what_to_do == 8:#buy GOLD and sell BTC
            y = math.fabs(buyHowManyBTCnum)*money[2]
            sell_bitcoin(y,n)
            commission = commission + 0.02 * y
            if gold[i][2] == 'TRUE':
                x = math.fabs(buyHowManyGOLDnum)*money[0]
                commission = commission + 0.01 * x
                buy_gold(x, i)
                print("buy gold and sell BTC")
            else:
                print("sell BTC")
        elif what_to_do == 9:#buy BTC and sell GOLD
            if gold[i][2] == 'TRUE':
                x = math.fabs(buyHowManyGOLDnum)*money[1]
                commission = commission + 0.01 * x
                sell_gold(x, i)
                print("buy BTC and sell GOLD")
            else:
                print("buy BTC")
            y = math.fabs(buyHowManyBTCnum)*money[0]
            commission = commission + 0.02 * y
            buy_bitcoin(y, n)
        if gold[i][2] == 'TRUE':
        # if i % 7 == 1 or i % 7 == 2 or i % 7 == 3 or i%7 == 4 or i % 7 == 0:
            m = m+1
        n = n+1
        print(str(n)+'days')
        # print(i)
        USdollar = showWholeMoney(m,n)
        USdollarlist.append(USdollar)
        if max < USdollar:
            max = USdollar
    plt.plot(USdollarlist,color="green")

    plt.show()
    print("max= " + str(max))
    print('commission=' + str(commission))
    # print(len(gold))
    # print(n)