import pandas as pd
import numpy as np

# Загрузка файла данных
data = pd.read_csv('имя_файла.tsv', delimiter='\t')

# Проверка на наличие пустых ячеек (исключая ячейки со значением 'NA')
empty_cells = np.where((pd.isnull(data)) & ~(data.values == 'NA'))

# Вывод номеров строк и колонок с пустыми ячейками
if len(empty_cells[0]) > 0:
    print('Пустые ячейки найдены в следующих местах:')
    for row, col in zip(empty_cells[0], empty_cells[1]):
        print(f"Строка {row}, колонка {col}")
else:
    print('Пустых ячеек не найдено')
