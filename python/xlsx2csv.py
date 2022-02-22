# ---
# author: jzh
# date: 2022.02.19
# ---
import pandas as pd


def xlsx_to_csv_pd():
    data_xls = pd.read_excel('mypred2.xls', index_col=0)
    data_xls.to_csv('mypred2.csv', encoding='utf-8')


if __name__ == '__main__':
    xlsx_to_csv_pd()