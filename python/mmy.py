
import random
import numpy as np
import random as rand
import matplotlib.pyplot as plt
import math
import csv
import strategy
commission = 0.0
bitcoin = []
gold = []
bitcoinpred = []
goldpred = []
mypred2 = []
money = [1000, 0, 0]
m = 0
n = 0
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