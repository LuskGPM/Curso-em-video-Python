"""
lista_pessoas = list()
nome_idade = list()
for i in range(3):
    nome_idade.append(str(input('Nome: ')))
    nome_idade.append(int(input('Idade: ')))
    lista_pessoas.append(nome_idade[:])
    nome_idade.clear()
for nome, idade in lista_pessoas:
    print(f'{nome} tem {idade} anos')
"""

lista_pessoas = list()
lista_nome_peso = list()
contagem_pessoa = peso = 0
while True:
    lista_nome_peso.append(str(input('Nome: ')))
    lista_nome_peso.append(float(input('Peso(kg): ')))
    lista_pessoas.append(lista_nome_peso[:])
    lista_nome_peso.clear()
    escolha_user = input('Quer continuar? [S/N]')
    contagem_pessoa += 1
    if escolha_user.strip().lower()[0] == 'n':
        break
for nome, pesos in lista_pessoas:
    peso += pesos
media = peso/contagem_pessoa
print(f'{contagem_pessoa} pessoas foram cadastradas')
for nome, pesos in lista_pessoas:
    if pesos > media:
        print(f'{nome} está acima da média de pesos que é {media}')
    elif pesos == media:
        print(f'{nome} está na média de pesos que é {media}')
    else:
        print(f'{nome} está abaixo da média de pesos que é {media}')
