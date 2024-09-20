lista_de_numeros = [

]

while True:
    numeros = int(input('Digite um número: '))
    lista_de_numeros.append(numeros)
    escolha_user = input('Quer continuar?[S/N]: ')
    if escolha_user.strip().lower()[0] == 'n':
        break
lista_de_numeros.sort(reverse=True)
print(f'Valores digitados foram', len(lista_de_numeros))
print(lista_de_numeros)
if 5 in lista_de_numeros:
    print('5 Faz parte da lista')
else:
    print('5 Não faz parte da lista')