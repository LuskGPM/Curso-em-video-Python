jogadores = list()

while True:
    total_gols = 0
    jogador = dict()
    todos_gols = list()
    jogador['nome'] = str(input('Nome do jogador: ')).capitalize().strip()
    try:
        n_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
        while n_partidas < 0:
            n_partidas = int(input('O número de partidas não pode ser negativo: '))
    except ValueError:
        n_partidas = int(input('Digite em número inteiro a quantidade de partida: '))
    for i in range(n_partidas):
        try:
            gols = int(input(f"Quantos gols na {i + 1}° Partida? "))
            while gols < 0:
                gols = int(input('O número de gols não pode ser negativo: '))
        except ValueError:
            gols = int(input('Digite a quantidade de gols em números inteiros: '))
        total_gols += gols
        todos_gols.append(gols)
    jogador['gols'] = todos_gols
    jogador['total'] = total_gols
    jogadores.append(jogador.copy())

    continuar = str(input('Continuar?[S/N]: ')).strip().upper()

    while continuar[0] not in "SN":
        continuar = str(input('Digite "S" ou "N"'))
    if continuar[0] == 'N':
        break
print('=-' * 26)
print(f"{'cod':<5}{'nome':<10}{'gols':^30}{'total':>10}")
print('__'*26)
for i, value in enumerate(jogadores):
    print(f"{i:<5}{value['nome']:<10}{str(value['gols']):^30}{value['total']:>10}")
print('__'*26)
while True:
    try:
        id_jogador = int(input('Mostrar dados de qual jogador (999 para sair): '))
    except ValueError:
        id_jogador = int(input('Digite o número correspondente ao código do jogador: '))
    if id_jogador == 999:
        break
    print('__'*20)
    for i, value in enumerate(jogadores):
        if i == id_jogador:
            print(f"MOSTRANDO DADOS DO JOGADOR {value['nome']}")
            for c in range(len(value['gols'])):
                print(f"No {c + 1}° jogo fez: {value['gols'][c]}")
            print("__"*20)
print('<< ENCERRADO >>')
