lista_numeros = [

]
for c in range(5):
    valor_adicionado = int(input('Digite um número: '))
    if c == 0 or valor_adicionado > lista_numeros[-1]:
        lista_numeros.append(valor_adicionado)
        print('Adicionado no final da lista')
    else:
        pos = 0
        while pos < len(lista_numeros):
            if valor_adicionado <= lista_numeros[pos]:
                lista_numeros.insert(pos, valor_adicionado)
                print('Adicionado na posição', pos)
                break
            pos += 1
print(lista_numeros)
