mask = '\u25A0'
def masking(slovo):
    cache = [i for i in slovo]

    for i in range(len(cache)):
        cache[i] = mask
    total = ''
    return total.join(cache)

def unmasking(secret_word, masked_word, guess):
    all_guess_indexes = []
    masked_word_list = [i for i in masked_word]
    total = ''
    for i in range(0,len(secret_word)):
        if secret_word[i] == guess:
            all_guess_indexes.append(i)

    for j in all_guess_indexes:
        masked_word_list[j] = guess

    return total.join(masked_word_list)