n = int(input())
i = 1
spisok = []
while i**2 <= n:
    spisok.append(i**2)
    i += 1
print(*spisok)