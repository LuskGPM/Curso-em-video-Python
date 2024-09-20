"""
lista = [
    'Lucas',
    'Gabriel',
    'Pereira',
    'de',
    'Melo',
    19,
    'Anos'
]
#lista.pop(2)
if 'de' in lista:
    lista.remove('de')
lista.pop()
for itens in lista:
    print(itens, end=' ')

valores = (list(range(4, 11)))
print(valores)
valores.insert(2, 'Lucas')
print(valores)
valores.clear()
print(valores)
"""

lista_valores = [

]
for c in range(0, 5):
    valor = int(input(f'Digite um número para o campo {c}: '))
    lista_valores.insert(c, valor)
print('Você digitou os valores:', lista_valores)
print('O maior valor foi', max(lista_valores))
print('O menor valor foi', min(lista_valores))
for i, valor in enumerate(lista_valores):
    if valor == max(lista_valores):
        print('O maior valor está na posição', i)
    elif valor == min(lista_valores):
        print('O menor valor está na posição', i)
