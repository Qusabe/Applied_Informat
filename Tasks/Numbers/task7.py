year = int(input())
if year %100 == 00:
    century = year//100
else:
    century = year//100 + 1
print(century)