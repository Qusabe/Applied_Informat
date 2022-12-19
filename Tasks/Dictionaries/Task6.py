dict = {}
number_of_lines = int(input())
for i in range(number_of_lines):
    cities = input().split()
    for city in cities[1:]:
        dict[city] = cities[0]

cities_list = []
number_of_cities = int(input())
for i in range(number_of_cities):
    cities_list.append(dict.get(input()))
    
for i in cities_list:
    print(i)