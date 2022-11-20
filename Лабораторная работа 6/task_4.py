import json
from itertools import zip_longest

INPUT_FILE = "input.csv"


def csv_to_list_dict(input_file_link: str, csv_new_line: str = '\n', csv_delimiter: str = ',') -> list[dict]:
    """Функция конвертер данных из csv в json формат

    Реализован функционал распознания "неполных" csv файлов:
    При отсутствии значений или заголовков, на места пропущенных данных подставляется значение None

    :param input_file_link: Ссылка на файл вхоных данных в формате csv
    :param csv_new_line: Разелитель строк в csv файле, по умолчанию '\\n'
    :param csv_delimiter: Разделитель значений в строке csv файла, по умолчанию ','
    :return: Возвращает список словарей формата [{column -> value}, ... , {column -> value}]
    название столбца — значение (аналог DictReader из модуля csv)
    :raises: ValueError, если аргуемнт csv_new_line равен аргументу csv_delimiter
    """

    # Проверка входных аргументов
    if csv_new_line == csv_delimiter:
        raise ValueError("Разделители строк и значений заданы одинаковыми символами:\n"
                         f"Разделитель строки: '{csv_new_line}'\n"
                         f"Разделитель значения: '{csv_delimiter}'")

    with open(input_file_link) as input_data:
        data_list = input_data.read().strip().split(csv_new_line)

    # Разделение входных данных на список заголовков и список списков данных
    csv_data = [data_line.split(csv_delimiter) for data_line in data_list]
    csv_headers_list = csv_data[0]
    csv_data_list = csv_data[1:]

    list_dict = []

    for csv_data_line in csv_data_list:

        # Объединение 2-х и более значений без заданного заголовка в общий список
        # для привеения к словарю без потери данных (методом zip_longest)
        if len(csv_data_line) - len(csv_headers_list) > 1:
            csv_data_line[len(csv_headers_list)] = csv_data_line[len(csv_headers_list):]
            del csv_data_line[len(csv_headers_list) + 1:]

        list_dict.append(dict(zip_longest(csv_headers_list, csv_data_line)))

    return list_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
