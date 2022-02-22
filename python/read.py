# ---
# author: jzh
# date: 2022.02.19
# ---
import csv

import yaml

bitcoin = []
gold = []
bitcoinpred = []
goldpred = []

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
print(bitcoinpred)
print(goldpred)
print(bitcoin)
print(gold)