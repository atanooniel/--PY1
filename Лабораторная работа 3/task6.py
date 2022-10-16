list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение

max_index = 0
for i in range(len(list_numbers)):  # перебираем все индексы
    num = list_numbers[max_index]
    current_num = list_numbers[i]
    if current_num > num:
        num = current_num
        max_index = i


list_numbers[9], list_numbers[-1] = list_numbers[-1], list_numbers[9]
print(list_numbers)
