import csv
import json
# переменная для хранения словарей
listed = []
# открываем файл
with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    # проходим по файлу и добавляем словари в список
    for i in reader:
        listed.append(i)
# открываем файл для вывода и записываем в него результат программы
with open('output.txt', 'w') as file:
    file.write(json.dumps(listed, indent=4))
