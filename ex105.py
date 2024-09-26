def notas(* n, sit=False):
    notas_di = dict()

    media_notas = sum(n)/len(n)
    notas_di['total'] = len(n)
    notas_di['maior'] = max(n)
    notas_di['menor'] = min(n)
    notas_di['média'] = media_notas
    if sit:
        if media_notas < 6:
            notas_di['situação'] = 'Péssima'
        elif 7 > media_notas > 6:
            notas_di['situação'] = 'Boa'
        else:
            notas_di['situação'] = 'Excelente'
    return notas_di


resp = notas(2, 7, 8.0, 9.5, sit=True)
print(resp)
