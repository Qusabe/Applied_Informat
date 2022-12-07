import code
def game():
    while True:
        command = int(input('1 - Начать игру, 2 - Выход \n'))

        if command == 1:
            code.start()
            print("Хотите сыграть ещё?")
        elif command == 2:
            break
game()