cache = input().split()
answer = '0 '
for i in range(len(cache)):
    count = 0
    for j in range(0,i):
        if cache[i] == cache[j]:
            count += 1
        if j == (i-1):
            answer = answer+f'{count} '
print(answer)