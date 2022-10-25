import random

def birthdays():
    sucesses = 0
    for i in range (1, 100000):
        test = [random.randint(1,365) for i in range(23)]
        if len(test) != len(set(test)):
            sucesses += 1
        else:
            continue
    result = sucesses/100000
    print(result)