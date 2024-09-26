def fatorial(valor, show=False):
    """
    --> Calcula o fatorial de um número
    :param valor: Coleta o valor que irá ser feito o calculo de fatorial
    :param show: (opcional) Se for True irá mostrar o cálculo, se for false ele irá mostrar apenas a resposta
    :return: retorna a resposta desejada
    """
    result = 1
    for i in range(valor, 0, -1):
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        result *= i
    return result


print(fatorial(5, False))
help(fatorial)
