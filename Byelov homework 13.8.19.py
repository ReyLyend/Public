#количество нужных билетов
tickets = int(input("How many tickets do you want to buy? -> "))
#возраст каждого посетителя
age_of_all_visitors = [int(input(f"How old is the {i} visitor? -> ")) for i in range(1,tickets+1)]
#сумма к оплате
total = 0
#количество платных билетов, чтоб дать скидку, если больше 3
charged_tickets = 0
#расчёт общей суммы
for age in age_of_all_visitors:
    if 18 <= age < 25:
        total += 990
        charged_tickets += 1
    if age >= 25:
        total += 1390
        charged_tickets += 1
#вывод общей суммы с учетом скидки
print(total * 0.9 if charged_tickets > 3 else total)