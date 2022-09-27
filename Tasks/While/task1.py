a = int(input())
for i in range(1,1000):
    if a % i == 0 and i != 1:
        print(i)
        break