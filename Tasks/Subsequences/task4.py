spisok = [int(i) for i in input().split()]
mx = spisok.index(max(spisok))
mn = spisok.index(min(spisok))
v1 = spisok[mx]
v2 = spisok[mn]
spisok[mx] = v2
spisok[mn] = v1
print(*spisok)