from random import randint
from time import sleep

numero_sorteados = list()

print('=' * 40)
print(f"{'JOGAR NA MEGA SENA':^40}")
print('=' * 40)
numero_de_jogos = int(input('Quantos jogos você quer que eu sorteie? '))

print('=-' * 5, f'SORTEANDO {numero_de_jogos} JOGOS', '=-' * 5)
for i in range(numero_de_jogos):
    for n in range(6):
        numero_aleatorio = randint(1, 60)
        while numero_aleatorio in numero_sorteados:
            numero_aleatorio = randint(1, 60)
        numero_sorteados.append(numero_aleatorio)

    print(f'Jogo {i + 1}: {numero_sorteados}')
    numero_sorteados.clear()
    sleep(0.5)
print(f'{" < Boa Sorte! > ":=^40}')
