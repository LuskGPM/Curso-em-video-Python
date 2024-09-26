from time import sleep


def valores(*num):
    print('Analisando os valores passados...')
    sleep(1)
    print('=' * 60)
    for i in num:
        print(i, end=' ', flush=True)
        sleep(0.3)
    print(f'Foram passados {len(num)} valores ao todo')
    sleep(1)
    if num:
        print(f'O maior valor informado foi {max(num)}')
        sleep(1)
    print('=' * 60)


valores(4, 9, 2, 10, 24)
valores(9, 1, 3)
valores(99, 318, 312, 318)
valores()
