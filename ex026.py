n = input('Nome: ')
print(f'Letra A aparece {n.strip().upper().count("A")} vezes')
print(f'Letra A aparece pela primeira vez na posição {n.strip().upper().find("A")+1}')
print(f'A letra A aparece pela ultima vez na posição {n.strip().upper().rfind("A")+1}')
