sp1 = [int(i) for i in input().split()]
sp2 = [int(i) for i in input().split()]
count = 0
for i in sp1:
    for n in sp2:
        if i == n:
            count += 1
print(count)