from math import floor,ceil
st = input()
ln = len(st)
first = st[:ceil(ln/2)]
sec = st[floor(ln/2):]
print(sec+first)