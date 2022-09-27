a = int(input())
b = int(input())
months = [31,28,31,30,31,30,31,31,30,31,30,31]
if 0<b<months[a-1] and 0<a<13:
    print(f'{b+1}-{a}-2022')
elif a == months[a-1] and 0<a<12:
    print(f'1-{a+1}-2022')
elif b == months[a-1] and a == 12:
    print(f'1-1-2023')
elif b == months[a-1] and 0<a<12:
    print(f'1-{a+1}-2022')
else: print('Try again')