from random import randint
print('Vamos jogar par ou impar')
c = 0
while True:
    nm = randint(0, 10)
    n = int(input('Diga um valor: '))
    pi = input('Par ou ímpar? [P/I]: ').strip().upper()
    if (nm + n) % 2 != 0:
        parim = "Impar"
    else:
        parim = "Par"
    if pi[0] in parim[0]:
        c += 1
        print(f'eu joguei {nm} e você jogou {n} que deu {nm + n} que é {parim}.\nVocê venceu.\nVamos mais uma...')
    else:
        print(f'Eu joguei {nm} e você jogou {n} que deu {nm+n} que é {parim}.\nVocê perdeu')
        break
print(f'Você venceu {c} vezes')
print('Game Over')
