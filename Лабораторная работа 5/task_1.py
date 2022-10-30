from pprint import pprint

LAST_NUMBER = 15
list_of_numbers = [
    {'bin': str(bin(i)), 'dec': i, 'hex': str(hex(i)), 'oct': str(oct(i))}
    for i in range(LAST_NUMBER + 1)
]
pprint(list_of_numbers)
