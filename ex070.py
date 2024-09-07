print('==' * 15)
print('          Loja Melo')
print('==' * 15)
soma = c1000 = c = 0
while True:
    nome = input('Nome do produto: ')
    valor = float(input('Valor do produto: R$'))
    c += 1
    soma += valor
    if valor > 1000:
        c1000 += 1
    if c == 1 or valor < menorvalor:
        menorvalor = valor
        menornome = nome
    continuar = input('Quer continuar? [S/N]: ').strip()
    while continuar not in "SsNn":
        continuar = input('Quer continuar? [S/N]: ').strip()
    if continuar in "Nn":
        break
print(f'Valor total da compra foi de R${soma:.2f}')
print(f'{c1000} produtos custaram mais de R$1000')
print(f'O produto mais barato foi um(a) {menornome} que custou R${menorvalor:.2f}')
