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
sorted = df.groupby('protocol').count()['timestamp']
print(sorted)



