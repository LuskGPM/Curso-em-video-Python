from sty import fg

pessoas_cadastradas = list()


def menu_principal():
    print('=' * 40)
    print(f"{fg.li_magenta + 'MENU PRINCIPAL':^40}" + fg.rs)
    print('=' * 40)
    print(f'{fg.yellow + "1" + fg.rs} - {fg.li_blue + "Ver pessoas cadastradas" + fg.rs}')
    print(f'{fg.yellow + "2" + fg.rs} - {fg.li_blue + "Cadastrar nova pessoa" + fg.rs}')
    print(f'{fg.yellow + "3" + fg.rs} - {fg.li_blue + "Sair do sistema" + fg.rs}')
    print('=' * 40)


def menu_pessoas(opção):
    print('=' * 40)
    print(f'{opção:^40}')
    print('=' * 40)


def continuar():
    input('Enter para continuar...')


def validação_de_entrada(mensagem, q_opções=3):
    while True:
        try:
            valor = int(input(fg.green + mensagem + fg.rs))
            if 0 < valor <= q_opções:
                return valor
            else:
                print(fg.red + 'digite o número referente às opções acima' + fg.rs)
        except ValueError:
            print(fg.red + 'Erro, digite um número inteiro válido' + fg.rs)


while True:
    menu_principal()
    option = validação_de_entrada('Sua Opção: ')
    if option == 1:
        menu_pessoas('OPÇÃO 1')
        continuar()
    elif option == 2:
        menu_pessoas('OPÇÃO 2')
        continuar()
    elif option == 3:
        continuar()
        break
