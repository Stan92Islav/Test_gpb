# Задание №1
# имеется текстовый файл file.csv, в котром разделитель полей с данными: | (верт. черта)
# пример ниже содержит небольшую часть этого файла(начальные 3 строки, включая строку заголовков полей)

"""
lastname|name|patronymic|date_of_birth|id
Фамилия1|Имя1|Отчество1 |21.11.1998   |312040348-3048
Фамилия2|Имя2|Отчество2 |11.01.1972   |457865234-3431
...
"""


# Задание
# 1. Реализовать сбор уникальных записей
# 2. Случается, что под одиннаковым id присутствуют разные данные - собрать отдельно такие записи

# Решение посредством pandas
import pandas as pd
df = pd.read_csv('file.csv', encoding='utf-8', sep='|')
unique = df.drop_duplicates()
identical_id = unique.loc[unique.duplicated(subset=["id"], keep=False)]

# Решение посредством модуля CSV
import csv
unique2 = {}

with open('file.csv', 'r', newline='', encoding='utf-8') as file:
    data = csv.DictReader(file, delimiter='|')

    for rows in data:
        if rows['id'] not in unique2:
            unique2.update({rows['id']: (rows['lastname'].strip(), rows['name'].strip(), rows['patronymic'].strip(), rows['date_of_birth'].strip())})
        else:
            print(f'Идентичные id: {rows['id']} - {(rows['lastname'].strip(), rows['name'].strip(), rows['patronymic'].strip(), rows['date_of_birth'].strip())}')
file.close()


# Задание №2
# в наличии список множеств. внутри множества целые числа
m = [{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]
# Задание: посчитать
#  1. общее количество чисел
#  2. общую сумму чисел
#  3. посчитать среднее значение
#  4. собрать все множества в один кортеж
# *написать решения в одну строку

quantity = len([i for i in m for j in i])
summ = sum(list(map(sum, m)))
mean = summ / quantity
tupl = tuple(m)			# Если я верно понял пункт 4 данного задания: собрать все множества, т.е. {....}
# Если имелось ввиду элементы всех множеств, то:
tupl2 = tuple(j for i in m for j in i)


# Задание №3
# имеется список списков
a = [[1,2,3], [4,5,6]]
# Задание:
# сделать список словарей
b = [{'k1': 1, 'k2': 2, 'k3': 3}, {'k1': 4, 'k2': 5, 'k3': 6}]

res_list = []
for i in a:
    res_dict = {}
    for j in i:
        res_dict['k'+str(j)] = j
    res_list.append(res_dict)
print(res_list)

res2 = [{'k'+str(j): j} for i in a for j in i]

res3 = [{'k'+str(j): j for i in a for j in i}]


# Задание №4
# Имеется папка с файлами
# Реализовать удаление файлов старше N дней

import os
import time

folder = "test"   # папка, из которой предстоит удаление файлов
N = 3             # количествто дней, как ориентир для удаления файлов, старше этого числа
os.chdir(os.path.join(os.getcwd(), folder))
list_of_files = os.listdir()    # получаем список файлов, хранящихся в указанной папке
current_time = time.time()      # текущее время

# производим итерацию по всем файлам
for i in list_of_files:
    # получаем место расположения файла(путь)
    file_location = os.path.join(os.getcwd(), i)
    if (current_time - os.stat(file_location).st_birthtime) > N * 86400:  # 86400 - количество секунд в одном дне
        print(f" Удалено : {i}")
        os.remove(file_location)


# Задание №5
# В наличии текстовый файл с набором русских слов(имена существительные, им.падеж)
# Одна строка файла содержит одно слово.

# Задание:
# Написать программу которая выводит список слов,
# каждый элемент списка которого - это новое слово,
# которое состоит из двух сцепленных в одно, которые имеются в текстовом файле.
# Порядок вывода слов НЕ имеет значения

# Например, текстовый файл содержит слова:
# ласты
# стык
# стыковка
# баласт
# кабала
# карась

# Пользователь вводмт первое слово: ласты
# Программа выводит:
# ластык
# ластыковка
#
# Пользователь вводмт первое слово: кабала
# Программа выводит:
# кабаласты
# кабаласт
#
# Пользователь вводмт первое слово: стыковка
# Программа выводит:
# стыковкабала
# стыковкарась

def connecting_words(w1, w2):
    w1_chars = w1[-2:]
    if w1_chars in w2 and w1 != w2:
        conn_pos = w2.find(w1_chars) + 2
        connect = w2[:conn_pos]

        if w1.endswith(connect):
            w2_out_chars = w2[conn_pos:]
            new_connect = connecting_words(w1, w2_out_chars)

            if new_connect:
                return new_connect
            else:
                return w1 + w2_out_chars


with open('/home/soer/Загрузки/ласты.txt', 'r', encoding='utf-8') as file:
    words = [line.strip() for line in file]

word_input = str(input('Введите слово: '))

for i in words:
    connected_words = connecting_words(word_input, i)
    if connected_words:
        print(connected_words)


# Задание №6
# Имеется банковское API возвращающее JSON
# {
# 	"Columns": ["key1", "key2", "key3"],
# 	"Description": "Банковское API каких-то важных документов",
# 	"RowCount": 2,
# 	"Rows": [
# 		["value1", "value2", "value3"],
# 		["value4", "value5", "value6"]
# 	]
# }
# Основной интерес представляют значения полей "Columns" и "Rows",
# которые соответственно являются списком названий столбцов и значениями столбцов

# Задание:
# 	1. Получить JSON из внешнего API
# 		ендпоинт: GET https://api.gazprombank.ru/very/important/docs?documents_date={"начало дня сегодня в виде таймстемп"}
# 	2. Валидировать входящий JSON используя модель pydantic
# 		(из ТЗ известно что поле "key1" имеет тип int, "key2"(datetime), "key3"(str))
# 	3. Представить данные "Columns" и "Rows" в виде плоского csv-подобного pandas.DataFrame
# 	4. В полученном DataFrame произвести переименование полей по след. маппингу
# 		"key1" -> "document_id", "key2" -> "document_dt", "key3" -> "document_name"
# 	5. Полученный DataFrame обогатить доп. столбцом:
# 		"load_dt" -> значение "сейчас"(датавремя)

import requests
from datetime import datetime
from pydantic import BaseModel
import json
import pandas as pd

current_time = datetime.now().timestamp()
# Получение JSON из внешнего API
response = requests.get(f'https://api.gazprombank.ru/very/important/docs?documents_date={current_time}')

if response.status_code == 200:
    data_json = response.json()
    print(data_json)
else:
    print('Error')

# Валидация вх JSON
class bank(BaseModel):
    key1: int
    key2: datetime
    key3: str

valid = bank.parse_raw(data_json)

# Экспорт JSON в pandas, создание датафрейма с интересующими столбцами
df = pd.json_normalize(data_json)[['Columns', 'Rows']]

# Не совсем понятно условие п.5: "Представить данные "Columns" и "Rows" в виде плоского csv-подобного pandas.DataFrame"

# Переименование полей key1, key2, key3
df = df.rename(columns={"key1": "document_id", "key2": "document_dt", "key3": "document_name"})
# Сегодняшнее время
today = datetime.now()
# Обогащение доп столбцом
df.insert(loc=len(df.columns), column='load_dt', value=today)








