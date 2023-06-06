import pandas as pd
import numpy as np
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Загрузка файла данных
data = pd.read_csv('enviromental_samples.tsv', delimiter='\t')
# unique использовал, чтобы узнать какие значения воспринимает код (None, nan (для NA и пустых строк))
# logging.info(data.iloc[:, 2].unique())
# Проверка на наличие пустых ячеек (исключая ячейки со значением 'None')
empty_cells = np.where(pd.isna(data))

# Вывод номеров строк и колонок с пустыми ячейками
if len(empty_cells[0]) > 0:
    logging.error('Пустые ячейки найдены в следующих местах:')
    for row, col in zip(empty_cells[0], empty_cells[1]):
        logging.error(f"Строка {row}, колонка {col}")
    exit(1)
else:
    logging.info('Пустых ячеек не найдено')
