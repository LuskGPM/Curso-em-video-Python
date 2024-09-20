lista_valores = []
while True:
    valor_digitado = int(input('Digite um valor: '))
    if valor_digitado not in lista_valores:
        lista_valores.append(valor_digitado)
        print('Valor adicionado na lista')
    else:
        print('Valor duplicado, não adicionado na lista')
    user_continuar = input('Continuar? [S/N]: ')
    if user_continuar.strip().lower()[0] == "n":
        break
print('Valores digitados:', sorted(lista_valores))
