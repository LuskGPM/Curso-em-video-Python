maior = 0
menor = 0
for c in range(1, 6):
    peso = int(input(f'Peso da {c}° Pessoa: '))
    if c == 1:
        maior=peso
        menor=peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso foi {maior}KG e o menor foi {menor}KG')