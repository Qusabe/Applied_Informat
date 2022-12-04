import random
from replace_symbols import *
spisok = ['книга','месяц','ручка','шарик','олень','носок']
secret_word = random.choice(spisok)
print(masking(secret_word))