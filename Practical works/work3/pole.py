import random

lives = 3
words = ['книга']
secret_word = random.choice(words)
shows = ['\u25A0 ','\u25A0 ', '\u25A0 ','\u25A0 ', '\u25A0']
guess = ''
places = []
print(*shows, '|', lives)
while True:
    guess = input('Введите букву или слово целиком: ')
    #if guess in secret_word and guess!=secret_word:   #проверка на то, что угадали именно букву
     #   numbers = shows.count(guess)
    #    while numbers >=1:                     #получаю индексы угаданных букв в слове
     #       places.append(shows.index(guess))
     #       shows.remove[guess]
     #   for i in places:
      #      shows.insert(i,secret_word[i])#открывю угаданные буквы
    if guess in secret_word and guess!=secret_word:
        shows.pop(secret_word.find(guess))
        shows.insert(secret_word.find(guess), guess)
        print(*shows, '|', lives)

    if guess == secret_word:    #правльный кусок кода
        for i in range(len(shows)):
            shows[i] = secret_word[i]

    if guess not in secret_word:
        print('Неправильно.Вы теряете жизнь')
        lives -= 1

    if ('\u25A0') not in shows:
        print("Вы выиграли! Приз в студию!")
        break

    if lives==0:
        print("Вы проиграли.")
        break