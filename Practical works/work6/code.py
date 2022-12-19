import re
pattern = r'Рейс (\d+) (?:прибыл|отправился) (из|в) (\w+) в (\d{2}:\d{2}:\d{2})'

with open('text.txt', mode='r',encoding='utf-8') as text:
    journal = text.read()
    new_journal = re.findall(pattern,journal)
    print(new_journal)

with open('updated_journal.txt', mode='w',encoding = 'utf-8') as update:
    for i in new_journal:
        update.write(f'[{i[3]}] - Поезд №{i[0]} {i[1]} {i[2]}\n')