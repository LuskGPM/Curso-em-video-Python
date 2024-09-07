pi = int(input('Primeiro termo: '))
rz = int(input('Razão: '))
c = 10
ct = 0
while c != 0:
    while c != 0:
        print(pi, end=' -> ')
        pi += rz
        c -= 1
        ct += 1
    c = int(input('Pausa\nQuer ver mais quantos termos? '))
print('Sequência finalizada com {} termos mostrados.'.format(ct))
