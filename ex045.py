import sty
from time import sleep
from random import randint

print(sty.bg.white + sty.fg.green + "-="*20 + sty.fg.rs + sty.bg.rs)
print(sty.bg.white+sty.fg.da_cyan + '   VAMOS JOGAR PEDRA, PAPEL E TESOURA!  ' + sty.fg.rs + sty.bg.rs)
print(sty.bg.white + sty.fg.green + "=-"*20 + sty.fg.rs + sty.bg.rs)
print(sty.bg.white + sty.fg.yellow + '[ 1 ] Pedra, [ 2 ] Papel, [ 3 ] Tesoura ' + sty.fg.rs + sty.bg.rs)
esc = int(input(sty.fg.grey + 'Sua escolha: ' + sty.fg.rs))
escm = randint(1, 3)
ppt = ['', 'Pedra', 'Papel', 'Tesoura']
while esc != 1 and esc != 2 and esc != 3:
    print(sty.bg.white + sty.fg.da_red + '           Escolha novamente!           ' + sty.fg.rs + sty.bg.rs)
    esc = int(input(sty.fg.grey + 'Sua escolha: ' + sty.fg.rs))
sleep(1)
print(sty.bg.white + sty.fg.li_grey + '                 Pedra...               ' + sty.fg.rs + sty.bg.rs)
sleep(1)
print(sty.bg.white + sty.fg.li_grey + '                 Papel...               ' + sty.fg.rs + sty.bg.rs)
sleep(1)
print(sty.bg.white + sty.fg.li_grey + '                E TESOURA               ' + sty.fg.rs + sty.bg.rs)
sleep(0.5)
if escm == esc:
    print(sty.bg.white + sty.fg.yellow + '                EMPATAMOS!              ' + sty.fg.rs + sty.bg.rs)
    print(sty.bg.white + sty.fg.yellow + f'Você escolheu {ppt[esc]} e eu escolhi  {ppt[escm]} '+ sty.bg.rs)
elif esc == 1 and escm == 3:
    print(sty.bg.white + sty.fg.green + '              VOCÊ VENCEU!              ' + sty.fg.rs + sty.bg.rs)
    print(sty.bg.white + sty.fg.green + f'Você escolheu {ppt[esc]}, eu escolhi {ppt[escm]} '+ sty.bg.rs)
elif esc == 2 and escm == 1:
    print(sty.bg.white + sty.fg.green + '              VOCÊ VENCEU!              ' + sty.fg.rs + sty.bg.rs)
    print(sty.bg.white + sty.fg.green + f' Você escolheu {ppt[esc]}, eu escolhi {ppt[escm]}  ' + sty.bg.rs)
elif esc == 3 and escm == 2:
    print(sty.bg.white + sty.fg.green + '              VOCÊ VENCEU!              ' + sty.bg.rs)
    print(sty.bg.white + sty.fg.green + f' Você escolheu {ppt[esc]}, eu escolhi {ppt[escm]}' + sty.bg.rs)
elif esc == 1 and escm == 2:
    print(sty.bg.white + sty.fg.red + '                EU VENCI!               ' + sty.fg.rs + sty.bg.rs)
    print(sty.bg.white + sty.fg.red + f' Eu escolhi {ppt[escm]} e você escolheu {ppt[esc]} ' + sty.bg.rs)
elif esc == 3 and escm == 2:
    print(sty.bg.white + sty.fg.red + '                EU VENCI!               ' + sty.fg.rs + sty.bg.rs)
    print(sty.bg.white + sty.fg.red + f'Eu escolhi {ppt[escm]} e você escolheu {ppt[esc]}' + sty.bg.rs)
else:
    print(sty.bg.white + sty.fg.red + '                EU VENCI!               ' + sty.fg.rs + sty.bg.rs)
    print(sty.bg.white + sty.fg.red + f'Eu escolhi {ppt[escm]} e você escolheu {ppt[esc]}' + sty.bg.rs)
