def resumo(preço=0, aumento=0, redução=0):
    print('=' * 50)
    print(f'{"RESUMO DO VALOR":^50}')
    print('=' * 50)
    print(f'{"Preço analisado:":<30} {moeda(preço):>20}')
    print(f'{"Dobro do preço:":<30} {dobro(preço):>20}')
    print(f'{"Metade do preço:":<30} {metade(preço):>20}')
    print(f'{f"{aumento}% Adição:":<30} {aumentar(preço, aumento):>20}')
    print(f'{f"{redução}% de Redução:":<30} {diminuir(preço, redução):>20}')
    print('_'*50)


def aumentar(valor=0, percent=0, formatar=True):
    percent = percent / 100
    aumento = valor * percent
    resultado = valor + aumento
    return resultado if formatar is False else moeda(resultado)


def diminuir(valor=0, percent=0, formatar=True):
    percent = percent / 100
    devedor = valor * percent
    resultado = valor - devedor
    return resultado if formatar is False else moeda(resultado)


def metade(valor=0, formatar=True):
    resultado = valor / 2
    return resultado if formatar is False else moeda(resultado)


def dobro(valor=0, formatar=True):
    resultado = valor * 2
    return resultado if formatar is False else moeda(resultado)


def moeda(valor=0.0, money='R$'):
    retorno = f'{money}{valor:.2f}'
    return retorno.replace('.', ',')
