st = input()
first = st.find('h')
last = st.rfind('h')
rever = st[first+1:last]
rever = rever.replace('h','H')
print(st[:first+1] + rever + st[last:])