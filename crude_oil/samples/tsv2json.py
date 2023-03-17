import csv
import json

# Определяем функцию для преобразования чисел в int
def convert_ints(obj):
    for key, value in obj.items():
        if isinstance(value, str) and value.isdigit():
            obj[key] = int(value)
    return obj

# Открываем TSV-файл для чтения
with open('crude_oil_samples.tsv', 'r') as tsvfile:
    reader = csv.DictReader(tsvfile, delimiter='\t')
    # Преобразуем данные в список словарей
    rows = [dict(row) for row in reader]

# Открываем JSON-файл для записи
with open('crude_oil_samples.json', 'w') as jsonfile:
    # Записываем данные в формате JSON с сохранением числовых значений как int
    json.dump(rows, jsonfile, indent=4, ensure_ascii=False, default=convert_ints)
