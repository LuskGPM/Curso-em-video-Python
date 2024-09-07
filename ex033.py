n1 = int(input('Número: '))
n2 = int(input('Mais um: '))
n3 = int(input('Último: '))
menor = n1
maior = n1
if n1 < n2:
    maior = n2
if n2 < n3:
    maior = n3
if n1 > n2:
    menor = n2
if n2 > n3:
    menor = n3
print(f'Menor número foi {menor} e o maior foi {maior}')
