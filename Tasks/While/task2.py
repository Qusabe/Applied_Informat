x = int(input())
n = 0
while True:
    if 2**n > x:
        break
    else: n += 1
print(n-1, 2**(n-1))