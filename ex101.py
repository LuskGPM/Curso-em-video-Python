"""
def teste(b):
    global a
    a = 8
    b += 2
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 4
teste(a)
print(f'a fora é {a}')

def soma(a=0, b=0, c=0):
    s = a + b + c
    return s


print(soma(4, 9))
"""



def voto():
    from datetime import date

    ano_atual = date.today().year
    idade = ano_atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


try:
    ano = int(input('Ano de nascimento: '))
except ValueError:
    ano = int(input(f'Digite o ano em um número inteiro: '))
print(voto())
