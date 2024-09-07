dias = int(input('Dias alugados: '))
km = float(input('Kilometros rodados: '))
aluguel = (60 * dias) + (0.15 * km)
print(f'Aluguel à pagar é de: R${aluguel:.2f}')