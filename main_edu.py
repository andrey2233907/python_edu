# PANDAS
import pandas as pd

# seri = pd.Series(['Дерево', 'Металл', 'Камень'], index=['Антон', 'Олег', 'Петр'])
# # print(seri)
# dict1 = {
#     'id': [0, 1, 2],
#     'name': ['Дерево', 'Металл', 'SSSSSS'],
#     'Цена': [10, 100, 101]
# }
# df = pd.DataFrame(dict1)
# print(df[df['Цена'] > 20])


# df = pd.read_csv('data.csv').fillna('-')
# cleaned = df.dropna()
# # print(cleaned[cleaned['port'] == 445])
# print(df.describe())


df = pd.read_csv('data.csv').fillna('Underfined')
# high = df[df['severity'] == 'high']
# critical = df[df['severity'] == 'critical']
# medium = df[df['severity'] == 'medium']
# merged = critical.merge(medium, 'outer').merge(high, 'outer')
# print(merged)
# sorted = df[df['severity'].isin(['medium', 'high', 'medium'])]
# sorted = df[df['source_ip'].str.contains('192.168')]
# sorted = df.sort_values('bytes_sent', ascending=False)
# sorted = df.groupby('protocol').count()['timestamp']
# print(sorted)



# MATPLOTLIB



import matplotlib.pyplot as plt
# df = pd.read_csv('data.csv')
# df.plot()

# x = list(range(-10, 11))
# y = [i**2 for i in x]
# plt.style.use('dark_background')
# plt.plot(x, y)
# plt.pie([1, 2, 3, 4, 5])
# plt.legend('')
# plt.xlabel('ось Х')
# plt.ylabel('ось У')
# plt.title('наш график')
# plt.show()


# df = pd.read_csv('ips.csv')
# plt.pie(df['data_transfered'].to_list(), colors=["#E2E2E2"])
# plt.legend(df['ip'].to_list())

# plt.show()

# legend = df['ip']
# values = df['data_transfered']
# plt.xticks(rotation=45)
# plt.bar(legend, values, 1)
# plt.show()



# SYS, OS, DATETIME, ARGPARSE

import sys
import os
import argparse
from datetime import datetime
# print(sys.argv)



# path = sys.argv[1]
# if not os.path.exists(path):
#     print(f'Файла по такому пути не существует')
#     exit()
# if not os.access(path, os.R_OK):
#     print(f'Нет доступа на чтение')
#     exit()
# with open(path) as file:
#     for line in file:
#         print(f'{line.strip()}')

# dirname = sys.argv[1] if len(sys.argv) > 1 else 'new dir'
# os.mkdir(dirname)



# parser = argparse.ArgumentParser()
# parser.add_argument('output_path', help='Путь к файлу для записи')
# parser.add_argument('-p', '--path', help='путь к файлу для чтения')
# parser.add_argument('-r', '--register', help='Переводит все строки файла в верхний регистр', action='store_true', required=False)

# args = parser.parse_args()
# if not os.path.exists(parser.path):
#     print('Файла не существует')
#     exit()

# with open(args.path, encode='utf-8') as file:
#     for line in file:
#         if args.register:
#             print(line.upper().strip())
#         else:
#             print(line.strip())
        


# print(datetime.now())





# RE 




import re


# ^ - начало строки
# \w - любая буква или цифра
# [] - любой символ из тех что внутри скобок
# + - 1 или более символов
# \d - любая цифра
# . - любой символ (внутри скобок - просто точка)
# $ - конец строки
# {n,n} - количество символов от n до n
# {n,} - количество чимволов от n до бесконечности
# 0 или более символов
# ? - 0 или 1 символов
# | - или


# string = 'andrey2233907@gmail.com'
# regex = r'^[\w-.]+@[\w]+\.[/w]+'

# result = re.search(regex, string)
# if result != None:
#     print('строка подходит')



# data = '24.01.6475-23:10'
# regex = r'^\d{2}\.\d{2}\.\d{4}-\d{2}:\d{2}$'
# result = re.search(regex, data)
# if result != None:
#     print('Дата подходит')
# else:
#     print('Непрвильно')



# regex = r'^(\w{4}: ).*'
# time = 'INFO: Hello'
# str2 = ''

# res = re.sub(regex, r'\1SYSTEM', time)
# print(res)



pwd = sys.argv[1]

regex_len = r'.{12,}'
regex_special = r'[!@#$%^&*()_+=-?:;№"~`]+'
regex_num = r'[\d]+'
regex_up = r'[A-Z]+'
regex_low = r'[a-z]+'

res_low = True if re.search(regex_low, pwd) != None else False
res_up = True if re.search(regex_up, pwd) != None else False
res_special = True if re.search(regex_special, pwd) != None else False
res_len = True if re.search(regex_len, pwd) != None else False
res_num = True if re.search(regex_num, pwd) != None else False


print(f'''Результат проверки пароля:
Наличие нижнего регистра: {res_low}
Наличие верхнего регистра: {res_up}
Наличие специального символа: {res_special}
Наличие цифры: {res_num}
12 символов или длиннее: {res_len}
''')

