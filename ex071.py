valor = int(input('Valor para sacar: R$'))
cedulas = 100
ncedulas = 0
while True:
    if valor >= cedulas:
        valor -= cedulas
        ncedulas += 1
    else:
        if ncedulas > 0:
            print(f'Total de {ncedulas} de {cedulas}')
        if cedulas == 100:
            cedulas = 50
        elif cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 5
        elif cedulas == 5:
            cedulas = 2
        ncedulas = 0
        if valor == 0:
            break
