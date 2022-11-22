def read_file(file_name: str) -> list:
    try:
        file:list = open(file_name)
        count: int = int(file.readline())
        cache: list = file.read().splitlines()
        if (len(cache) > count) or (len(cache) < count):
            raise Exception('Ошибка: Количество не совпадает')
        cache = [int(cache[i]) for i in range(0,count)]
        return cache
    except FileNotFoundError:
        return ("Файл не найден")
    except UnicodeDecodeError:
        return ('Ошибка: В файле содержится текст')
    except ValueError:
        return ('Ошибка: Не все файлы в файле - числа')
    except TypeError:
        return ('Ошибка: В файле не все элементы числа')
    except Exception as unexpected_exception:
        return ('Ошибка:'+str(unexpected_exception))
    finally:
        try:
            file.close()
        except:
            print("Удивительно")