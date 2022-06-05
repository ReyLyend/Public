per_cent = {'TKB': 5.6, 'CKB': 5.9, 'VTB': 4.28, 'SBER': 4.0}
deposit = []
money = input('Input money value: \n')
for i in per_cent.values():
    deposit.append(round(float(money)*i/100))
print('deposit =', deposit)
print('Максимальная сумма, которую вы можете заработать -', max(deposit))

