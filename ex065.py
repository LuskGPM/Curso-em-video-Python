soma = maior = menor = c = 0
while True:
    n = int(input('Digite um número: '))
    soma += n
    c += 1
    if c == 1:
        maior = n
        menor = n
    cn = input('Quer continuar? [S/N]: ').strip()
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    if cn[0] in "Nn":
        break
    while cn[0] not in "NnSs":
        cn = input('Quer continuar? [S/N]: ')
print(f'Você digitou {c} números, a média deles foi {soma/c}.\nO maior número foi {maior} e o menor foi {menor}')
