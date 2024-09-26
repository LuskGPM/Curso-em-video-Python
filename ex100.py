from random import randint
from time import sleep

numbers = list()


def sorteando():
    print('Sorteando os 5 valores da lista: ', end='')
    for i in range(5):
        i = randint(1, 10)
        numbers.append(i)
        print(f'{i}', end=' ', flush=True)
        sleep(0.6)
    print()


def somandoPar():
    soma = 0
    for i in numbers:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores de {numbers} temos o total de {soma}')


sorteando()
somandoPar()
