classificacao_brasileirao = (
    ("Botafogo", 59),
    ("Flamengo", 56),
    ("Palmeiras", 54),
    ("Fluminense", 52),
    ("Grêmio", 50),
    ("Atlético Mineiro", 49),
    ("São Paulo", 47),
    ("Fortaleza", 46),
    ("Corinthians", 44),
    ("Internacional", 43),
    ("Athletico Paranaense", 42),
    ("Cruzeiro", 41),
    ("Bragantino", 40),
    ("Santos", 39),
    ("Vasco da Gama", 38),
    ("Ceará", 37),
    ("Goiás", 35),
    ("Coritiba", 33),
    ("Bahia", 32),
    ("Atlético Goianiense", 30),
    ("Ponte Preta", 28)
)
nome_times = (time for time, pontos in classificacao_brasileirao)
nome_times_ordenados = sorted(nome_times)
nome_time_buscar = "Botafogo"
print('Os cinco primeiro times são \n ')
for time, pontos in classificacao_brasileirao[:5]:
    print(f'{time} com {pontos} pontos')

print('==' * 20 , '\n')

print('Os 4 últimos times são \n')
for time, pontos in classificacao_brasileirao[-4:]:
    print(f'{time} com {pontos} pontos')

print('==' * 20, '\n')

print(f'os times em ordem alfabética são \n')
for time in nome_times_ordenados:
    print(time)

print('==' * 20, '\n')

for i, (time, pontos) in enumerate(classificacao_brasileirao):
    if time == nome_time_buscar:
        print(f'O {nome_time_buscar} está na {i + 1}° Posição com {pontos} pontos')
