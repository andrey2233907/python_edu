# PANDAS
# import pandas as pd

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


# df = pd.read_csv('data.csv').fillna('Underfined')
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



# import matplotlib.pyplot as plt
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



# pwd = sys.argv[1]

# regex_len = r'.{12,}'
# regex_special = r'[!@#$%^&*()_+=-?:;№"~`]+'
# regex_num = r'[\d]+'
# regex_up = r'[A-Z]+'
# regex_low = r'[a-z]+'

# res_low = True if re.search(regex_low, pwd) != None else False
# res_up = True if re.search(regex_up, pwd) != None else False
# res_special = True if re.search(regex_special, pwd) != None else False
# res_len = True if re.search(regex_len, pwd) != None else False
# res_num = True if re.search(regex_num, pwd) != None else False


# print(f'''Результат проверки пароля:
# Наличие нижнего регистра: {res_low}
# Наличие верхнего регистра: {res_up}
# Наличие специального символа: {res_special}
# Наличие цифры: {res_num}
# 12 символов или длиннее: {res_len}
# ''')




# HTTP SERVER

import http.server

# class MyHandler(http.server.BaseHTTPRequestHandler):
#     # def do_GET(self):

#     #     self.send_response(200)
#     #     self.send_header('Content-Type', 'text/plain; charset=utf-8')
#     #     self.end_headers()
#     #     self.wfile.write('hELLO'.encode())
#     def do_GET(self):
#         self.send_header()


# try:
#     with http.server.HTTPServer(('0.0.0.0', 6767), MyHandler) as server:
#         print('Hosting')
#         server.serve_forever()
# except KeyboardInterrupt:
#     exit()




# beautifulsoup4, scapy, lxml, requests






# import requests

# response = requests.post('https://httpbin.org/post')
# response = requests.post('https://httpbin.org/post', params={'key1': 10, 'password': 'fawohu'})
# print(response.text)


# resp_dict = response.json()
# print(resp_dict['origin'])




# import bs4
# import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument('query', help='Запрос в duckduckgo')
# args = parser.parse_args()
# params = {
#     'q': args.query,
#     'ia': 'web'
# }

# # responce = requests.get('https://httpbin.org/html')
# # responce = requests.get('https://en.wikipedia.org/wiki/List_of_HTTP_status_codes', headers={'User-Agent': 'Mozilla'})
# responce = requests.get('https://duckduckgo.com/', params=params)
# soup = bs4.BeautifulSoup(responce.text, 'lxml')
# # print(soup.find('h1'))
# result = [i.find('a') for i in soup.find_all('li')]
# # print(soup.find_all('div', class_='mw-heading'))
# print(result)






# from scapy.all import *
# from scapy.layers.inet import TCP, IP, ICMP
# from scapy.sendrecv import send, sr1

# # pckt = IP(dst='10.1.123.244') / ICMP()
# pckt = IP(dst='10.1.123.224') / TCP(dport=9001) / 'https://clck.su/ZakWa'


# sr1(pckt)







# РАБОТА С API




# import requests
# import argparse
# import json

# parser = argparse.ArgumentParser()

# parser.add_argument('fields', nargs='+', help='Поля, которые вернет API')
# parser.add_argument('-e', '--endpoint', default='games', help='endpoint')

# args = parser.parse_args()
# URL = 'https://api.battlemetrics.com/games'
# request_params = {
#     'fields[game]': args.fields
# }

# response = requests.get(f'{URL}?page[size]=67&fields[game]={','.join(args.fields)}')

# print(response.text)
# print(json.dumps(response.json(), indent=2))


# for game in response.json()['data']:
#     print(game)


# for game in response.json()['data']:
#     print(f'id: {game['id']}')
#     for field in args.fields:
#         print(f'{field}: {game['attributes'][field]}')
#     print()






# SQL






# import argparse
# parser = argparse.ArgumentParser()
# import hashlib
# parser.add_argument('-u', required=False, help='Username')
# parser.add_argument('-p', required=False, help='password')
# args = parser.parse_args()
# import sqlite3

# conn = sqlite3.connect('database.db')
# cursor = conn.cursor()

# cursor.execute('''
# create table if not exists Users(
#     id integer  primary key autoincrement,
#     username varchar(30),
#     password varchar(64)
# );
# ''')


# if args.u != None and args.p != None:
#     pwdhash = hashlib.md5(args.p.encode()).hexdigest()
#     query = '''
#         insert into Users(username, password)
#         values (?, ?);
#     '''
#     cursor.execute(query, (args.u, pwdhash))

# cursor.execute('''
# select * from Users;
# ''')
# result = cursor.fetchall()

# print(result)
# conn.commit()




# BASE64, XOR




# import hashlib
# import argparse
# import base64

# parser = argparse.ArgumentParser()
# parser.add_argument('mode', help='Режимы работы программы (hash, base64, xor)')
# parser.add_argument('path', help='путь к файлу')
# parser.add_argument('-a', '--algorithm', help='Алгоритм хэширования (md5, sha256, sha512), по умолчанию - md5', default='md5')
# parser.add_argument('-o', '--output-file', help='Путь к файлу для вывода', required=False)
# parser.add_argument('-d', '--decode', action='store_true', help='Режим декодирования base64: True/False, по умолчанию - False')
# parser.add_argument('-k', '--key', help='Ключ для раюоты с xor', required=False)
# args = parser.parse_args()




# def hashfile(file_contents: str, algorithm: str) -> str:
#     encoded_file_contents = file_contents.encode()
#     hashed_file_contents = None
#     match algorithm:
#         case 'md5':
#             hashed_file_contents = hashlib.md5(encoded_file_contents).hexdigest()
#         case 'sha256':
#             hashed_file_contents = hashlib.sha256(encoded_file_contents).hexdigest()
#         case 'sha512':
#             hashed_file_contents = hashlib.sha512(encoded_file_contents).hexdigest()
#         case _:
#             print('Возможные виды хэширования: md5, sha256, sha512') 
#     return hashed_file_contents




# def base64_file(file_contents: str, decode: bool):
#     encoded_file_contents = file_contents.encode()
#     if decode:
#         result = base64.b64decode(encoded_file_contents)
#     else:
#         resilt = base64.b64encode(encoded_file_contents)
#     return resilt.decode()



# def xor(file_contents: str, key: str) -> str:
#     if key == None:
#         print('Для работы с xor нужно указать ключ по флагу -k')
#     result = ''
#     for i in range(len(file_contents)):
#         utf_file_char = ord(file_contents[i])
#         utf_key_char = ord(key[i % len(key)])
#         char_result = utf_file_char ^ utf_key_char
#         result += chr(char_result)
#     return result


# def print_or_write(result: str, output_file: str | None):
#     if output_file == None:
#         print(result)
#     else:
#         with open(output_file, 'w') as file:
#             file.write(result)



# def main():
#     with open(args.path) as file:
#         file_contents = file.read()
#         result = None
#         match args.mode:
#             case 'hash':
#                 result = hashfile(file_contents, args.algorithm)
#             case 'base64':
#                 result = base64_file(file_contents, args.decode)
#             case 'xor':
#                 result = xor(file_contents, args.key) 
#             case _:
#                 print("Возможные режимы работы программы: hash, base64, xor")
#                 exit()
#         print_or_write(result, args.output_file)

# if __name__ == '__main__':
#     main()




#АНАЛИЗ ЛОГОВ (не готово чутчут)





# import re
# def stat(regex, file):
#     stat = {}
#     for line in file:
#         regex_result = re.findall(regex, line)
#         if len(regex_result) == 0:
#             continue
#         if regex_result[0] in stat:
#             stat[regex_result[0]] += 1
#         else:
#             stat[regex_result[0]] = 1
#     file.seek(0)
#     return stat

# def anonmalies(stat):
#     avg = sum(stat.values()) / len(stat)
#     for item in stat.items():
#         if item[1] > avg * 1.5 or item[1] < avg * 0.33:
#             print(f'Anomaly in {item[0]}: {item[1]}')


# def get_errors(file, statuscode):
#     regex = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).+(\d\d\d)$'
#     stats = {}
#     for line in file:
#         regex_res = re.findall(regex, line)
#         if len(regex_res) < 2:
#             continue
#         if regex_res[1] != statuscode:
#             continue
#         if regex_res[0] in stat:
#             stat[regex_res[0]] += 1
#         else:
#             stat[regex_res[0]] == 1
#     return stats



# with open('access.log', 'r') as file:
#     hours_counter = stat(r'\d\d\d\d:(\d\d):\d\d:\d\d', file)
#     ip_counter = stat(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', file)
#     anonmalies(hours_counter)
#     anonmalies(ip_counter)
#     get_errors(file, 404)





# VIRUS TOTAL API




import json
import requests
from sys import argv
import base64

def get_scanners_by_result_type(scanners: dict, category: str) -> str:
    result = ''
    for item in scanners.items():
        if item[1]['category'] == category:
            result += f'{item[0]}, '
    return result



url_to_scan = argv[1]

b64_url = base64.urlsafe_b64encode(url_to_scan.encode()).decode().replace('=', '')

url = f'https://www.virustotal.com/api/v3/urls/{b64_url}'
headers = {'x-apikey': '7108cfaecffdd723e62c86b03179887e482f75ade06478a3b0c62b01c37880e1', 'accept': 'application/json'}

report = requests.get(url, headers=headers).json()
scanners = report['data']['attributes']['last_analysis_results']

print('statistics:')
print(f'malicious: {report['data']['attributes']['last_analysis_stats']['malicious']}; {get_scanners_by_result_type(scanners, 'malicious')}')
print(f'suspicious: {report['data']['attributes']['last_analysis_stats']['suspicious']}; {get_scanners_by_result_type(scanners, 'suspicious')}')
print(f'undetected: {report['data']['attributes']['last_analysis_stats']['undetected']}; {get_scanners_by_result_type(scanners, 'undetected')}')
print(f'harmless: {report['data']['attributes']['last_analysis_stats']['harmless']}; {get_scanners_by_result_type(scanners, 'harmless')}')
print(f'timeout: {report['data']['attributes']['last_analysis_stats']['timeout']}; {get_scanners_by_result_type(scanners, 'timeout')}')
