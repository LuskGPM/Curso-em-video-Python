# Tupla com 10 palavras
palavras = (
    "sol",
    "lua",
    "estrela",
    "ceu",
    "mar",
    "terra",
    "flor",
    "arvore",
    "rio",
    "montanha"
)
vogais = 'aeiou'


# Exemplo de como acessar e imprimir as palavras
def vogais_palavra(palavras):
    return ' '.join([letra for letra in palavras if letra in vogais])


for palavra in palavras:
    vogais_separadas = vogais_palavra(palavra)
    print(f'A palavra {palavra} tem {vogais_separadas}')
