spisok = list(input().split())
def pig_it(inp):
    pattern = '!?.,\",\',\\,\/'
    for i in inp:
        if i not in pattern:
            cache = i[::-1]
            inp[inp.index(i)] = cache + 'ay'
    # print(spisok)
    for word in inp:
        if word[0] in pattern:
            cache = word[1:] + word[0]
            inp[inp.index(word)] = cache
    return inp
print(*pig_it(spisok))