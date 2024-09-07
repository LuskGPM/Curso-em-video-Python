op = '''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa'''
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
esc = int(input(f'O que deseja fazer?\n{op}\nEscolha: '))
while esc != 5:
    if esc > 5 or esc < 1:
        esc = int(input(f'Opção inválida, escolha novamente.\n{op}\nEscolha: '))
    elif esc == 1:
        print(f'{n1} + {n2} = {n1 + n2}')
        print('=-=' * 9)
    elif esc == 2:
        print(f'{n1} * {n2} = {n1 * n2}')
        print('=-=' * 9)
    elif esc == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
            print('=-=' * 9)
        elif n1 < n2:
            print(f'{n2} é maior que {n1}')
            print('=-=' * 9)
        else:
            print('Ambos valores são iguais')
            print('=-=' * 9)
    else:
        n1 = int(input('Novo número: '))
        n2 = int(input('Novo número: '))
    esc = int(input(f'O que deseja fazer?\n{op}\nEscolha: '))
print('Tenha um bom dia!')
