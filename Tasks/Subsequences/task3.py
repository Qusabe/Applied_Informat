spisok = [int(i) for i in input().split()]
for i in range(len(spisok)):
    spisok[i], spisok[i+1] = spisok[i+2],spisok[i+3]
    if i == (len(spisok) - 4):
        break
print(*spisok)