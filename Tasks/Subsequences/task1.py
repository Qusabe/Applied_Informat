
spisok = [int(s) for s in input().split()]
lst = [i for i in spisok if i % 2 != 0]
print(*lst)