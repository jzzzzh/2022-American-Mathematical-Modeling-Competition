import numpy as np
import csv
import random as rand
import datetime
bitcoin = []
gold = []
# money[usd, gold, bitcoin]
money = [1000, 0, 0]

m = 0
n = 0
with open('BCHAIN-MKPRU.csv') as f:
    f_csv = csv.reader(f)
    list_f_csv = list(f_csv)
    # date = list_f_csv[1][0]
    # print(date)

    # ans = datetime.datetime.strptime('9/11/2016',"%m/%d/%Y")
    # print(type(date))
    # print(ans)
    # print(type(ans))
    for row in list_f_csv[2:]:
        # print(row[0])
        x = row[0][-1]
        y = row[0][-2]
        ans = row[0][:-2]
        ans = ans +'20'
        ans = ans+y+x
        # print(ans)
        # print(type(x))
        ans0 = datetime.datetime.strptime(ans,"%m/%d/%Y")
        print(ans0)
        row[0] = ans0
        row[1] = float(row[1])
        bitcoin.append(row)
with open('bitcoin.csv','w',newline='')as f:
    f_csv = csv.writer(f)
    headers = ['date','val']
    f_csv.writerow(headers)
    f_csv.writerows(bitcoin)
# with open('LBMA-GOLD.csv') as f:
#     f_csv = csv.reader(f)
#     list_f_csv = list(f_csv)
#     date = list_f_csv[1][0]
#     for row in list_f_csv[2:]:
#         gold.append(row)
# print(bitcoin)
# print(gold)