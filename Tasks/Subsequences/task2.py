spisok = [int(i) for i in input().split()]
lst = []
i = 1
while i <= len(spisok):
    if spisok[i] > spisok[i-1]:
        lst.append(spisok[i])
    if spisok[i] == spisok[-1]:
        break
    i += 1
print(*lst)
