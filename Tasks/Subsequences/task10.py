st = input()
first = st.find('h')
last = st.rfind('h')
print(st[:first] + st[last+1:])
