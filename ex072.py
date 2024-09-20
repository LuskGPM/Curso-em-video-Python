"""from random import randint

n = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
n2 = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
nn2 = n + n2

print(n)
print(sorted(n))
print(n2)
print(sorted(n2))
print(nn2)
print(sorted(nn2))
print('')
print(nn2.count(4))
if nn2.count(4):
    print(nn2.index(4))
"""

numbers = (
    'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
    'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte',
)
numberSelect = int(input('Escolha um número de 0 a 20: '))
while numberSelect < 0 or numberSelect > len(numbers) - 1:
    print('inválido')
    numberSelect = int(input('Escolha um número de 0 a 20: '))
print(f'Você digitou o número {numbers[numberSelect]}')

print(sorted(numbers))