cache = input().split()
count = 0
dict = {}
for i in cache:
    for f in cache[:cache.index[i]]:
        if f == i:
            count += 1
    dict[i] = count
print(dict)