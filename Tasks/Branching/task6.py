a = int(input())
first = a//100
sec = (a//10)%10
last = a%10%10
if first < sec and first < last:
    if sec < last:
        print('Yes')
    else: print('No')
else:
    print('No')