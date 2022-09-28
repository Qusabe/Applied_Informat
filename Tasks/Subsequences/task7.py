sp1 = [int(i) for i in input().split()]
alr_exst = []
for i in sp1:
    if i in alr_exst:
        print('YES')
    else:
        print("NO")
        alr_exst.append(i)
