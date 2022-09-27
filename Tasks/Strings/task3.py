tring = input().lower()
first = tring.find('f')
last = tring.rfind('f')
if first == last:
    print(last)
else: print(first, last)
