dict = {}
number_of_pairs = int(input())

for i in range(number_of_pairs):
    synonim, synonim2 = input().split()
    dict[synonim] = synonim2

reversed_dict = {}
for key, item in dict.items():
    reversed_dict[item] = key

inp = input()
print(reversed_dict.get(inp))