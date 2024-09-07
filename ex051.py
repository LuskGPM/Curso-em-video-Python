t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
for c in range(t, (t + (10 - 1) * r) + r, r):
    print(c, end=' -> ')
print('Acabou')