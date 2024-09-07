s = n = c = 0
while n != 999:
    c += 1; s += n; n = int(input('Digite um número (999 para parar): '))
print('A soma dos {} números digitados resultou em: {}'.format(c - 1, s))
