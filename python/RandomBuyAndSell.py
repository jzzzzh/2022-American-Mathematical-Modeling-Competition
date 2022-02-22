# ---
# author: jzh
# date: 2022.02.18
# ---
import numpy as np
import csv
import random as rand
import matplotlib.pyplot as plt
bitcoin = []
gold = []
# money[usd, gold, bitcoin]
money = [1000, 0, 0]

m = 0
n = 0
def read():
    with open('BCHAIN-MKPRU.csv') as f:
        f_csv = csv.reader(f)
        list_f_csv = list(f_csv)
        date = list_f_csv[1][0]
        for row in list_f_csv[2:]:
            bitcoin.append(row)
    with open('gold_finish.csv') as f:
        f_csv = csv.reader(f)
        list_f_csv = list(f_csv)
        date = list_f_csv[1][0]
        for row in list_f_csv[2:]:
            gold.append(row)
    # print(bitcoin)
    # print(gold)

def buy_bitcoin(x,n):
    #money is the whole money, x is the money buy bitcoin, n is the day
    if float(money[0]) >= x:
        true_buy_money = 0.98 * x
        bitcoin_num = true_buy_money/float(bitcoin[n+1][1])
        money[0] = money[0] - x
        money[2] = money[2] + bitcoin_num
    else:
        print("error,money buy bitcoin is not enough")

def sell_bitcoin(y,n):
    #money is the whole money, y is the money sell bitcoin, n is the day
    if float(money[2]) >= y:
        true_sell_money = 0.98 * y
        money_num = true_sell_money*float(bitcoin[n+1][1])
        money[0] = money[0] + money_num
        money[2] = money[2] - y
    else:
        print("error,money sell bitcoin is not enough")


def sell_gold(y, m):
    # money is the whole money, y is the money sell gold, m is the day
    if float(money[1]) >= y:
        true_sell_money = 0.99 * y
        money_num = true_sell_money * float(gold[m + 1][1])
        money[0] = money[0]+ money_num
        money[2] = money[1] - y
    else:
        print("error,money sell bitcoin is not enough")


def buy_gold(x,m):
    #money is the whole money, x is the money buy gold, m is the day
    if float(money[0]) >= x:
        true_buy_money = 0.99 * x
        gold_num = true_buy_money/float(gold[m+1][1])
        money[0] = money[0] - x
        money[1] = money[1] + gold_num
    else:
        print("error,money buy gold is not enough")




def showWholeMoney(m,n):
    #money is the whole money, m is the gold day, n is the bitcoin day,
    print(money)
    whole_money = money[0] + money[1]*float(gold[m + 1][1]) + money[2]*float(bitcoin[n+1][1])
    # whole_money = money[0] + money[2]*float(bitcoin[n+1][1])
    # whole_money = money[0] + money[1]*float(gold[m+1][1])
    # print(float(gold[m+1][1]))
    # print(m)
    # print(gold[m+1])
    print('$  ' + str(whole_money))
    return whole_money

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
    test_time = 1000
    USdollarlist = []
    for i in range(0,test_time):
        what_to_do = rand.randint(1, 7)
        # what_to_do = 3
        print("bitcoin = $" + str(bitcoin[n+1][1]))


        if i % 7 == 1 or i % 7 == 2 or i % 7 == 3 or i % 7 == 4 or i % 7 == 0:
            print("gold = $" + str(gold[m+1][1]))


        # print(what_to_do)
        if what_to_do == 1: #不动
            print("No buy No sell")
        if what_to_do == 2: #buy gold
            if i % 7 == 1 or i%7 == 2 or i % 7 == 3 or i%7 == 4 or i % 7 == 0:
                x = rand.randrange(0,100,1)*money[0]*0.01
                buy_gold( x, m)
                print("buy gold")
            else:
                print("No buy No sell")
        if what_to_do == 3:#buy bitcoin
            x = rand.randrange(0,100,1)*money[0]*0.01
            # x = 0.5
            buy_bitcoin(x, n)
            print("buy bitcoin")
        if what_to_do == 4:# buy both
            x = rand.randrange(0,100,1)*money[0]*0.01
            buy_bitcoin(x, n)
            if i % 7 == 1 or i%7 == 2 or i % 7 == 3 or i%7 == 4 or i % 7 == 0:
                x = rand.randrange(0,100,1)*money[0]*0.01
                buy_gold(x, m)
                print("buy both")
            else:
                print("buy bitcoin")
        if what_to_do == 5:#sell gold
            if i % 7 == 1 or i % 7 == 2 or i % 7 == 3 or i % 7 == 4 or i % 7 == 0:
                y = rand.randrange(0,100,1)*money[1]*0.01
                sell_bitcoin(y, m)
                print("sell gold")
            else:
                print("No buy No sell")
        if what_to_do == 6:#sell bitcoin
            y = rand.randrange(0,100,1)*money[2]*0.01
            sell_bitcoin(y, n)
            print("sell bitcoin")
        if what_to_do == 7:#sell both
            y = rand.randrange(0,100,1)*money[2]*0.01
            sell_bitcoin(y, n)
            if i % 7 == 1 or i % 7 == 2 or i % 7 == 3 or i % 7 == 4 or i % 7 == 0:
                y = rand.randrange(0,100,1)*money[1]*0.01
                sell_bitcoin(y, m)
                print("sell both")
            else:
                print("sell bitcoin")
        if i % 7 == 1 or i % 7 == 2 or i % 7 == 3 or i%7 == 4 or i % 7 == 0:
            m = m+1
        n = n+1
        print(n)
        USdollar = showWholeMoney(m,n)
        USdollarlist.append(USdollar)
        if max < USdollar:
            max = USdollar
    plt.plot(USdollarlist,color="green")

    plt.show()
    print("max= " + str(max))
