a = int(input()) # горизонталь
b = int(input()) #  вертикаль
a1 = int(input())
b1 = int(input())
doska = [['black','white','black','white','black','white','black','white'],
         ['white','black','white','black','white','black','white','black'],
         ['black','white','black','white','black','white','black','black'],
         ['white','black','white','black','white','black','white','black'],
         ['black','white','black','white','black','white','black','white'],
         ['white','black','white','black','white','black','white','black'],
         ['black','white','black','white','black','white','black','white'],
         ['white','black','white','black','white','black','white','black']]
clr1 = doska[a-1][b-1]
clr2 = doska[a1-1][b1-1]
if clr1 == clr2:
    print('Yes')
else: print('No')