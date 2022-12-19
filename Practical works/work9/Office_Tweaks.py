import os
from pdf2docx import parse
from docx2pdf import convert
from PIL import Image



def get_menu():
    catalog = os.getcwd()
    choice = int(input(f'\nТекущий каталог: {catalog}\n\n'
                            'Выберите действие:\n\n'
                            '0. Сменить рабочий каталог\n'
                            '1. Преобразовать PDF в Docx\n'
                            '2. Преобразовать Docx в PDF\n'
                            '3. Произвести сжатие изображений\n'
                            '4. Удалить группу файлов\n'
                            '5. Выход\n\n'
                            'Ваш выбор: '))
    if choice == 0:
        answer = input('Укажите корректный путь к рабочему каталогу: ')
        if os.path.exists(answer) == True:
            os.chdir(answer)
        else:
            print('Такого каталога нет')
    if choice == 1:
        convert_PDF_to_Docx(catalog)
    if choice == 2:
        convert_Docx_to_PDF(catalog)
    if choice == 3:
        compress_image(catalog)
    if choice == 4:
        deleting_files(catalog)
    if choice == 5:
        return 0
    return get_menu()


def convert_PDF_to_Docx(catalog):
    print('Список файлов с расширением .pdf в данном каталоге:')
    list_of_files = os.listdir(catalog)
    PDF_files = []
    count = 0
    for file in list_of_files:
        if '.pdf' in file:
            count = count + 1
            print(f'{count}. {file}')
            PDF_files.append(file)
    answer = int(input('Введите номер файла для преобразования '
                            '(чтобы преобразовать все файлы из данного католога введите 0): '))

    if answer == 0:
        for file in PDF_files:
            pdf_file = fr'{catalog}\{file}'
            docx_file = fr'{catalog}\{file}'
            docx_file = docx_file.replace('.pdf', '.docx')
            parse(pdf_file, docx_file)
    else:
        pdf_file = fr'{catalog}\{PDF_files[answer - 1]}'
        docx_file = fr'{catalog}\{PDF_files[answer - 1]}'
        docx_file = docx_file.replace('.pdf', '.docx')
        parse(pdf_file, docx_file)


def convert_Docx_to_PDF(catalog):
    print('Список файлов с расширением .Docx в данном каталоге:')
    list_of_files = os.listdir(catalog)
    Docx_files = []
    count = 0
    for file in list_of_files:
        if '.docx' in file:
            count = count + 1
            print(f'{count}. {file}')
            Docx_files.append(file)
    answer = int(input('Введите номер файла для преобразования '
                            '(чтобы преобразовать все файлы из данного католога введите 0): '))

    if answer == 0:
        for file in Docx_files:
            pdf_file = fr'{catalog}\{file}'
            docx_file = fr'{catalog}\{file}'
            pdf_file = pdf_file.replace('.docx', '.pdf')
            convert(docx_file, pdf_file)
    else:
        pdf_file = fr'{catalog}\{Docx_files[answer - 1]}'
        docx_file = fr'{catalog}\{Docx_files[answer - 1]}'
        pdf_file = pdf_file.replace('.docx', '.pdf')
        convert(docx_file, pdf_file)


def compress_image(catalog):
    print("Список файлов с расширением ('.jpeg', '.gif', '.png' ,'.jpg') в данном каталоге:")
    list_of_files = os.listdir(catalog)
    image_files = []
    count = 0
    for file in list_of_files:
        if ('.jpeg' in file) or ('.gif' in file) or ('.png' in file) or ('.jpg' in file):
            count = count + 1
            print(f'{count}. {file}')
            image_files.append(file)
    answer = int(input('Введите номер файла для преобразования '
                            '(чтобы преобразовать все файлы из данного католога введите 0): '))
    answer2 = int(input('Введите параметры сжатия (от 0 до 100%): '))
    if answer == 0:
        for file in image_files:
            image_path = file
            image_file = Image.open(image_path)
            image_file.save(image_path, quality=answer2)
    else:
        image_path = image_files[answer - 1]
        image_file = Image.open(image_path)
        image_file.save(image_path, quality=answer2)


def deleting_files(catalog):
    answer = int(input('Выберите действие:\n\n'
                            '1. Удалить все файлы начинающиеся на определённую подстроку\n'
                            '2. Удалите все файлы заканчивающиеся на определённую подстроку\n'
                            '3. Удалить все файлы содержащие определённую подстроку\n'
                            '4. Удалить все файлы по расширению\n'
                            'Введите номер действия: '))
    answer2 = input('Введите подстроку: ')
    list_of_files = os.listdir(catalog)
    if answer == 1:
        for file in list_of_files:
            if file.startswith(answer2) == True:
                os.remove(fr"{catalog}\{file}")
                print(f'Файл: {file} успешно удалён!')
    if answer == 2:
        for file in list_of_files:
            if (answer2 + '.') in file:
                os.remove(fr"{catalog}\{file}")
                print(f'Файл: {file} успешно удалён!')
    if answer == 3:
        for file in list_of_files:
            if (answer2) in file:
                os.remove(fr"{catalog}\{file}")
                print(f'Файл: {file} успешно удалён!')
    if answer == 4:
        for file in list_of_files:
            if ('.' + answer2) in file:
                os.remove(fr"{catalog}\{file}")
                print(f'Файл: {file} успешно удалён!')


get_menu()