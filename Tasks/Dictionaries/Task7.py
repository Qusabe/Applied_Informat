dict = {}
number_of_lines = int(input())
for i in range(number_of_lines):
    line = input().split()
    for j in line:
        dict[j] = dict.get(j,0) + 1

for i in sorted(dict,key = dict.get,reverse=True):
    print(i, dict[i])