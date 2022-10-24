def get_count_char(str_):
    str_lower = str_.lower()
    char_in_str_dict = {}
    for char in str_lower:
        if char.isalpha():
            if char not in char_in_str_dict:
                char_in_str_dict[char] = 1
            else:
                char_in_str_dict[char] += 1
    return char_in_str_dict


def percent_count_char(char_dict):
    percent_dict = {}
    sum_of_chars = sum(char_dict.values())
    PERCENT_CONST = 100
    for char in char_dict:
        percent_dict[char] = round(char_dict[char] / sum_of_chars * PERCENT_CONST, 2)
    return percent_dict


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
