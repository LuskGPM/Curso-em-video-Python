def escreva(valor):
    valor.strip()
    tamanho = len(valor) + 5
    print('=' * tamanho)
    print(f"{valor:^{tamanho}}")
    print('=' * tamanho)


escreva(str(input('Escreva algo: ')))
escreva(str(input('Escreva algo: ')))