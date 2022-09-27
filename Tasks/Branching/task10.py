a = int(input())
b = int(input())
doska = [['white','black','white','black','white','black','white','black'],
         ['black','white','black','white','black','white','black','white'],
         ['white','black','white','black','white','black','white','black'],
         ['black','white','black','white','black','white','black','white'],
         ['white','black','white','black','white','black','white','black'],
         ['black','white','black','white','black','white','black','white'],
         ['white','black','white','black','white','black','white','black'],
         ['white','black','white','black','white','black','white','black']]    #Я взял так, что начало доски находится снизу,
                                                                                #из-за чего ответы и получились иными
print(doska[b-1][a-1])