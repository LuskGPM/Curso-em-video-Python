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


def ler_float(f):
    from sty import fg
    while True:
        # Substitui vírgula por ponto
        dado_final = f.replace(',', '.')
        try:
            # Tenta converter para float
            dado_final = float(dado_final)
            return dado_final

        except ValueError:
            print(fg.red + 'ERRO. Você digitou um valor incorretamente' + fg.rs)
            f = input('Tente novamente: ')  # Solicita novo valor caso falhe
