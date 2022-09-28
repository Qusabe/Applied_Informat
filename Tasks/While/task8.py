count_max = 0
count = 0
n = 1
n0 = 0
while n != 0:
    n = int(input())
    if n == n0:
        count += 1
        if count_max < count:
            count_max = count
        else: continue
    else: count = 0
    n0 = n
count_max += 1
print(count_max)