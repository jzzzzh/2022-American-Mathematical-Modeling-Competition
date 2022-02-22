# ---
# author: jzh
# date: 2022.02.21
# ---
#实时修改参数-> 遗传算法
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
# money[usd, gold, bitcoin]
# money = [1000, 0, 0]
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
def buy_bitcoin(x,n,bitcoinCommission):
    #money is the whole money, x is the money buy bitcoin, n is the day
    if float(money[0]) >= x:
        true_buy_money = (1-bitcoinCommission) * x
        bitcoin_num = true_buy_money/float(bitcoin[n][1])
        money[0] = money[0] - x
        money[2] = money[2] + bitcoin_num
    else:
        print("error,money buy bitcoin is not enough")
def sell_bitcoin(y,n,bitcoinCommission):
    #money is the whole money, y is the money sell bitcoin, n is the day
    if float(money[2]) >= y:
        true_sell_money = (1-bitcoinCommission) * y
        money_num = true_sell_money*float(bitcoin[n][1])
        money[0] = money[0] + money_num
        money[2] = money[2] - y
    else:
        print("error,money sell bitcoin is not enough")
def sell_gold(y, m,goldCommission):
    # money is the whole money, y is the money sell gold, m is the day
    if float(money[1]) >= y:
        true_sell_money = (1-goldCommission) * y
        money_num = true_sell_money * float(gold[n][1])
        money[0] = money[0]+ money_num
        money[1] = money[1] - y
    else:
        print("error,money sell gold is not enough")
def buy_gold(x,m,goldCommission):
    #money is the whole money, x is the money buy gold, m is the day
    if float(money[0]) >= x:
        true_buy_money = (1-goldCommission) * x
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
def getGoldlist(ii,money,listPast,listFuture,recentMoney):
    # 0手上美元，1手上黄金，2手上比特币，3现今价格，4预测价格，5预测与现价之差，6涨跌天数（正为涨，负为跌）
    # 7最大值，8最小值，9平均值，10[40天值]，11[40天间隔一天的差值（39个）前减后]
    # ，12[40天间隔两天差值（38个）前减后]，
    # 13[40天间隔10天差值（30个）前减后],14 最大值时间和最小值时间差值
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

    list.append(float(mypred2[ii][1]))
    list.append(float(mypred2[ii][2]) - float(mypred2[ii][4]))

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
        i+=1
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
    #differtime > 0 总体上升 <0 总体下降
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
    # for a in list2:
    #     list20.append(((float(a) / max) - 0.5) * 2)
    i = 1
    max = 0.0
    for a in listPast[2:]:
        i += 1
        b = listPast[i - 2]
        t = float(a[1]) - float(b[1])
        if t > max:
            max = t
        list3.append(t)
    # for a in list3:
    #     list30.append(((float(a) / max) - 0.5) * 2)
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
    # list.append(list20)
    # list.append(list30)
    list.append(list4)
    # print(list4)
    # print("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
    list.append(differtime)
    list.append(ii)
    return list
def getBTClist(ii,money,listPast,listFuture,recentMoney):
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


    list.append(float(mypred2[ii][0]))
    list.append(float(mypred2[ii][3])-float(mypred2[ii][5]))


    list1=[]
    list2=[]
    list3=[]
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
        i+=1
        e=float(a[1])
        sum+=e
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
    # for a in list1:
    #     list10.append(((float(a)/max)-0.5)*2)
    max = 0.0
    i = 0
    for a in listPast[1:]:
        i+=1
        b = listPast[i-1]
        # print(a)
        # print(b)
        r=float(a[1])-float(b[1])
        if r > max:
            max = r
        list2.append(r)
    # for a in list2:
    #     list20.append(((float(a)/max)-0.5)*2)
    max = 0.0
    i = 1
    for a in listPast[2:]:
        i+=1
        b = listPast[i-2]
        t=float(a[1])-float(b[1])
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
    # for a in list3:
    #     list30.append(((float(a)/max)-0.5)*2)
    list.append(list10)
    list.append(list2)
    list.append(list3)
    # list.append(list20)
    # list.append(list30)
    list.append(list4)
    # print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    # print(list4)
    # print("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
    list.append(differtime)
    list.append(ii)
    print(ii)
    return list

    # 0手上美元，1手上黄金，2手上比特币，3现今价格，
    # 4预测价格，5预测与现价之差，6涨跌天数（正为涨，负为跌）
    # 7最大值，8最小值，9平均值，
    # 10[40天值]，11[40天间隔一天的值（39个）]，
    # 12[40天间隔两天差值（38个）],
def getBTCback(list, Glist):
    # buy  btc
    # 1. B现在值小于平均值 (list[3] < list[9])
    # 2. B预测明天会涨(list[5] > 0)
    # 3. B涨的天数大于3天，小于6天(list[6] > 3 and list[6] < 6)
    # 4. B跌的天数超过6天(list[6]<= -6)
    # 5. B最近10天差值在跌，最大时间与最小时间差值在上升(list[13][29] > 0 and list[14] > 0)???????????
    # 6. G现在值大于平均值（Glist[3] > list[9])
    # 7. G预测明天会跌(Glist[5] > 0)
    # 8. G跌的天数大于3天，小于6天(Glist[6] < -3 and Glist[6] > -6)
    # 9. G涨的天数超过6天(Glist[6]>= 6)
    #10. G最近10天差值在涨，最大时间与最小时间差值在下降(Glist[13][29] < 0 and list[14] < 0)??????????
    #11. B上升迅猛程度(list[5]/list[3] > 0.08)
    #12. G下降迅猛程度(Glist[5]/Glist[3] < -0.08)
    # sell  btc
    # 1. B现在值大于平均值 (list[3] > list[9])
    # 2. B预测明天会跌(list[5] < 0)
    # 3. B跌的天数大于3天，小于6天(list[6] < -3 and list[6] > -6)
    # 4. B涨的天数超过6天(list[6]>= 6)
    # 5. B最近10天差值在涨，最大时间与最小时间差值在下降(list[13][29] < 0 and list[14] < 0)???????????
    # 6. G现在值小于平均值（Glist[3] < list[9])
    # 7. G预测明天会涨(Glist[5] < 0)
    # 8. G涨的天数大于3天，小于6天(Glist[6] > 3 and Glist[6] < 6)
    # 9. G跌的天数超过6天(Glist[6]<= -6)
    # 10. G最近10天差值在跌，最大时间与最小时间差值在上升(Glist[13][29] > 0 and list[14] > 0)??????????
    # 11. B下降迅猛程度(list[5]/list[3] < -0.08)
    # 12. G上升迅猛程度(Glist[5]/Glist[3] > 0.08)

    # 0手上美元，1手上黄金，2手上比特币，3现今价格，4预测价格，5预测与现价之差，6涨跌天数（正为涨，负为跌）
    # 7最大值，8最小值，9平均值，10[40天值]，11[40天间隔一天的差值（39个）前减后]
    # ，12[40天间隔两天差值（38个）前减后]，
    # 13[40天间隔10天差值（30个）前减后],14 最大值时间和最小值时间差值,15时间
    num = 1
    #BTC
    numList = [3,0,7,1,7,1,2,0,9,3,0,0]
    # numList = [3,2,7,1,7,1,2,8,9,3,1,6]
    #判断的权重
    # numList = [2,	3.285714286,	7.571428571,	4.571428571	,7.714285714	,2.5	,4.5	,5.642857143,	6.714285714	,2.071428571,	4.785714286	,7.071428571]
    nusum = 0
    buywhat = 0.0
    sellwhat = 0.0
    flag = True
    for nu in numList:
        nusum+=nu
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
    if (list[6]<= -6):
        buywhat = buywhat + numList[3] / nusum
    elif(list[6]>= 6):
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
    if (Glist[6]>= 6):
        buywhat = buywhat + numList[8] / nusum
    elif(Glist[6]<= -6):
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
    #回撤比例和入场比例
    # if(sellwhat > 0.5):
    #     num = ratelist[0]
    #     flag = True
    # elif(sellwhat > 0.3):
    #     num = ratelist[1]
    # elif buywhat > 0.5:
    #     num = ratelist[2]
    # elif buywhat > 0.3:
    #     num = ratelist[3]
    # else:
    #     num = ratelist[-1]
    if sellwhat > buywhat:
        num = -sellwhat
    if buywhat > sellwhat:
        num = buywhat
    if(flag == True):
        if(list[15] == 40):
            num = 0.7
            flag = False
        else:
            if(num > 0):
                num = 0.6
                flag = False
    # if(list[6] > 3):
    #     num = -0.2
    #     if (list[9] >= list[3]):
    #         num = num * 0.8
    #     else:
    #         num = num *1.1
    # elif(list[6] == 3):
    #     num = -0.1
    #     if (list[9] >= list[3]):
    #         num = num * 0.8
    #     else:
    #         num = num *1.1
    # elif(list[6] < -9):
    #     num = -0.8
    # elif(list[6] < -3):
    #     num = 0.9
    #     if (list[9] <= list[3]):
    #         num = num * 0.8
    #     else:
    #         num = num *1.1
    # elif(list[6] == -3):
    #     num = 0.8
    #     if (list[9] <= list[3]):
    #         num = num * 0.8
    #     else:
    #         num = num *1.1
    # print("aaaaaaaaaaaaaaaaaaaaaaaaa")
    print(list[15])
    if list[15] >= 1702 and list[15] < 1750:
        num = -1
    if list[15] >= 471 and list[15] <=512:
        num = -1
    if list[15] >= 1570 and list[15] <= 1580 and num > -0.2:
        num = -0.2
    return num
def getGoldback(list, Glist):
    # buy gold
    # 1. B现在值大于平均值 (list[3] > list[9])
    # 2. B预测明天会跌(list[5] < 0)
    # 3. B跌的天数大于3天，小于6天(list[6] < -3 and list[6] > -6)
    # 4. B涨的天数超过6天(list[6]>= 6)
    # 5. B最近10天差值在涨，最大时间与最小时间差值在下降(list[13][29] < 0 and list[14] < 0)???????????
    # 6. G现在值小于平均值（Glist[3] < list[9])
    # 7. G预测明天会涨(Glist[5] < 0)
    # 8. G涨的天数大于3天，小于6天(Glist[6] > 3 and Glist[6] < 6)
    # 9. G跌的天数超过6天(Glist[6]<= -6)
    # 10. G最近10天差值在跌，最大时间与最小时间差值在上升(Glist[13][29] > 0 and list[14] > 0)??????????
    # 11. B下降迅猛程度(list[5]/list[3] < -0.08)
    # 12. G上升迅猛程度(Glist[5]/Glist[3] > 0.08)
    # sell gold
    # 1. B现在值小于平均值 (list[3] < list[9])
    # 2. B预测明天会涨(list[5] > 0)
    # 3. B涨的天数大于3天，小于6天(list[6] > 3 and list[6] < 6)
    # 4. B跌的天数超过6天(list[6]<= -6)
    # 5. B最近10天差值在跌，最大时间与最小时间差值在上升(list[13][29] > 0 and list[14] > 0)???????????
    # 6. G现在值大于平均值（Glist[3] > list[9])
    # 7. G预测明天会跌(Glist[5] > 0)
    # 8. G跌的天数大于3天，小于6天(Glist[6] < -3 and Glist[6] > -6)
    # 9. G涨的天数超过6天(Glist[6]>= 6)
    # 10. G最近10天差值在涨，最大时间与最小时间差值在下降(Glist[13][29] < 0 and list[14] < 0)??????????
    # 11. B上升迅猛程度(list[5]/list[3] > 0.08)
    # 12. G下降迅猛程度(Glist[5]/Glist[3] < -0.08)

    # 0手上美元，1手上黄金，2手上比特币，3现今价格，4预测价格，5预测与现价之差，6涨跌天数（正为涨，负为跌）
    # 7最大值，8最小值，9平均值，10[40天值]，11[40天间隔一天的差值（39个）前减后]
    # ，12[40天间隔两天差值（38个）前减后]，
    # 13[40天间隔10天差值（30个）前减后],14 最大值时间和最小值时间差值
    num = 0.0
    # if (list[6] > 2):
    #     num = -0.08
    #     if(list[9] >= list[3]):
    #         num = num * 0.8
    #     else:
    #         num = num*1.1
    # elif (list[6] == 2):
    #     num = -0.05
    #     if (list[9] >= list[3]):
    #         num = num * 0.7
    #     else:
    #         num = num *1.1
    # elif (list[6] < -3):
    #     num = 0.15
    #     if (list[9] <= list[3]):
    #         num = num * 0.8
    #     else:
    #         num = num *1.1
    # elif (list[6] == -3):
    #     num = 0.4
    #     if (list[9] <= list[3]):
    #         num = num * 0.8
    #     else:
    #         num = num *1.1
    num = 1
    # gold
    #5.214285714	4.571428571	6.571428571	5.142857143	6.928571429	5.357142857	4	5.285714286	6	6	5.428571429	6.785714286
    # numList = [6, 5, 7, 1, 1, 2, 4, 8, 4, 4, 2, 8]
    numList = [6, 0, 7, 1, 1, 2, 0, 8, 4, 4, 0, 0]
    flag = True
    # numList = [5.214285714	,4.571428571	,6.571428571,	5.142857143,	6.928571429	,5.357142857	,4,	5.285714286	,6,	6,	5.428571429,	6.785714286]
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
    # if (sellwhat > 0.5):
    #     num = ratelist[0]
    # elif (sellwhat > 0.3):
    #     num = ratelist[1]
    # elif buywhat > 0.5:
    #     num = ratelist[2]
    # elif buywhat > 0.3:
    #     num = ratelist[3]
    # else:
    #     num = ratelist[-1]
    if sellwhat > buywhat:
        num = -sellwhat
    if buywhat > sellwhat:
        num = buywhat
    if (flag == True):
        if (list[15] == 40):
            num = 0.4
            flag = False
        else:
            if (num > 0):
                num = 0.6
                flag = False
    return num


def buyHowManyB(i,money,listPast,listFuture,recentMoney,Glistpast,GlistFuture,GrecentMony,goldCommission):
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
    manylist = getBTClist(i, money, listPast, listFuture, recentMoney)
    Gmanylist = getGoldlist(i,money,Glistpast,GlistFuture,GrecentMony)
    many = getBTCback(manylist,Gmanylist)
    # many = getBTCback1(manylist)
    x = random.randint(1,(25 - int(math.fabs(many))*10)*int(bitcoinCommission * 100))
    # x = random.randint(1, (25 - int(math.fabs(many)) * 10))
    # if math.fabs(many) < 0.4 and x > 1:
    if math.fabs(many) < 0.6 and x > 1:
    # if x > 1:
        many = 0
    else:
        many = many
#many -1 ~ 1
    return many


def buyHowManyG(i,money,Blistpast,BlistFuture,BrecentMoney,listPast,listFuture,recentMoney,goldCommission):
    # print("ggggggggggggggggggggggggggggggggggggg")
    # print(money)
    # print(listPast)
    # print(listFuture)
    # print(recentMoney)
    # print("gggggggggggggggggggggggggggggggggggggg")

    manylist = getGoldlist(i,money,listPast,listFuture,recentMoney)
    Bmanylist = getBTClist(i,money,Blistpast,BlistFuture,BrecentMoney)
    # print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    # print(i)
    many = getGoldback(Bmanylist,manylist)
    # x = random.randint(1, (25 - int(math.fabs(many)) * 10))
    x = random.randint(1, (25 - int(math.fabs(many))*10)*int(goldCommission * 100))
    # many = getGoldback1(manylist)
    # if math.fabs(many)< 0.4 and x > 1:
    if math.fabs(many) < 0.6 and x > 1:
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
    bitcoinCommission = 0.03
    goldCommission = 0.02
    test_time = 1825
    USdollarlist = []
    for i in range(0,test_time):
        # what_to_do = rand.randint(1, 9)
        # what_to_do = 3
        print("bitcoin = $" + str(bitcoin[n][1]))
        if(i >= 40):
            BTHlistpast = bitcoin[i-40:i]
            BTHlistpred = bitcoinpred[i+1]
            BTHdallor = bitcoin[n][1]
            GOLDlistpast = gold[i - 40:i]
            GOLDlistpred = goldpred[i + 1]
            GOLDdallor = gold[i][1]
            buyHowManyBTCnum = buyHowManyB(i,money,BTHlistpast,BTHlistpred,BTHdallor,GOLDlistpast, GOLDlistpred, GOLDdallor,bitcoinCommission)
            buyHowManyGOLD = 0
            if gold[i][2] == 'TRUE':
                print("gold = $" + str(gold[i][1]))
                buyHowManyGOLDnum = buyHowManyG(i,money,BTHlistpast,BTHlistpred,BTHdallor,GOLDlistpast, GOLDlistpred, GOLDdallor,goldCommission)
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
                buy_gold(x, i,goldCommission)
                commission=commission+0.01*x
                print("buy gold")
            else:
                print("No buy No sell")
        elif what_to_do == 3:#buy bitcoin
            x = math.fabs(buyHowManyBTCnum)*money[0]
            # x = 0.5
            buy_bitcoin(x, n,bitcoinCommission)
            commission = commission + 0.02 * x
            print("buy bitcoin")
        elif what_to_do == 4:# buy both
            x = math.fabs(buyHowManyGOLDnum)*money[0]
            buy_bitcoin(x, n,bitcoinCommission)
            commission = commission + 0.02 * x
            if gold[i][2] == 'TRUE':
                x = math.fabs(buyHowManyBTCnum)*money[0]
                buy_gold(x, i,goldCommission)
                commission = commission + 0.01 * x
                print("buy both")
            else:
                print("buy bitcoin")
        elif what_to_do == 5:#sell gold
            if gold[i][2] == 'TRUE':
                y = math.fabs(buyHowManyGOLDnum)*money[1]
                commission = commission + 0.01 * y
                sell_gold(y, i,goldCommission)
                print("sell gold")
            else:
                print("No buy No sell")
        elif what_to_do == 6:#sell bitcoin
            y = math.fabs(buyHowManyBTCnum)*money[2]
            commission = commission + 0.02 * y
            sell_bitcoin(y, n,bitcoinCommission)
            print("sell bitcoin")
        elif what_to_do == 7:#sell both
            y = math.fabs(buyHowManyBTCnum)*money[2]
            commission = commission + 0.02 * y
            sell_bitcoin(y, n,bitcoinCommission)
            if gold[i][2] == 'TRUE':
                y = math.fabs(buyHowManyGOLDnum)*money[1]
                commission = commission + 0.01 * y
                sell_gold(y, i,goldCommission)
                print("sell both")
            else:
                print("sell bitcoin")
        elif what_to_do == 8:#buy GOLD and sell BTC
            y = math.fabs(buyHowManyBTCnum)*money[2]
            sell_bitcoin(y,n,bitcoinCommission)
            commission = commission + 0.02 * y
            if gold[i][2] == 'TRUE':
                x = math.fabs(buyHowManyGOLDnum)*money[0]
                commission = commission + 0.01 * x
                buy_gold(x, i,goldCommission)
                print("buy gold and sell BTC")
            else:
                print("sell BTC")
        elif what_to_do == 9:#buy BTC and sell GOLD
            if gold[i][2] == 'TRUE':
                x = math.fabs(buyHowManyGOLDnum)*money[1]
                commission = commission + 0.01 * x
                sell_gold(x, i,goldCommission)
                print("buy BTC and sell GOLD")
            else:
                print("buy BTC")
            y = math.fabs(buyHowManyBTCnum)*money[0]
            commission = commission + 0.02 * y
            buy_bitcoin(y, n,bitcoinCommission)
        if gold[i][2] == 'TRUE':
        # if i % 7 == 1 or i % 7 == 2 or i % 7 == 3 or i%7 == 4 or i % 7 == 0:
            m = m+1
        n = n+1
        print(str(n)+'days')
        # print(i)
        USdollar = showWholeMoney(m,n)
        lllist = []
        lllist.append(USdollar)
        USdollarlist.append(lllist)
        if max < USdollar:
            max = USdollar



    # plt.figure(facecolor='gray')
    plt.style.use({'figure.figsize': (20, 8)})
    plt.ylabel('Value')
    plt.xlabel('Date')
    plt.plot(USdollarlist,color="orange")
    plt.show()
    print("max= " + str(max))
    print('commission=' + str(commission))
    print(USdollarlist)
    with open('111/yes.csv', 'w+', newline='') as f:
        csv_file = csv.writer(f)
        csv_file.writerows(USdollarlist)
    print(len(gold))
    print(n)