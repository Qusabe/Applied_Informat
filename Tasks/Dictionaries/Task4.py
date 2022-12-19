number_of_lines = int(input())
words_list = []
for i in range(number_of_lines):
    line = input().split(' ')
    for j in line:
        words_list.append(j)
words_list = sorted(words_list)

max = 0
answer = ""
for i in words_list:
    if words_list.count(i) > max:
        answer = i
        max = words_list.count(i)
print(answer)
