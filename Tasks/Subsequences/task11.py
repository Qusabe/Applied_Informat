st = input()
first = st.find('h')
last = st.rfind('h')       #Почему print(rever[::-1] работает, а print(st[first:last:-1] - нет?
rever = st[first+1:last]
print(st[:first+1] + rever[::-1] + st[last:])
