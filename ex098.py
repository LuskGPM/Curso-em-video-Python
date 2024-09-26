from time import sleep


def contador(inicio, fim, saltos):
    print(f'\ncontando de {inicio} até {fim} pulando {saltos} números')
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(cont, end=' ', flush=True)
            cont += saltos
            sleep(0.5)
    else:
        cont = inicio
        while cont >= fim:
            print(cont, end=' ', flush=True)
            cont -= saltos
            sleep(0.5)


contador(0, 10, 1)
contador(10, 0, 1)
contador(int(input('\nDigite o valor inicial: ')), int(input('Digite o valor final: ')), int(input('Digite a razão: ')))