print("==" * 5,'Loja',"==" * 5)
p = float(input('Valor das compras: R$'))
fp = int(input('''Qual a forma de pagamento?
[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista cartão
[ 3 ] Parcelado 2x
[ 4 ] Parcelado 3x
Sua opção: '''))
while fp != 1 and fp != 2 and  fp != 3 and fp != 4:
    fp = int(input('''Tente Novamente!
    [ 1 ] À vista dinheiro/cheque
    [ 2 ] À vista cartão
    [ 3 ] Parcelado 2x
    [ 4 ] Parcelado 3x
    Sua opção: '''))
if fp == 1:
    print(f'Você obteve um desconto de 10% e suas compras irá custar R${p - (p * 0.10):.2f}')
elif fp == 2:
    print(f'Você obteve um desconto de 5% e suas comprar irá custar R${p - (p * 0.5):.2f}')
elif fp == 3:
    print(f'Você não obteve descontos e suas compram irá custar R${p:.2f}')
else:
    print(f'Com o parcelamento suas comprar tiveram um juros de 20% e irá custar R${(p * 0.20) + p:.2f}')
