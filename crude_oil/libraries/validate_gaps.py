import pandas as pd
import numpy as np

# Загрузка файла данных
data = pd.read_csv('crude_oil_libraries.tsv', delimiter='\t')
# unique использовал, чтобы узнать какие значения воспринимает код (None, nan (для NA и пустых строк))
# print(data.iloc[:, 2].unique())
# Проверка на наличие пустых ячеек (исключая ячейки со значением 'None')
empty_cells = np.where(pd.isna(data))

# Вывод номеров строк и колонок с пустыми ячейками
if len(empty_cells[0]) > 0:
    print('Пустые ячейки найдены в следующих местах:')
    for row, col in zip(empty_cells[0], empty_cells[1]):
        print(f"Строка {row}, колонка {col}")
    exit(1)
else:
    print('Пустых ячеек не найдено')
