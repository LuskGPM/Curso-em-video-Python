import datetime
money = float(input('Reais: R$'))
hoje = datetime.date(2024, 8, 20)
print(f'Com R${money}, você compra hoje ({hoje.day}/{hoje.month}/{hoje.year}) ${money/5.48:.2f} Dólares.')