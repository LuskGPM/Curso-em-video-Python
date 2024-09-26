from sty import fg


def ler_int(i):
    from sty import fg

    while True:
        try:
            # Solicita valor inteiro diretamente
            number = int(i)
            return number

        except ValueError:
            print(fg.red + 'ERRO, digite um número inteiro válido' + fg.rs)
            i = input('Tente novamente: ')


def menu_principal():
    menu = ['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema']
    print('=' * 40)
    print(f"{fg.li_magenta + 'MENU PRINCIPAL':^40}" + fg.rs)
    print('=' * 40)
    for i, opt in enumerate(menu):
        print(fg.yellow + f'{i + 1}' + fg.rs + f' - {fg.li_blue + opt + fg.rs}')
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


def salvar_dados():
    nome = str(input('Nome: '))
    idade = ler_int(input('Idade: '))
    with open('dados_pessoas.txt', 'a') as arquivo:
        arquivo.write(f'{nome:<24} {idade:>10} anos\n')
        print(f'{nome} Cadastrado(a) com sucesso')


def ler_dados():
    try:
        with open('dados_pessoas.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            if linhas:
                print('=' * 40)
                for linha in linhas:
                    print(linha.strip())
                print('=' * 40)
            else:
                print('O arquivo está vazio')
    except FileNotFoundError:
        print('O arquivo não foi encontrado')
