lives = 0

def quantity_of_lives():
    difficulty = int(input("Выберите сложность: \n1 - Лёгкая\n2-Нормальная\n3-Сложная\n"))
    if difficulty == 1:
        return 1000000000
    elif difficulty == 2:
        return 5
    elif difficulty == 3:
        return 3
    else:
        print('Неверная сложность')
        return quantity_of_lives()
