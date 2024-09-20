from random import randint
from time import sleep
from operator import itemgetter

dados = dict()
ranking = dict()

for i in range(4):
    dados[f'Jogador{i + 1}'] = randint(1, 6)
    print(f'Jogador{i + 1} Jogou {dados[f"Jogador{i + 1}"]}')
    sleep(0.7)

ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
print('='*30)
for i, jogo in enumerate(ranking):
    print(f'{i + 1}° Lugar {jogo[0]} com {jogo[1]}')
    sleep(0.7)