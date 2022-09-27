a = int(input())
first = a//1000
sec = a//100%10
trd = a%100//10
lst = a%10%10%10
if first == lst and sec == trd:
    print('yes')
else: print('No')