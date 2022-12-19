number_of_writes = int(input())
dict = {}
for i in range(number_of_writes):
    last_name, quantity_of_people = input().split(' ')
    if last_name in dict:
        dict[last_name] = str(int(quantity_of_people) + int(dict[last_name]))
    else:
        dict[last_name] = quantity_of_people

for last_name, quantity_of_people in sorted(dict.items()):
    print(last_name + ' ' + quantity_of_people)