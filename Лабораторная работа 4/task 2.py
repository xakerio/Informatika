# TODO импортировать необходимые молули
import csv # импортируем модуль csv для чтения csv-файла и модуль json для записи данных в json
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

# создаём функцию task(), которая записывает записывает файл, но ничего не возвращает
def task() -> None:
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as f: # открываем csv-файл c кодировкой utf-8; r-чтение(with автоматически закроет файл)
        read = csv.DictReader(f) # DictReader читает csv и превращает строки в словари, первая строка является названиями столбцов
        data = list(read) # преобразовываем строки в список словарей

    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as f: # открываем json-файл для записи с кодировкой utf-8; w-режим записи
        json.dump(data, f, ensure_ascii=False, indent=4) # записываем данные в json с отступами по 4(indent)
        #ensure_ascii = False - чтобы русские символы не изменялись
if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")