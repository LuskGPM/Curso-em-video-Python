from time import sleep

gerenciamento = dict()
gols_lista = list()

total_de_gols = 0
nome_jogador = str(input('Nome do jogador: '))
numero_de_partidas = int(input('Numero de partidas jogadas: '))

for i in range(numero_de_partidas):
    gols_partidas = int(input(f'Quantos gols na partida {i + 1}? '))
    total_de_gols += gols_partidas
    gols_lista.append(gols_partidas)

gerenciamento['Nome'] = nome_jogador
gerenciamento['Gols'] = gols_lista
gerenciamento['total'] = total_de_gols

print('=-'*25)
print(gerenciamento)
print('=-'*25)

for k, v in gerenciamento.items():
    print(f'O campo {k} tem valor {v}')
    sleep(0.7)
print('=-'*25)

print(f'O jogador {gerenciamento["Nome"]} jogou {len(gols_lista)} partidas')
for i in range(len(gols_lista)):
    print(f'Na partida {i + 1} marcou {gerenciamento["Gols"][i]}')
    sleep(0.7)
print(f"Totalizando {gerenciamento['total']} gols")
