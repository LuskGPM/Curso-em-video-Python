soma = 0
count = 0
for c in range(0, 6):
    n = int(input('Digite um número: '))
    if n%2==0:
        soma = soma + n
        count += 1
print(f'{count} números eram pares e a soma deles resulta em: {soma}')