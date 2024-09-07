import math

ang = float(input('Angulo: '))
s = math.sin(math.radians(ang))
c = math.cos(math.radians(ang))
t = math.tan(math.radians(ang))
print(f'Seno: {s:.2f} \nCosseno: {c:.2f}\n Tangente: {t:.2f}')