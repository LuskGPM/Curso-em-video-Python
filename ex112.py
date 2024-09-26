from funções import moeda
from funções import vall

preço = vall.ler_float(input('Digite o preço: '))
aumento = vall.ler_float(input('% de aumento: '))
redução = vall.ler_float(input('% redução: '))
moeda.resumo(preço, aumento, redução)
