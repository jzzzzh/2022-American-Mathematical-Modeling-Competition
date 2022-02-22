# ---
# author: jzh
# date: 2022.02.19
# ---
import pandas as pd
import openpyxl

def csv_to_xlsx_pd():
    csv = pd.read_csv(r'pred.csv', encoding='utf-8')
    csv.to_excel(r'mypred.xlsx', sheet_name='sheet1')


if __name__ == '__main__':
    csv_to_xlsx_pd()