qtd = int(input('Quantos termos: '))
t1 = 1
t2 = 0
while qtd != 0:
    t3 = t1 + t2
    print(t3, end=' -> ')
    t1 = t2
    t2 = t3
    qtd -= 1
print('FIM')
