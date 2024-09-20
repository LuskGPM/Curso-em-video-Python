# Tupla com 5 itens e seus preços
itens_para_venda = (
    ("Camiseta", 29.99),
    ("Calça Jeans", 89.90),
    ("Tênis", 149.99),
    ("Jaqueta", 199.90),
    ("Óculos de Sol", 79.50)
)

# Exemplo de como acessar e imprimir os itens e seus preços
print('='*40)
print(f'{"Loja":^40}')
print('='*40)
for item, preco in itens_para_venda:
    print(f"{item:.<25} Preço: R${preco:.>5.2f}")
