a = int(input())
b = int(input())
c = int(input())
spisok = [a,b,c]
if a == b == c:
    print(3)
elif len(set(spisok)) == 2:
    print(2)
else: print(0)