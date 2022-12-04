def masking(slovo):
    cache = [i for i in slovo]
    mask = '\u25A0 '
    for i in range(len(cache)):
        cache[i] = mask
    total = ''
    return total.join(cache)

print(masking('AAA'))