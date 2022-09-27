a = int(input())
b = int(input())
doska = [['black','white','black','white','black','white','black','white'],
         ['white','black','white','black','white','black','white','black'],
         ['black','white','black','white','black','white','black','black'],
         ['white','black','white','black','white','black','white','black'],
         ['black','white','black','white','black','white','black','white'],
         ['white','black','white','black','white','black','white','black'],
         ['black','white','black','white','black','white','black','white'],
         ['white','black','white','black','white','black','white','black']]
print(doska[b-1][a-1])