min = int(input())
if 0<min<1441:

    hours = min//60
    minuts = min%60
    print(f'{hours}:{minuts}')
else:
    print('Try again')