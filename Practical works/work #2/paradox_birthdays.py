import random

def birthdays():
    sucesses = 0
    for i in range (1, 1000):
        test = [random.randint(1,365) for i in range(23)]
        if len(test) != len(set(test)):
            sucesses += 1
        else:
            continue
    result = int((sucesses/1000)*100))
    print(result)