def read_file(file_name: str) -> list:
    with open(file_name, encoding='utf-8') as f:
        cache: list = f.read().split()

    for i in range(len(cache)):
        cache[i] = cache[i].lower()
        cache[i] = "".join(a for a in cache[i] if a.isalpha())

    for word in cache:
        if word=='' or len(word) == 1:
            cache.remove(word)
    output_text: set = set(cache)

    return list(output_text)

def save_file(file_name: str, words: list):
    Unique: list = sorted(words)
    with open(file_name, mode='w', encoding = "utf-8") as file:
        file.write("Всего уникальных слов: " + str(len(Unique)))
        file.write('\n========================\n')
        file.write('\n'.join(words))
        return file

