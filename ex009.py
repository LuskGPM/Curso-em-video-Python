from sty import rs,fg
n = int(input('Número: '))
print(fg.li_yellow + '=' * 12 + fg.rs)
print(fg.li_cyan + f'''{n} * 1 = {n*1}
{n} * 2 = {n*2}
{n} * 3 = {n*3}
{n} * 4 = {n*4}
{n} * 5 = {n*5}
{n} * 6 = {n*6}
{n} * 7 = {n*7}
{n} * 8 = {n*8}
{n} * 9 = {n*9}
{n} * 10 = {n*10}''' +fg.rs)
print(fg.li_yellow + '=' * 12 + fg.rs)
