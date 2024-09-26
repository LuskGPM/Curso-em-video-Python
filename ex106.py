from sty import fg, bg
from time import sleep


def pyhelp(msg, cor):
    tamanho = len(msg) + 5
    print(cor + fg.white + '~' * tamanho)
    print(f'{msg:^{tamanho}}')
    print('~' * tamanho)
    print(bg.rs + fg.rs, end='')
    sleep(0.7)


def funct_or_dict(fc_or_di):
    if fc_or_di.strip().upper() == 'FIM':
        return True
    else:
        pyhelp('ACESSANDO PAINEL DE COMANDO', bg.da_blue)
        print(bg.white + fg.da_grey)
        help(fc_or_di)
        print(bg.rs + fg.rs, end='')
        sleep(1)


while True:
    pyhelp('SISTEMA DE AJUDA PyHELP', bg.da_green)
    continuar = funct_or_dict(input('Função ou Biblioteca > '))
    if continuar:
        break

pyhelp('Finalizando, volte sempre', bg.da_grey)
