from math import sqrt
s1 = int(input('Segmento 1: '))
s2 = int(input('Segmento 2: '))
s3 = int(input('Segmento 3: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('os segmentos podem formar um triângulo')
else:
    print('os segmentos não podem formar um triângulo')
