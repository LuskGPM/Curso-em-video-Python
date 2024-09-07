casa = float(input('Valor da casa: R$'))
s = float(input('Sálario do comprador: R$'))
ano = int(input('Anos de financiamento: '))
prest = casa / (ano * 12)
if prest > s * 0.30:
    ar = "Reprovado pelos valores da parcela excederem"
else:
    ar = "Aprovado pelos valores da parcela não excederem"
print(f'Para pagar uma casa de R${casa} por {ano} anos, a prestação será de R${prest:.2f}.'
      f'\nPortanto o financiamento foi {ar} 30% do seu salário de R${s}')
