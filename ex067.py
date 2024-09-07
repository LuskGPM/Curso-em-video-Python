while True:
    n = int(input('Digite um valor para ver sua tabuada: '))
    if n < 0:
        break
    mult = 1
    while True:      
        print(f'{n} x {mult} = {n * mult}')
        mult += 1
        if mult > 10:
            break
    decisao = str(input('Deseja continuar? [S/N]: ')).strip()
    if decisao[0] not in "NnSs":
        print('Informação inválida, tarefa fechada.')
        break
    if decisao[0] in "Nn":
        break
print('Volte sempre e tenha um ótimo dia.')
