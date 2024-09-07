nome = input('Nome: ')
print(f'''Maiúsculo: {nome.upper()}
Minúsculo: {nome.lower()}
Número de letras: {len(''.join(nome.split()))}
Primeiro nome: {nome.split()[0]} e tem {len(nome.split()[0])}''')
