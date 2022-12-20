import pymorphy2
import operator
import translate

def get_normal_form(word):
    morph = pymorphy2.MorphAnalyzer()
    return morph.parse(word)[0].normal_form

def normalize_words_list(words_list):
    for i in range(len(words_list)):
        letters = [a for a in words_list[i] if a.isalpha()]
        word = "".join(letters)
        words_list[i] = get_normal_form(word)
    return words_list

def get_sorted_dict(words):
    words_in_dict = {}
    for word in words:
        words_in_dict[word] = str(words.count(word))
    if '' in words_in_dict :
        words_in_dict.pop('')
    return  dict(sorted(words_in_dict.items(), key=operator.itemgetter(1), reverse=True))

def write_dict_to_file(file, dict):
    en_translator = translate.Translator(from_lang='ru', to_lang='en')

    with open(file, encoding='utf-8',mode='w') as file:
        for word in dict:
            file.write(f'{word} | {en_translator.translate(word)} | {dict[word]}\n')

def get_english_phrasebook(file_name: str, phrasebook: str):
    with open(file_name, "r", encoding='utf-8') as file:
        list = file.read().split()
        write_dict_to_file(phrasebook, get_sorted_dict(normalize_words_list(list)))

get_english_phrasebook('data.txt', 'phrasebook.txt')