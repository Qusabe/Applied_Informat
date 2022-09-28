sp1 = [int(i) for i in input().split()]
sp2 = [int(i) for i in input().split()]
sp3 = []
for i in sp1:
    for n in sp2:
        if i == n:
            sp3.append(n)
a = set(sp3)
print(*a)