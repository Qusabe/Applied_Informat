import difficulty, random
import record_handler as rec_h
from replace_symbols import *
spisok = open("spisok.txt")
def win():
    print("Вы выиграли!")
    rec_h.current_session_record += 1

    if rec_h.current_session_record > rec_h.record:
        print("Ваш новый рекорд угаданных подряд слов - " + str(rec_h.current_session_record))
        rec_h.record = rec_h.current_session_record
        rec_h.update_record()


def start():
    with open('spisok.txt', encoding = "utf-8") as  spsk:
        spisok = spsk.read().readlines()
    secret_word = random.choice(spisok).lower()
    lives = difficulty.quantity_of_lives()
    masked = masking(secret_word)
    while True:
        print(f'{masked} | lives = {lives}')
        guess = input("Назовите букву или слово целиком\n: ").lower()
        if guess == secret_word:
            win()
            break
        elif guess in secret_word:
            if guess in masked:
                print("Эта буква уже открыта!")
            else:
                print("Правильно!")
                masked = unmasking(secret_word,masked,guess)

            if mask not in masked:
                win()
                break

        else:
            print("Неправильно. Вы теряете жизнь")
            lives -= 1

        if lives == 0:
            print("Жизни закончились. Вы проиграли")
            print("Ваш рекорд - " + str(rec_h.record))
            break