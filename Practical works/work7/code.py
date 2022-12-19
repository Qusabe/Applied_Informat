import csv
def get_books(pattern):
    books = []
    with open('books.csv',mode='r',encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='|')
        for line in reader:
            if pattern in line[1]:
                books.append(line)
    return books


def get_totals(liist):
    result = []
    for line in liist:
        price = float(line[3])*float(line[4])
        if price > 500:
            result.append((line[0], price))
        else:
            result.append((line[0], price+100))
    return result

a = get_books('Python')
b = get_totals(a)
print(a)
print(b)