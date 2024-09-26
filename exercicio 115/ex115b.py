def salvar_dados(nome, idade):
    with open('dados_pessoas.txt', 'a') as arquivo:
        arquivo.write(f'Nome: {nome} Idade: {idade}\n')


def ler_dados():
    try:
        with open('dados_pessoas.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            if linhas:
                for linha in linhas:
                    print(linha.strip())
            else:
                print('O arquivo está vazio')
    except FileNotFoundError:
        print('O arquivo não foi encontrado')


while True:
    opção = int(input('1 ou 2: '))
    if opção == 1:
        nome = str(input('Informe o nome("sair" para sair): ')).strip()
        if nome.lower() == 'sair':
            break
        idade = int(input('Idade: '))

        salvar_dados(nome, idade)
    elif opção == 2:
        ler_dados()

print('Dados salvos com sucesso')
