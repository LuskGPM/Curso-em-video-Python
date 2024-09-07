escolha = input('Digite "C" para converter em Celsius e "F" para Fahrenheit: ')
while escolha.upper() != 'C' and escolha.upper() != 'F':
    escolha = input('Tente novamente, C ou F: ')
valor = float(input('Temperatura: '))
if escolha.upper() == "F":
    F = (valor * 9/5) + 32
    print(f'Valor em fahrenheit é: {F:.1f}F°')
else:
    C = (valor - 32) * 5/9
    print(f'Valor em Celsius é: {C:.1f}C°')