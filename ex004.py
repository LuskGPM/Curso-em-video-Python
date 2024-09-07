n = input('digite algo')
print(f'''
tipo: {type(n)}
É um número? {n.isalnum()}
Alfanumerico? {n.isalpha()}
espaço? {n.isspace()}''')