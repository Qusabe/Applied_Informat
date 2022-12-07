cache = input().split()
sentence = ''
count = []
for i in cache:
    count.append(sentence.count(i))
    sentence += i
print(*count)