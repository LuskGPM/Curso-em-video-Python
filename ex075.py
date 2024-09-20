numeros_digitados= (
    int(input('Digite um número: ')),
    int(input('Outro número: ')),
    int(input('Outro número: ')),
    int(input('Último número: '))
)
c = 0
print(f'Você digitou os valores: ', end='')
for numeros in numeros_digitados:
    print(numeros, end=' ')
print(f'\nO valor 9 foi digitado {numeros_digitados.count(9)} vezes')
if 3 in numeros_digitados:
    print(f'O número 3 foi digitado na {numeros_digitados.index(3) + 1}° posição')
else:
    print('Valor 3 não foi digitado')
print('Os valores pares digitados foram: ', end='')
for numero_par in numeros_digitados:
    if numero_par % 2 == 0:
        print(numero_par, end=' ')
        c += 1
if c == 0:
    print('Nenhum.')