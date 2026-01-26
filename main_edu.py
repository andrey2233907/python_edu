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
plt.style.use('dark_background')
# plt.plot(x, y)
# plt.pie([1, 2, 3, 4, 5])
# plt.legend('')
# plt.xlabel('ось Х')
# plt.ylabel('ось У')
# plt.title('наш график')
# plt.show()


df = pd.read_csv('ips.csv')
# plt.pie(df['data_transfered'].to_list(), colors=["#E2E2E2"])
# plt.legend(df['ip'].to_list())

# plt.show()

legend = df['ip']
values = df['data_transfered']
plt.xticks(rotation=45)
plt.bar(legend, values, 1)
plt.show()
