def ficha(nome_jogador='<desconhecido>', gol_total=0):
    print(f'O jogador {nome_jogador} fez {gol_total} gol(s)')


nome = str(input('Nome: '))
gol = str(input('Gols: '))

if gol.isdigit():
    gol = int(gol)
else:
    gol = '0'
if nome.strip() == '':
    ficha(gol_total=gol)
else:
    ficha(nome, gol)
