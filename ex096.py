"""
def dobra(lst):
    for i in range(len(lst)):
        lst[i] *= 2


valores = [2, 4, 7, 9, 5]
dobra(valores)
print(valores)
"""


def área(largura, comprimento):
    area = largura * comprimento
    print(f'A largura do terreno é {largura}m², o comprimento é {comprimento}m² e sua área é {area:,}m²')


área(float(input('Largura do terreno(m²): ')), float(input('Comprimento do terreno(m²): ')))
