money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
money_current = money_capital

month = 0  # количество месяцев, которое можно прожить

# TODO Оформить решение

while True:
    money_current += salary - spend
    spend = spend * (1 + increase)
    month += 1
    if money_current <= spend:
        break

print(month)
